import utils.files.check as check_utils
def append(text, file):
    with open(file, 'a') as f:
        f.write(text)
        f.write('\n')

def error(text, file='logs/error.log'):
    check_utils.is_safe(file)
    with open(file, 'a') as f:
        f.write(f'ERROR: {text}')
        f.write('\n')

def info(text, file='logs/info.log'):
    check_utils.is_safe(file)
    with open(file, 'a') as f:
        f.write(f'INFO: {text}')
        f.write('\n')

def warning(text, file='logs/warning.log'):
    check_utils.is_safe(file)
    with open(file, 'a') as f:
        f.write(f'WARNING: {text}')
        f.write('\n')