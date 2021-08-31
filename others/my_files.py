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


def copy_file(source_path: str, destination_path: str):
    # destination folders have to exist as first!!!
    from shutil import copyfile
    copyfile(source_path, destination_path)


def copy_dir(source_dir: str, destination_dir: str, rewrite: bool = True):
    from shutil import copytree, rmtree
    if rewrite:
        if exist_dir(destination_dir):
            rmtree(destination_dir)
    copytree(source_dir, destination_dir)

def exist_file(file_name: str) -> bool:
    """
    function return bool of existing file
    """
    return os.path.isfile(file_name)

def exist_dir(directory_name: str) -> bool:
    """
    function return bool of existing directory
    """
    return os.path.isdir(directory_name)

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


def get_dir(file_path: str) -> str:
    """
    function return absolute current directory path
    """
    return os.path.dirname(file_path)


def get_cur_dir() -> str:
    """
    function return absolute current directory path
    """
    return os.curdir

    # def get_temp_project_folder_path() -> str:
    # """
    # function return temp absolute project folder path
    # """
    # return str(sys._MEIPASS)

def make_dir(directory_name: str) -> bool:
    """
    function create directory if it doesn't exist
    """
    if not exist_dir(directory_name):
        os.mkdir(directory_name)
        return True
    return False


def _write_json(json_file_name: str, data: object):
    try:
        j_data = json.dumps(data, ensure_ascii=False, indent=2)
        write_file(json_file_name, j_data)
    except Exception as ex:
        raise SyntaxError("JSON writing error: " + str(ex))


def _read_json(json_file_name: str) -> str:
    try:
        j_data = json.loads(read_file(json_file_name))
        return j_data
    except Exception as ex:
        raise SyntaxError("JSON reading error: " + str(ex))


def get_files_with_extension(extension: str) -> list:
    if not extension.startswith("."):
        extension = "." + extension

    files = []
    for file in os.listdir(get_cur_dir()):
        if file.endswith(extension):
            files.append(file)

    return files


def get_drive_from_path(file_path: str) -> str:
    drive_tail = os.path.splitdrive(file_path)
    return drive_tail[0]    # Like - C:
    # return drive_tail[1]  # Like - \User\Documents\file.txt
