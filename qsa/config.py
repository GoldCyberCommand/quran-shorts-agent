"""Config loading for quran-shorts-agent. Stdlib only."""
import copy
import json
import os

DEFAULTS = {
    "source_dirs": [
        "~/Videos/quran-sources",
    ],
    "queue_dir": "queue",
    "state_file": "state/state.json",
    "segment": {
        "min_seconds": 20,
        "max_seconds": 58,
        "target_seconds": 40,
        "max_shorts_per_video": 3,
        "silence_db": "auto",
        "silence_min_seconds": 0.5,
        "pad_seconds": 0.3,
    },
    "video": {
        "width": 1080,
        "height": 1920,
        "background": "black",  # "black" (pad) or "blur"
    },
    "upload": {
        "privacy_status": "public",
        "category_id": "27",  # Education
        "max_uploads_per_run": 1,
        "tags": ["Quran", "Recitation", "Tilawah", "Shorts"],
        "title_template": "{surah} — Part {n} | Beautiful Quran Recitation #Shorts",
        "description_template": (
            "Recitation of {surah} (part {n}), with word-by-word tajweed text.\n\n"
            "#Quran #Recitation #Shorts"
        ),
    },
}


def project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _merge(base, override):
    out = copy.deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _merge(out[key], value)
        else:
            out[key] = value
    return out


def load_config():
    root = project_root()
    path = os.path.join(root, "config.json")
    cfg = copy.deepcopy(DEFAULTS)
    if os.path.exists(path):
        with open(path) as fh:
            cfg = _merge(cfg, json.load(fh))
    cfg["source_dirs"] = [os.path.expanduser(d) for d in cfg["source_dirs"]]
    for key in ("queue_dir", "state_file"):
        value = os.path.expanduser(cfg[key])
        if not os.path.isabs(value):
            value = os.path.join(root, value)
        cfg[key] = value
    return cfg
