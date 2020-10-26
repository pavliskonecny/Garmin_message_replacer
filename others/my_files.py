import os
import sys
import json


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
    function return bool of existing file
    """
    return os.path.isfile(file_name)


def get_abs_path(file_name: str) -> str:
    """
    function return absolute path from relative file name
    """
    return os.path.abspath(file_name)


def get_file_name(file_path: str) -> str:
    """
    function return file name from absolute file path
    """
    return os.path.basename(file_path)


def get_project_dir_path() -> str:
    """
    function return absolute project folder path
    """
    # res = str(os.path.abspath(os.curdir))  #by this you will get current FILE folder, not PROJECT folder
    # res = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #by this you will get path without last folder
    return str(sys.path[1])

def get_cur_dir() -> str:
    """
    function return absolute current directory path
    """
    return os.curdir


#def get_temp_project_folder_path() -> str:
    """
    function return temp absolute project folder path
    """
#    return str(sys._MEIPASS)


def _write_json(json_file_name: str, data: object):
    j_data = json.dumps(data, ensure_ascii=False, indent=2)
    write_file(json_file_name, j_data)


def _read_json(json_file_name: str) -> str:
    j_data = json.loads(read_file(json_file_name))
    return j_data

def get_files_with_extension(extension: str) -> list:
    if not extension.startswith("."):
        extension = "." + extension

    files = []
    for file in os.listdir(get_cur_dir()):
        if file.endswith(extension):
            files.append(file)

    return files