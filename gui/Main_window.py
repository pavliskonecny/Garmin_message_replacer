# pyuic5 -o gui/Ui_MainWindow.py gui/Ui_MainWindow.ui

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from gui.Ui_MainWindow import Ui_MainWindow

import others.my_files as my_files
from others.My_time import My_Time
import garmin_data


class Main_window(QMainWindow):

    def __init__(self):
        super(Main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self._time_stamp = My_Time(4)
        self._load_temp_files()
        self._init_path_file()

        self.ui.psbStart.clicked.connect(self.btnStart_onClick)
        self.ui.psbBrowse.clicked.connect(self.btnBrowse_onClick)

    def _load_temp_files(self):
        base_path = ""
        try:
            base_path = my_files.get_temp_project_folder_path()
        except Exception:
            base_path = my_files.get_project_folder_path()
        finally:
            icon_path = base_path + '\\files\\ico.ico'
            self.setWindowIcon(QIcon(icon_path))

    def _init_path_file(self):
        if my_files.exist_file(garmin_data.FILE_NAME):
            self.ui.lnePath.setText(my_files.get_abs_path(garmin_data.FILE_NAME))

    def btnBrowse_onClick(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Garmin Lang Files (*.gtt)")
        if file_name:
            self.ui.lnePath.setText(file_name)

    def btnStart_onClick(self):
        try:
            self._add_output("**** START *****")
            self._add_output("Reading file ..... ")

            source_file_name = self.ui.lnePath.text()
            source_text = my_files.read_file(source_file_name)

            self._add_output("Replacing ..... ")
            target_text = garmin_data.replace2(source_text)

            self._add_output("Writing file ..... ")
            target_file_name = self._get_save_file_name()
            if not target_file_name:
                self._add_output("**** FILE SAVING INTERRUPT BY USER *****")
            else:
                my_files.write_file(target_file_name, target_text)
                self._add_output("**** DONE *****")
        except ValueError as ExValErr:
            QMessageBox.critical(self, "Text position error: ", str(ExValErr))
        except FileNotFoundError as ExFileNotFound:
            QMessageBox.information(self, "File doesn't exist",
                                    "Please, as first select Garmin Language file\n" + str(ExFileNotFound))
        except Exception as ExGlobal:
            QMessageBox.critical(self, "Unexpected error", "Unexpected error: " + str(ExGlobal))

    def _get_save_file_name(self):
        propose_file_name = "new_" + my_files.get_file_name(self.ui.lnePath.text())
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File as", propose_file_name, "Garmin Lang Files (*.gtt)")
        return file_name

    def _add_output(self, new_text: str):
        text = self.ui.txeOutput.toPlainText()
        if text:
            text += "\n"
        text += self._time_stamp.get_time_stamp() + new_text
        self.ui.txeOutput.setText(text)
