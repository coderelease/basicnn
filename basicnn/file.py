import os


def ensure_dirs(file_path, file_has_suffix=True):
    if file_has_suffix and "." in os.path.basename(file_path):
        directory = os.path.dirname(file_path)
    else:
        directory = file_path

    if not os.path.exists(directory):
        os.makedirs(directory)

    return file_path


def home_path():
    return os.path.expanduser('~')


def join(*args):
    return os.path.join(*args)


def dirname_and_basename(file_path):
    return os.path.dirname(file_path), os.path.basename(file_path)
