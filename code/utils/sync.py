
from datetime import datetime
def get_timestamp(digits=2):
    return datetime.now().strftime(f'%Y%m%d%H%M%S%f')[:digits]

# def get_timestamp_string():
#     return datetime.now().strftime('%Y-%m-%d %H:%M:%S')