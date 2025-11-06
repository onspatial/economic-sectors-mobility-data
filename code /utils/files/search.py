import utils.files.path as path_utils
import utils.files.basics as file_basics
import utils.string.match as string_match
import utils.files.check as file_check


def get_matching_files(folder_path, pattern, path=True, regex=True, verbose=False):
    if verbose:
        print(f"Looking for files matching {pattern} in {folder_path}")
    matched_files = []
    all_files = file_basics.get_files(folder_path)
    for file in all_files:
        if string_match.is_match(file, pattern, regex=regex):
            if path:
                matched_files.append(path_utils.join_path(folder_path, file))
            else:
                matched_files.append(file)

    return matched_files


def get_files(folders, file_name, path=True, verbose=False):
    print(f"Searching for {file_name} in {len(folders)} folders...")
    files = []
    for folder in folders:
        if verbose:
            print(f"Searching for {file_name} in {folder}")
        file_path = path_utils.join_path(folder, file_name)
        if file_check.exists(file_path):
            if path:
                files.append(file_path)
            else:
                files.append(file_name)
            files.append(file_path)
    return files
