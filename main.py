"""***********************************************************************"""
"""*** The GUI source code for changing messages (response text) on Garmin ***"""
"""***********************************************************************"""

"""Original messages are:"""
"""OK."""
"""ANO"""
"""NE"""
"""Jezdím."""
"""Brzy budu doma."""
"""Teď nemůžu mluvit."""
"""Teď nemůžu."""
"""Se zpožděním."""
"""Téměř u cíle."""
"""Jste v polovině."""

# First column are original texts, second column are replaced texts
change_list = [
    ['OK.', 'OK'],  # ...it can be not safety, because it can be many times inside the file.
    ['Jezdím.', 'Jsem na kole. Ozvu se později.'],
    ['Teď nemůžu mluvit.', 'Teď nemůžu mluvit. Ozvu se.'],
    ['Teď nemůžu.', 'Za chvíli jsem tam!'],
    ['Se zpožděním.', 'Budu mít zpoždění.'],
    ['Téměř u cíle.', 'Dorazím za 20 minut.'],
    ['Jste v polovině.', 'Dorazím za 30 minut.'],
    ['Odesláno z mého zařízení Garmin', 'Odesláno ze zařízení Garmin']
]

# List of texts what don't have to be 2 times in the language file
exception_list = \
    ['Odesláno z mého zařízení Garmin']

file_name = 'Czech.gtt'

from PyQt5 import QtWidgets
import gui.Main_win

"""
def replace_lang(text: str):
    for i in range(len(change_list)):
        orig_item = change_list[i][0]
        replace_item = change_list[i][1]
        count = text.count(orig_item)

        if count != 2:
            if not (orig_item in exception_list) or count != 1:
                raise ValueError("ERROR: Can not be find text - " + str(i+1) + ". " + orig_item)
        text = text.replace(orig_item, replace_item)
    return text


def read_file(f_name: str):
    with open(f_name, mode='r', encoding='utf-8', newline='') as file:
        return file.read()


def write_file(f_name: str, text: str):
    # Check if the last char is ENTER. Then it should remove it, because the same rows count like before
    last_char = text[len(text) - 1:len(text)]
    if last_char == '\n':
        text = text[0:len(text) - 1]
    # Start writing the file
    with open(f_name, mode='w', encoding='utf-8', newline='') as file:
        print(text, file=file)

def myCons():
    try:
        print("#### GARMIN LANGUAGE REPLACER 1.02 ####")
        print("**** START *****")

        print("Reading file ..... ")
        original_text = read_file(file_name)

        print("Replacing ..... ")
        replaced_text = replace_lang(original_text)

        print("Writing file ..... ")
        write_file("new_" + file_name, replaced_text)

        print("**** DONE *****")
    except ValueError as ExValErr:
        print(ExValErr)
    except FileNotFoundError as ExFileNotFound:
        print('ERROR: File not found - ', ExFileNotFound)
    except Exception as ExGlobal:
        print('ERROR: Undefined exception - ', ExGlobal)
    finally:
        input("Press enter to exit")
"""

# pyuic5 -o gui/Main_win.py gui/Main_win.ui
import sys
from PyQt5 import QtGui


def load_temp_files():
    base_path = ""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = sys.path[1]
    finally:
        icon_path = base_path + '\\files\\ico.ico'
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.setWindowIcon(icon)


app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
win = gui.Main_win.Ui_MainWindow()

win.setupUi(window)
win.retranslateUi(window)

win.psbStart.clicked.connect(load_temp_files)

window.show()
app.exec()
