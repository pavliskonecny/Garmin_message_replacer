"""
to convert from qt designer *.ui file to python *.py file use command:
pyuic5 --from-imports -o gui/Ui_MainWindow.py gui/Ui_MainWindow.ui

to convert resources file *.qrc to python *.py file use command:
pyrcc5 gui/resources.qrc -o gui/resources_rc.py
"""

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
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
        self._init()

        self.ui.psbStart.clicked.connect(self.btnStart_onClick)
        self.ui.psbBrowse.clicked.connect(self.btnBrowse_onClick)
        self.ui.psbAbout.clicked.connect(self.actAbout_onClick)

    def _init(self):
        lang_file_path = garmin_data.get_lang_file_name()
        if my_files.exist_file(lang_file_path):
            self.ui.lnePath.setText(lang_file_path)

        if not garmin_data.json_exist():
            self._add_output("ERROR - JSON file doesn't exist")
            QMessageBox.critical(self, "JSON file error: ", "JSON file " + garmin_data.JSON_FILE_NAME + " doesn't exist!")
            self.ui.psbStart.setEnabled(False)
            self.ui.psbBrowse.setEnabled(False)

    def actAbout_onClick(self):
        QMessageBox.about(self, "About", "Created by:\n" "Pavel Konečný\n" "Czech Republic\n" "2020")

    def btnBrowse_onClick(self):
        file_name_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Garmin Lang Files (*.gtt)")
        if file_name_path:
            self.ui.lnePath.setText(file_name_path)

    def btnStart_onClick(self):
        try:
            self._add_output("**** START *****")

            self._add_output("Reading file ..... ")
            source_file_path = self.ui.lnePath.text()
            source_text = my_files.read_file(source_file_path)

            self._add_output("Replacing messages ..... ")
            target_text = garmin_data.replace(source_text)

            if self.ui.chcbBackup.isChecked():
                self._add_output("Creating backup ..... ")
                backup_dir = "backup"
                today = My_Time.today()
                source_file_path = self.ui.lnePath.text()
                file_name = my_files.get_file_name(source_file_path)
                my_files.make_dir(backup_dir)
                my_files.make_dir(f"{backup_dir}\\{today}")
                my_files.copy_file(source_file_path, f"{backup_dir}\\{today}\\{file_name}")

            self._add_output("Writing file ..... ")
            if self.ui.chcbOverwrite.isChecked():
                target_file_path = self.ui.lnePath.text()
            else:
                target_file_path = self._get_save_file_path()
            if not target_file_path:
                self._add_output("**** FILE SAVING INTERRUPT BY USER *****")
            else:
                my_files.write_file(target_file_path, target_text)
                self._add_output("**** DONE *****")
        except ValueError as ExValErr:
            self._add_output("ERROR")
            QMessageBox.critical(self, "TAG error: ", str(ExValErr))
        except FileNotFoundError as ExFileNotFound:
            self._add_output("ERROR")
            QMessageBox.information(self, "File doesn't exist",
                                    "Please, as first select Garmin Language file\n" + str(ExFileNotFound))
        except SyntaxError as ExSynEee:
            self._add_output("ERROR")
            QMessageBox.critical(self, "Syntax error: ", str(ExSynEee))
        except Exception as ExGlobal:
            self._add_output("ERROR")
            QMessageBox.critical(self, "Unexpected error", "Unexpected error: " + str(ExGlobal))

    def _get_save_file_path(self):
        source_file_path = self.ui.lnePath.text()
        #propose_dir_name = my_files.get_dir(source_file_name)
        #propose_file_name = "new_" + my_files.get_file_name(source_file_name)
        #propose_path = propose_dir_name + "\\" + propose_file_name
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File as", source_file_path, "Garmin Lang Files (*.gtt)")
        return file_name

    def _add_output(self, new_text: str):
        text = self.ui.txeOutput.toPlainText()
        if text:
            text += "\n"
        text += self._time_stamp.get_time_stamp() + new_text
        self.ui.txeOutput.setText(text)
