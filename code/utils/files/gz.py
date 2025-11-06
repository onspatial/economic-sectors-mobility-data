import utils.files.path as path_utils
import utils.files.basics as basics_utils
import utils.files.check as check_utils
import gzip as gzip_module
import os
import time


def gz(input_path, output_path=None, is_dir=False, verbose=False):
    if check_utils.exists(output_path):
        if verbose:
            print(f"{output_path} already exists...")
        return output_path
    if is_dir:
        return gz_dir(input_path, verbose)
    return gz_file(input_path, verbose)


def ungz(input_path, output_path=None, is_dir=False, verbose=False):
    if check_utils.exists(output_path):
        if verbose:
            print(f"{output_path} already exists...")
        return output_path
    if is_dir:
        ungz_path = ungz_dir(input_path, verbose)
    else:
        ungz_path = ungz_file(input_path, verbose)
    if output_path:
        return basics_utils.move(ungz_path, output_path)
    return ungz_path


def ungz_file(input_file_path, verbose=False):
    input_file_path = path_utils.get_absolute_path(input_file_path)
    if not check_utils.exists(input_file_path):
        if verbose:
            print(f"{input_file_path} does not exist...")
        return None
    if not input_file_path.endswith(".gz"):
        if verbose:
            print(f"{input_file_path} is not a gz file...")
        return input_file_path
    if verbose:
        print(f"Ungzipping {input_file_path}")
        # and make sure it flushed to disk
    with gzip_module.open(input_file_path, "rb") as f_in:
        with open(input_file_path[:-3], "wb") as f_out:
            f_out.writelines(f_in)
    check_utils.wait_until_file_exists(input_file_path[:-3], time_out=10)
    return input_file_path[:-3]


def ungz_dir(input_dir, verbose=False):
    if not input_dir.endswith(".gz"):
        if verbose:
            print(f"{input_dir} is not a gz file...")
        return input_dir
    if verbose:
        print(f"Ungzipping {input_dir}")
    with gzip_module.open(input_dir, "rb") as f_in:
        with open(input_dir[:-3], "wb") as f_out:
            f_out.writelines(f_in)
    return input_dir[:-3]


def gz_file(input_file_path, verbose=False):
    input_file_path = path_utils.get_absolute_path(input_file_path)
    if not check_utils.exists(input_file_path):
        if verbose:
            print(f"{input_file_path} does not exist...")
        return None
    if input_file_path.endswith(".gz"):
        if verbose:
            print(f"{input_file_path} is already a gz file...")
        return input_file_path
    if verbose:
        print(f"Gzipping {input_file_path}")
    with open(input_file_path, "rb") as f_in:
        with gzip_module.open(f"{input_file_path}.gz", "wb") as f_out:
            f_out.writelines(f_in)

    return f"{input_file_path}.gz"


def gz_dir(output_dir, verbose=False):
    dir_name = os.path.basename(output_dir)
    files = basics_utils.get_files(output_dir)
    if verbose:
        print(f"Gzipping {files} to {dir_name}.gz")
    with gzip_module.open(f"{output_dir}.gz", "wb") as f_out:
        for file in files:
            with open(file, "rb") as f_in:
                f_out.writelines(f_in)
    return f"{output_dir}.gz"
