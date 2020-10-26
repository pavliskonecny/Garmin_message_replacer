import os
import sys

# ******************************************************
# CHANGE THIS PARAMETERS AS NEEDED
py_file_name = 'main.py'

add_exe_file_name = True    # False will make exe file name the same like project name folder
exe_file_name = "Garmin Lang Replacer"

add_icon = True             # Add exe file icon
ico_name = "images\\ico.ico"

add_folder = False           # Include folder to exe file
add_folder_name = "files"

gui_app = True              # False will take console app, True will take GUI app

one_file = True             # True means one exe file. False means folder with necessary files and exe file

# ******************************************************


def make_build():
    project_name = get_project_name()
    project_folder = get_project_folder()

    cmd = "pyinstaller --noconfirm --log-level=WARN --clean"

    if one_file:
        cmd += " --onefile"

    if gui_app:
        cmd += " --noconsole"

    if add_folder:
        cmd += " --add-data " + project_folder + "\\" + add_folder_name + ";" + add_folder_name

    cmd += " " + project_folder + "\\" + py_file_name
    cmd += " --name " + project_name
    cmd += " --specpath " + project_folder + "\\build\\"    # for spec file
    cmd += " --workpath " + project_folder + "\\build\\"    # for build file
    cmd += " --distpath " + project_folder + "\\dist\\"     # for distribution exe file

    if add_icon:
        cmd += " --icon " + project_folder + "\\" + ico_name  # --icon MyIcon.ico

    print(cmd)
    os.system('cmd /c "' + cmd + '"')  # execute cmd


def get_project_name():
    if add_exe_file_name:
        return "\"" + exe_file_name + "\""  # "" are here because of possible spaces in the exe file name
    else:
        return os.path.basename(get_project_folder())  # get project name


def get_project_folder():
    # res = str(os.path.abspath(os.curdir))  #by this you will get current FILE folder, not PROJECT folder
    # res = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #by this you will get path without last folder
    res = sys.path[1]
    return res


def open_folder():
    dist_path = get_project_folder() + "\\dist\\"
    cmd = "explorer " + dist_path  # explorer C:/Users/konepa1/PycharmProjects/test/dist

    os.system('cmd /c "' + cmd + '"')  # execute cmd


# ******* START *********
print("Start building ...")
make_build()
print("Build is DONE")
open_folder()
