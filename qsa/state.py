"""JSON ledger of processed sources and rendered/uploaded shorts."""
import json
import os


def load_state(state_file):
    if os.path.exists(state_file):
        with open(state_file) as fh:
            return json.load(fh)
    return {"sources": {}, "shorts": []}


def save_state(state_file, state):
    os.makedirs(os.path.dirname(state_file), exist_ok=True)
    tmp = state_file + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(state, fh, indent=2)
    os.replace(tmp, state_file)


def pending_uploads(state):
    return [s for s in state["shorts"] if not s.get("uploaded")]
