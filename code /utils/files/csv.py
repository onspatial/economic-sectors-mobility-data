import pandas


def get_number_of_rows(file_path):
    data = pandas.read_csv(file_path)
    number_of_rows = len(data)
    return number_of_rows
