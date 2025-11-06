import utils.files.check as check_utils
import utils.files.path as path_utils
import utils.files.bash as bash_utils


def get_downloaded_file_path(file_name, url="", output_dir="data/downloaded", time_out=2, verbose=False):
    file_path = f"{output_dir}/{file_name}"
    file_path = path_utils.get_absolute_path(file_path)
    if verbose:
        print(f"Downloading {url} to {file_path}")
    if check_utils.exists(file_path):
        if verbose:
            print(f"File {file_path} already exists")
        return file_path
    if url != "":
        print(f"Downloading {file_name} from {url}")
        check_utils.is_safe(file_path, new=False, is_dir=False)
        download_command = f"wget -O {file_path} {url} && wait"
        bash_utils.run_command(download_command)
        check_utils.wait_until_file_exists(file_path, time_out=time_out, command_to_run=download_command, verbose=verbose)
        return file_path
    else:
        return None


def download_all_files(file_list_df, download_storage=None, verbose=False):
    if download_storage is None:
        return None
    all_file_paths = []
    for row in file_list_df.iterrows():
        file_info = row[1]
        file_name = file_info["file_name"]
        download_link = file_info["download_link"]
        downloaded_path = get_downloaded_file_path(file_name, download_link, output_dir=download_storage, verbose=verbose)
        all_file_paths.append(downloaded_path)
    return all_file_paths
