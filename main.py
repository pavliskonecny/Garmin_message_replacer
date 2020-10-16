"""***********************************************************************"""
"""*** The source code for changing messages (response text) on Garmin ***"""
"""***********************************************************************"""

from PyQt5 import QtWidgets
from gui.Main_window import Main_window
import sys


app = QtWidgets.QApplication([])
window = Main_window()
sys.exit(app.exec())