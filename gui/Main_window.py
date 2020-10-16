# pyuic5 -o gui/Ui_MainWindow.py gui/Ui_MainWindow.ui

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from gui.Ui_MainWindow import Ui_MainWindow
import sys

import others.my_files as my_files
from others.my_time import My_time
import garmin_data


class Main_window(QMainWindow):

    def __init__(self):
        super(Main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self._time_stamp = My_time(4)
        self._load_temp_files()
        self._init_path_file()

        self.ui.psbStart.clicked.connect(self.btnStart_onClick)
        self.ui.psbBrowse.clicked.connect(self.btnBrowse_onClick)

    def _load_temp_files(self):
        base_path = ""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = sys.path[1]
        finally:
            icon_path = base_path + '\\files\\ico.ico'
            self.setWindowIcon(QIcon(icon_path))

    def _init_path_file(self):
        if my_files.exist_file(garmin_data.file_name):
            self.ui.lnePath.setText(my_files.get_abs_path(garmin_data.file_name))

    def btnBrowse_onClick(self):
        # file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Garmin Lang Files (*.gtt);;All Files (*)")
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Garmin Lang Files (*.gtt)")
        if file_name:
            self.ui.lnePath.setText(file_name)

    def btnStart_onClick(self):
        try:
            self._add_text("**** START *****")
            self._add_text("Reading file ..... ")

            file_name = self.ui.lnePath.text()
            original_text = my_files.read_file(file_name)

            self._add_text("Replacing ..... ")
            replaced_text = self._replace_lang(original_text)

            self._add_text("Writing file ..... ")

            if not self._write_file(replaced_text):
                self._add_text("**** FILE WAS NOT SAVED *****")
            else:
                self._add_text("**** DONE *****")
        except ValueError as ExValErr:
            QMessageBox.critical(self, "Text position error", str(ExValErr))
        except FileNotFoundError as ExFileNotFound:
            QMessageBox.information(self, "File doesn't exist",
                                    "Please, as first select Garmin Language file\n" + str(ExFileNotFound))
        except Exception as ExGlobal:
            QMessageBox.critical(self, "Unexpected error",
                                 "Please, as first select Garmin Language file\n" + str(ExGlobal))
    def _write_file(self, text: str) -> bool:
        file_name, _ = QFileDialog.getSaveFileName(self, "Save new File as", "", "Garmin Lang Files (*.gtt)")
        if file_name:
            my_files.write_file(file_name, text)
            return True
        else:
            return False

    def _add_text(self, new_text: str):
        text = self.ui.txeState.toPlainText()
        if text:
            text += "\n"
        text += self._time_stamp.get_time_stamp() + new_text
        self.ui.txeState.setText(text)

    def _replace_lang(self, text: str):
        for i in range(len(garmin_data.change_list)):
            orig_item = garmin_data.change_list[i][0]
            replace_item = garmin_data.change_list[i][1]
            count = text.count(orig_item)

            if count != 2:
                if not (orig_item in garmin_data.exception_list) or count != 1:
                    raise ValueError("Can not be find text - " + str(i + 1) + ". " + orig_item)
            text = text.replace(orig_item, replace_item)

        # Check if the last char is ENTER. If that you should remove it,
        # because the row count must be the same like before
        last_char = text[len(text) - 1:len(text)]
        if last_char == '\n':
            text = text[0:len(text) - 1]

        return text


        """
        res = qm.question(self, 'Title', "Are you sure to reset all the values?", qm.Yes | qm.No)
        print(type(res))

        if res == QMessageBox.Yes:
            print("yes")
        else:
            qm.information(self, '', "Nothing Changed", qm.Ok)

        val = self.ui.prbProgbar.value()
        val += 10
        if val > 100:
            val = 100
        self.ui.prbProgbar.setValue(val)
        """
