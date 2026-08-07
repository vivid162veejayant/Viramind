# profile.py

import json
import os

PROFILE_PATH = "data/profile.json"

def load_profile():
    if not os.path.exists(PROFILE_PATH):
        return {
            "name": None,
            "compile_attempts": 0,
            "syntax_errors": 0,
            "confidence": 100,
            "chaos": 0
        }

    with open(PROFILE_PATH, "r") as f:
        return json.load(f)


def save_profile(profile):
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f, indent=4)