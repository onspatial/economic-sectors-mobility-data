import json
import utils.files.check as check_utils


def get_json(file):
    with open(file, "r") as f:
        return json.load(f)


def save_json(data, file):
    check_utils.is_safe(file, new=True, is_dir=False)
    with open(file, "w") as f:
        json.dump(data, f)
