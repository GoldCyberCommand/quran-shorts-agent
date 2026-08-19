# quran-shorts-agent

Turn long Quran recitation videos into a steady stream of YouTube Shorts —
automatically.

The agent watches a folder for recitation videos, finds meaningful
segments by detecting the natural pauses between ayat, renders them as
vertical 1080x1920 Shorts with ffmpeg, and drip-uploads them to your
YouTube channel on a schedule (one per day by default). Point it at a
folder once, and every new video you drop in becomes Shorts on your
channel without you touching anything.

Pairs well with [QAAM](https://github.com/GoldCyberCommand/QAAM), which
turns recitation videos into clean black-background videos with
word-by-word tajweed-coloured mushaf text — this agent was built to feed
on QAAM's output, but works on any recitation video.

> **Please only re-publish recitations you own or have permission to use.**

If this saves you time, you can support the work:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-support%20this%20project-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/goldcybercommandlimited)

## How it picks "meaningful parts"

1. **Manual (best):** put a sidecar file next to any source video named
   `<video>.mp4.highlights`, one range per line (`mm:ss-mm:ss` or plain
   seconds; `#` comments allowed). Those exact cuts are used.
2. **Automatic:** recitation-pause detection (ffmpeg `silencedetect`).
   Pauses between ayat are natural cut points; the agent joins consecutive
   ayat into segments of 20–58 s (targeting ~40 s), up to 3 Shorts per
   video, and never cuts mid-recitation. All tunable in `config.json`.

Rendering: the video is scaled to width and letterboxed onto a black 9:16
canvas (ideal for black-background videos like QAAM's). Set
`video.background` to `"blur"` for a blurred-fill look on regular footage.
Audio gets a gentle fade-out.

## Requirements

- macOS or Linux, Python 3.9+
- [ffmpeg](https://ffmpeg.org/) (`brew install ffmpeg` / `apt install ffmpeg`)
- A Google account with a YouTube channel (upload step only)

## Install

Download the [latest release](https://github.com/GoldCyberCommand/quran-shorts-agent/releases)
or clone the repo, then:

```bash
pip3 install -r requirements.txt      # Google API libs (upload only)
cp config.example.json config.json    # then edit source_dirs etc.
```

Optionally `pip3 install .` to get a global `qsa` command instead of
`python3 -m qsa`.

## YouTube API setup (one-time)

1. In [Google Cloud Console](https://console.cloud.google.com/) create a
   project and enable **YouTube Data API v3**.
2. Configure the OAuth consent screen (External; add yourself as a test
   user), then create an OAuth client of type **Desktop app**.
3. Download the client JSON as `client_secret.json` into the project
   folder (gitignored — it never leaves your machine).
4. Run `python3 -m qsa auth` and sign in with the account that owns your
   channel. This writes `token.json` (also gitignored).

Quota: an upload costs 1,600 of the default 10,000 daily units, so the
default 1 upload/run never comes close to the limit.

## Usage

```bash
python3 -m qsa scan                 # preview: which videos, which cuts
python3 -m qsa process              # render new Shorts into queue/
python3 -m qsa upload --dry-run     # show exactly what would be uploaded
python3 -m qsa upload               # upload (max_uploads_per_run, default 1)
python3 -m qsa run                  # process + upload — the scheduled entrypoint
python3 -m qsa status               # ledger summary + recent upload URLs
```

`state/state.json` is the ledger: which sources were processed, which
Shorts exist, which are uploaded. A source is never cut twice and a Short
never uploaded twice, even across crashes. Delete a source's entry to
reprocess it.

## Fully automatic (scheduling)

**macOS** — installs a launchd job that runs `qsa run` daily at 17:00:

```bash
bash automation/install-schedule.sh
```

**Linux** — add a cron line (daily at 17:00):

```cron
0 17 * * * cd /path/to/quran-shorts-agent && /usr/bin/python3 -m qsa run >> logs/run.log 2>&1
```

Each run picks up new source videos, renders their Shorts, and uploads the
next queued Short. Change cadence via the schedule or
`upload.max_uploads_per_run`.

## Configuration (`config.json`)

| Key | Meaning |
|---|---|
| `source_dirs` | Folders scanned recursively for new videos |
| `segment.min/max/target_seconds` | Segment length bounds and sweet spot |
| `segment.max_shorts_per_video` | Cap per source video |
| `segment.silence_db` | `"auto"` (default: per-video adaptive threshold) or a fixed dB value |
| `segment.silence_min_seconds` | Minimum pause length (default 0.5 s) |
| `video.background` | `"black"` letterbox or `"blur"` fill |
| `upload.privacy_status` | `unlisted` (default — flip to `public` when happy) |
| `upload.title_template`, `description_template` | `{surah}`, `{n}` placeholders |

Surah names are parsed from `surah_<number>_<Name>.mp4` filenames (QAAM's
naming); anything else falls back to the filename.

## Support

Issues and PRs welcome. If this project is useful to you, consider
[buying me a coffee](https://buymeacoffee.com/goldcybercommandlimited) ☕

## License

[MIT](LICENSE) © 2026 Gold Cyber Command Limited
