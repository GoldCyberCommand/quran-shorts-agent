"""Find meaningful segments in a recitation video.

Primary method: recitation-pause detection via ffmpeg silencedetect —
pauses between ayat are natural cut points. If a sidecar file
"<video>.highlights" exists next to the source, its timestamps are used
instead (one "start-end" range per line, seconds or mm:ss)."""
import os
import re
import subprocess

_SILENCE_START = re.compile(r"silence_start:\s*([0-9.]+)")
_SILENCE_END = re.compile(r"silence_end:\s*([0-9.]+)")


def probe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def detect_speech_chunks(path, silence_db, silence_min_seconds, duration):
    """Return [(start, end)] intervals of recitation between pauses."""
    silence_filter = "silencedetect=noise={}dB:d={}".format(
        silence_db, silence_min_seconds)
    proc = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", path,
         "-af", silence_filter, "-f", "null", "-"],
        capture_output=True, text=True,
    )
    starts, ends = [], []
    for line in proc.stderr.splitlines():
        m = _SILENCE_START.search(line)
        if m:
            starts.append(float(m.group(1)))
            continue
        m = _SILENCE_END.search(line)
        if m:
            ends.append(float(m.group(1)))

    chunks = []
    cursor = 0.0
    for i, s_start in enumerate(starts):
        if s_start - cursor > 0.5:
            chunks.append((cursor, s_start))
        cursor = ends[i] if i < len(ends) else duration
    if duration - cursor > 0.5:
        chunks.append((cursor, duration))
    return chunks


def pick_segments(chunks, min_s, max_s, target_s, max_n):
    """Choose up to max_n non-overlapping runs of chunks, each within
    [min_s, max_s], preferring durations near target_s."""
    candidates = []
    for i in range(len(chunks)):
        single = chunks[i][1] - chunks[i][0]
        if single > max_s:
            # One unbroken stretch longer than a Short — trim a window.
            candidates.append((chunks[i][0], chunks[i][0] + target_s))
            continue
        for j in range(i, len(chunks)):
            span = chunks[j][1] - chunks[i][0]
            if span > max_s:
                break
            if span >= min_s:
                candidates.append((chunks[i][0], chunks[j][1]))

    candidates.sort(key=lambda c: abs((c[1] - c[0]) - target_s))
    chosen = []
    for cand in candidates:
        if len(chosen) >= max_n:
            break
        if all(cand[1] <= s or cand[0] >= e for s, e in chosen):
            chosen.append(cand)
    return sorted(chosen)


def _parse_ts(text):
    parts = text.strip().split(":")
    seconds = 0.0
    for part in parts:
        seconds = seconds * 60 + float(part)
    return seconds


def load_highlights(video_path):
    """Optional manual override: '<video>.highlights' with 'start-end' lines."""
    sidecar = video_path + ".highlights"
    if not os.path.exists(sidecar):
        return None
    segments = []
    with open(sidecar) as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            start_text, end_text = line.split("-", 1)
            segments.append((_parse_ts(start_text), _parse_ts(end_text)))
    return segments or None


def find_segments(video_path, seg_cfg):
    manual = load_highlights(video_path)
    if manual is not None:
        return manual, "manual"
    duration = probe_duration(video_path)
    chunks = detect_speech_chunks(
        video_path, seg_cfg["silence_db"], seg_cfg["silence_min_seconds"], duration)
    pad = seg_cfg["pad_seconds"]
    segments = pick_segments(
        chunks, seg_cfg["min_seconds"], seg_cfg["max_seconds"],
        seg_cfg["target_seconds"], seg_cfg["max_shorts_per_video"])
    padded = [(max(0.0, s - pad), min(duration, e + pad)) for s, e in segments]
    return padded, "auto"
