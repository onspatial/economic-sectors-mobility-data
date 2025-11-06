import utils.files.check as check_utils


def save_text(dict, file):
    check_utils.is_safe(file, new=True, is_dir=False)
    with open(file, "w") as f:
        for key in dict:
            f.write(f"{key} = {dict[key]}\n")
