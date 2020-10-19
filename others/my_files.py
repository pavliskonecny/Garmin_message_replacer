from os import path


def read_file(f_name: str) -> str:
    """
    read text file
    """
    with open(f_name, mode='r', encoding='utf-8', newline='') as file:
        return file.read()


def write_file(f_name: str, text: str):
    """
    write text file
    """
    with open(f_name, mode='w', encoding='utf-8', newline='') as file:
        print(text, file=file)


def exist_file(file_name: str) -> bool:
    """
    function will return bool of existing file
    """
    return path.isfile(file_name)


def get_abs_path(file_name: str) -> str:
    """
    function will return absolute path from relative file name
    """
    return path.abspath(file_name)


def get_file_name(file_path: str) -> str:
    """
    function will return file name from absolute path
    """
    return path.basename(file_path)
