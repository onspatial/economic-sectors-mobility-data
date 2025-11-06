import utils.files.basics as file_basics
import utils.files.bash as bash_utils
import os
import time


def exists(path, is_dir=False):
    try:
        if not path:
            return False
        if path == "":
            return False
        if not isinstance(path, str):
            return False

        if is_dir:
            return os.path.isdir(path)
        else:
            return os.path.exists(path)

    except Exception as e:
        print(f"ERROR: {path} does not exist and the following error occurred: {e}")
        return False


def is_safe(path, new=False, is_dir=False):
    try:
        if new:
            if exists(path, is_dir):
                file_basics.remove(path, is_dir, trash=False)
            file_basics.create(path, is_dir)
            return True
        else:
            file_basics.create(path, is_dir)
            return True
    except Exception as e:
        print(f"ERROR: {path} is not safe and the following error occurred: {e}")
        return False


def wait_until_file_exists(file_path, time_out=10, command_to_run="", verbose=False):
    # time.sleep(time_out)
    sleep_time = time_out
    while not exists(file_path):
        time.sleep(sleep_time)
        bash_utils.run_command(command_to_run)
        sleep_time *= 2
        if verbose:
            print(f"Waiting for {file_path} to be written to disk...{sleep_time} seconds", end="\r")
