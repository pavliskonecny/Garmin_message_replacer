from os import path, curdir


def read_file(f_name: str):
    with open(f_name, mode='r', encoding='utf-8', newline='') as file:
        return file.read()

def write_file(f_name: str, text: str):
    with open(f_name, mode='w', encoding='utf-8', newline='') as file:
        print(text, file=file)

def exist_file(file_name: str) -> bool:
    return path.isfile(file_name)

def get_abs_path(file_name: str) -> str:
    return path.abspath(file_name)

def get_file_name(file_path: str) -> str:
    return path.basename(file_path)