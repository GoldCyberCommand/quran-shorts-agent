"""quran-shorts-agent CLI.

Commands:
  scan     - show which new source videos would be cut, and where
  process  - render new Shorts into the queue
  upload   - upload queued Shorts to YouTube (drip-fed per run)
  run      - process + upload (the scheduled entrypoint)
  status   - ledger summary
  auth     - one-time YouTube OAuth flow
"""
import argparse
import os
import re
import sys

from . import segments as seg
from . import state as st
from .config import load_config
from .render import render_short

VIDEO_EXTS = {".mp4", ".mov", ".m4v", ".mkv"}
_SURAH_RE = re.compile(r"surah_(\d+)_(.+)", re.IGNORECASE)


def _find_sources(cfg):
    found = []
    for src_dir in cfg["source_dirs"]:
        if not os.path.isdir(src_dir):
            print("warning: source dir missing: %s" % src_dir, file=sys.stderr)
            continue
        for dirpath, _, filenames in os.walk(src_dir):
            for name in sorted(filenames):
                if os.path.splitext(name)[1].lower() in VIDEO_EXTS:
                    found.append(os.path.join(dirpath, name))
    return sorted(found)


def _surah_label(path):
    stem = os.path.splitext(os.path.basename(path))[0]
    m = _SURAH_RE.match(stem)
    if m:
        return "Surah %s" % m.group(2).replace("_", " ")
    return stem.replace("_", " ")


def _fmt_ts(t):
    return "%d:%05.2f" % (int(t // 60), t % 60)


def _fill(template, short):
    return (template.replace("{surah}", short["surah"])
                    .replace("{n}", str(short["part"])))


def cmd_scan(cfg, args):
    state = st.load_state(cfg["state_file"])
    new = [p for p in _find_sources(cfg) if p not in state["sources"]]
    if not new:
        print("No new source videos.")
        return
    for path in new:
        segs, method = seg.find_segments(path, cfg["segment"])
        print("%s  (%s)" % (path, method))
        if not segs:
            print("  no usable segments found")
        for i, (s, e) in enumerate(segs, 1):
            print("  part %d: %s - %s  (%.1fs)" % (i, _fmt_ts(s), _fmt_ts(e), e - s))


def cmd_process(cfg, args):
    state = st.load_state(cfg["state_file"])
    queue_dir = cfg["queue_dir"]
    os.makedirs(queue_dir, exist_ok=True)
    new = [p for p in _find_sources(cfg) if p not in state["sources"]]
    if args.limit:
        new = new[: args.limit]
    if not new:
        print("No new source videos to process.")
        return

    for path in new:
        segs, method = seg.find_segments(path, cfg["segment"])
        stem = os.path.splitext(os.path.basename(path))[0]
        surah = _surah_label(path)
        rendered = []
        print("Processing %s (%s, %d segment(s))" % (path, method, len(segs)))
        for i, (s, e) in enumerate(segs, 1):
            out_name = "%s_part%d.mp4" % (stem, i)
            out_path = os.path.join(queue_dir, out_name)
            render_short(path, s, e, out_path,
                         cfg["video"]["width"], cfg["video"]["height"],
                         cfg["video"]["background"])
            short = {
                "file": out_path,
                "source": path,
                "surah": surah,
                "part": i,
                "start": round(s, 2),
                "end": round(e, 2),
                "method": method,
                "uploaded": False,
                "video_id": None,
            }
            state["shorts"].append(short)
            rendered.append(out_name)
            print("  rendered %s (%.1fs)" % (out_name, e - s))
        state["sources"][path] = {"segments": len(segs), "method": method,
                                  "shorts": rendered}
        st.save_state(cfg["state_file"], state)
    print("Queue now holds %d pending Short(s)."
          % len(st.pending_uploads(state)))


def cmd_upload(cfg, args):
    from . import youtube as yt
    state = st.load_state(cfg["state_file"])
    pending = st.pending_uploads(state)
    if not pending:
        print("Nothing queued for upload.")
        return
    limit = args.limit or cfg["upload"]["max_uploads_per_run"]
    batch = pending[:limit]

    up = cfg["upload"]
    if args.dry_run:
        for short in batch:
            title = _fill(up["title_template"], short)
            print("[dry-run] would upload %s as %r (%s)"
                  % (short["file"], title, up["privacy_status"]))
        return

    service = yt.get_service()
    for short in batch:
        title = _fill(up["title_template"], short)
        description = _fill(up["description_template"], short)
        print("Uploading %s ..." % os.path.basename(short["file"]))
        video_id = yt.upload_video(
            service, short["file"], title, description,
            up["tags"], up["category_id"], up["privacy_status"])
        short["uploaded"] = True
        short["video_id"] = video_id
        st.save_state(cfg["state_file"], state)
        print("  https://youtube.com/shorts/%s" % video_id)
    remaining = len(st.pending_uploads(state))
    print("Done. %d Short(s) still queued." % remaining)


def cmd_run(cfg, args):
    cmd_process(cfg, args)
    cmd_upload(cfg, args)


def cmd_status(cfg, args):
    state = st.load_state(cfg["state_file"])
    uploaded = [s for s in state["shorts"] if s.get("uploaded")]
    print("Sources processed: %d" % len(state["sources"]))
    print("Shorts rendered:   %d" % len(state["shorts"]))
    print("Shorts uploaded:   %d" % len(uploaded))
    print("Shorts queued:     %d" % len(st.pending_uploads(state)))
    for short in uploaded[-5:]:
        print("  %s -> https://youtube.com/shorts/%s"
              % (os.path.basename(short["file"]), short["video_id"]))


def cmd_auth(cfg, args):
    from . import youtube as yt
    yt.run_auth_flow()


def main(argv=None):
    parser = argparse.ArgumentParser(prog="qsa", description=__doc__)
    sub = parser.add_subparsers(dest="command")
    sub.required = True
    for name, fn in [("scan", cmd_scan), ("process", cmd_process),
                     ("upload", cmd_upload), ("run", cmd_run),
                     ("status", cmd_status), ("auth", cmd_auth)]:
        p = sub.add_parser(name)
        p.add_argument("--limit", type=int, default=0,
                       help="max items this run (0 = config default)")
        p.add_argument("--dry-run", action="store_true",
                       help="upload: print what would be uploaded, send nothing")
        p.set_defaults(fn=fn)
    args = parser.parse_args(argv)
    cfg = load_config()
    args.fn(cfg, args)


if __name__ == "__main__":
    main()
