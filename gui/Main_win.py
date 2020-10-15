# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 280)
        MainWindow.setMinimumSize(QtCore.QSize(500, 280))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui\\../files/garmin.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblHint = QtWidgets.QLabel(self.centralwidget)
        self.lblHint.setMinimumSize(QtCore.QSize(0, 30))
        self.lblHint.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblHint.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHint.setObjectName("lblHint")
        self.verticalLayout.addWidget(self.lblHint)
        self.frmMain = QtWidgets.QFrame(self.centralwidget)
        self.frmMain.setMinimumSize(QtCore.QSize(0, 200))
        self.frmMain.setStyleSheet("")
        self.frmMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmMain.setObjectName("frmMain")
        self.gridLayout = QtWidgets.QGridLayout(self.frmMain)
        self.gridLayout.setObjectName("gridLayout")
        self.txeState = QtWidgets.QTextEdit(self.frmMain)
        self.txeState.setStyleSheet("")
        self.txeState.setReadOnly(True)
        self.txeState.setObjectName("txeState")
        self.gridLayout.addWidget(self.txeState, 7, 2, 1, 1)
        self.lnePath = QtWidgets.QLineEdit(self.frmMain)
        self.lnePath.setEnabled(True)
        self.lnePath.setReadOnly(True)
        self.lnePath.setObjectName("lnePath")
        self.gridLayout.addWidget(self.lnePath, 4, 2, 1, 1)
        self.psbBrowse = QtWidgets.QPushButton(self.frmMain)
        self.psbBrowse.setObjectName("psbBrowse")
        self.gridLayout.addWidget(self.psbBrowse, 4, 0, 1, 1)
        self.chckOverwrite = QtWidgets.QCheckBox(self.frmMain)
        self.chckOverwrite.setToolTip("")
        self.chckOverwrite.setWhatsThis("")
        self.chckOverwrite.setShortcut("")
        self.chckOverwrite.setTristate(False)
        self.chckOverwrite.setObjectName("chckOverwrite")
        self.gridLayout.addWidget(self.chckOverwrite, 5, 0, 1, 1)
        self.psbStart = QtWidgets.QPushButton(self.frmMain)
        self.psbStart.setStyleSheet("background-color: rgb(0, 124, 195);\n"
"color: rgb(225, 225, 225);")
        self.psbStart.setObjectName("psbStart")
        self.gridLayout.addWidget(self.psbStart, 7, 0, 1, 1)
        self.verticalLayout.addWidget(self.frmMain)
        self.prbProgbar = QtWidgets.QProgressBar(self.centralwidget)
        self.prbProgbar.setStyleSheet("color: rgb(0, 124, 195);\n"
"")
        self.prbProgbar.setProperty("value", 24)
        self.prbProgbar.setObjectName("prbProgbar")
        self.verticalLayout.addWidget(self.prbProgbar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Garmin Language message replacer"))
        self.lblHint.setText(_translate("MainWindow", "Please, select desired language file for conversion:        "))
        self.psbBrowse.setText(_translate("MainWindow", "Browse"))
        self.chckOverwrite.setText(_translate("MainWindow", "Overwrite\n"
"language file?"))
        self.psbStart.setText(_translate("MainWindow", "START\n"
"Conversion"))
