from PyQt5 import QtWidgets, QtGui
from gui.Ui_MainWindow import Ui_MainWindow
import sys

class Main_window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self._load_temp_files()

        self.ui.psbStart.clicked.connect(self.btnStartOnClick)

    def _load_temp_files(self):
        base_path = ""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = sys.path[1]
        finally:
            icon_path = base_path + '\\files\\ico.ico'
            self.setWindowIcon(QtGui.QIcon(icon_path))

    def btnStartOnClick(self):
        val = self.ui.prbProgbar.value()
        val += 10
        if val > 100:
            val=100
        self.ui.prbProgbar.setValue(val)
