def get_cleaned_lines(file, ignore_set=["", "#", "//"]):
    lines = get_lines(file)
    cleaned_lines = []
    for line in lines:
        if line.strip() in ignore_set:
            continue
        else:
            cleaned_lines.append(f"{line.strip()}")
    return cleaned_lines


def get_lines(file):
    with open(file, "r") as f:
        return f.readlines()


def save_lines_to_file(lines, file):
    with open(file, "w") as f:
        f.write("\n".join(lines))
