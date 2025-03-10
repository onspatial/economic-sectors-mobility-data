
import utils.files.path as path_utils
import utils.files.basics as basics_utils
import utils.files.check as check_utils
import os
   
def zip(input_path, is_dir=False, verbose=False):
    if is_dir:
        return zip_dir(input_path,verbose)
    return zip_file(input_path, verbose)


def zip_file(input_file_path, verbose=False):
    input_file_path = path_utils.get_absolute_path(input_file_path)
    if not check_utils.exists(input_file_path):
        print(f"{input_file_path} does not exist...")
        return None
    if input_file_path.endswith(".zip"):
        print(f"{input_file_path} is already a zip file...")
        return input_file_path
    if verbose:
        print(f'Zipping {input_file_path}')
    os.system(f"cd {path_utils.get_parent_folder(input_file_path,path=True)} && zip -r {path_utils.get_file_name(input_file_path).split('.')[0]}.zip {path_utils.get_file_name(input_file_path)}")
    return f"{path_utils.get_parent_folder(input_file_path,path=True)}/{path_utils.get_file_name(input_file_path)}.zip"

def zip_dir(output_dir, verbose=False):
    dir_name = os.path.basename(output_dir)
    files = basics_utils.get_files(output_dir)
    if verbose:
        print(f'Zipping {files} to {dir_name}.zip')
    os.system(f'cd {output_dir} && zip -r {dir_name}.zip {' '.join(files)}')
    return f'{output_dir}/{dir_name}.zip'

# def unzip_file(file):
#     file = get_absolute_path(file)
#     if not exists(file):
#         print(f"{file} does not exist...")
#         return
#     if file.endswith(".zip"):
        
#         os.system(f"unzip {file} -d {get_file_path(file)}/tmp")
#         # th eonly file in tmp folder
#         temp_name = get_file_list(f"{get_file_path(file)}/tmp")[0]
#         return temp_name
#     else:
#         print(f"{file} is not a zip file...")
#         return file
    


# def unzip(src,des, quiet=True, log=f'logs/unzip.{sync_utils.get_timestamp(8)}.log', verbose=False):
#     src = file_path.get_absolute_path(src)
#     des = file_path.get_absolute_path(des)

#     file_check.is_safe(des,new=True,is_dir=True)
#     if verbose:
#         print(f'Unzipping {src} to {des}')
#     if quiet and file_check.is_safe(log):        
#         os.system(f'unzip {src} -d {des} >> {log}')
#     else:
#         os.system(f'unzip -q {src} -d {des}')
#     return des
