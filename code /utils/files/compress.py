
import utils.files.zip as zip_utils
import utils.files.gz as gz_utils
import utils.files.basics as basics_utils
import utils.files.check as check_utils
import pandas
import os

def get_extracted_file_path(input_file_path, output_file_path=None, remove_extracted=False,  verbose=False):
    csv_file_path = input_file_path
    try:
        if verbose:
            print(f"Extracting {input_file_path}")
        if input_file_path.endswith(".zip"):
            csv_file_path =  zip_utils.unzip(input_file_path, output_file_path, verbose=verbose)
        elif input_file_path.endswith(".gz"):
            csv_file_path =  gz_utils.ungz(input_file_path, output_file_path, verbose=verbose)
        if remove_extracted:
            basics_utils.remove_file(input_file_path)
        return csv_file_path
    except Exception as e:
        print(f"Error in input_file_path: {input_file_path}")
        os.system(f"echo {input_file_path} >> error.txt")
        basics_utils.remove_file(input_file_path)
        print(e)

def get_df_from_file(input_file_path, output_file_path='temp.csv',  remove_extracted=False, verbose=True):
    if not check_utils.exists(input_file_path):
        print(f"File does not exist: {input_file_path}")
        return None
    extracted_path = get_extracted_file_path(input_file_path, output_file_path=output_file_path,verbose=verbose)
    if extracted_path is None:
        return None
    df = pandas.read_csv(extracted_path, low_memory=False)
    if remove_extracted:
        basics_utils.remove_file(extracted_path)
    return df

def compress(input_path, extension="zip", is_dir=False, verbose=False):
    if extension == "zip":
        return zip(input_path,is_dir,verbose)
    elif extension == "gz":
        return gz(input_path,is_dir,verbose)
    
def decompress(input_path, extension="zip", is_dir=False, verbose=False):
    if extension == "zip":
        return zip_utils.unzip(input_path,is_dir,verbose)
    elif extension == "gz":
        return gz_utils.ungz(input_path,is_dir,verbose)
 
def zip(input_path, is_dir=False, verbose=False):
    return zip_utils.zip(input_path,is_dir, verbose=verbose)

def gz(input_path, is_dir=False, verbose=False):
    return gz_utils.gz(input_path,is_dir, verbose=verbose)

def unzip(input_path, is_dir=False, verbose=False):
    return zip_utils.unzip(input_path,is_dir, verbose=verbose)

def ungz(input_path, is_dir=False, verbose=False):
    return gz_utils.ungz(input_path,is_dir, verbose=verbose)