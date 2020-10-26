# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 250)
        MainWindow.setMinimumSize(QtCore.QSize(500, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main ico/images/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frmMain = QtWidgets.QFrame(self.centralwidget)
        self.frmMain.setMinimumSize(QtCore.QSize(0, 200))
        self.frmMain.setStyleSheet("")
        self.frmMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmMain.setObjectName("frmMain")
        self.gridLayout = QtWidgets.QGridLayout(self.frmMain)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(9)
        self.gridLayout.setObjectName("gridLayout")
        self.lblLogo = QtWidgets.QLabel(self.frmMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLogo.sizePolicy().hasHeightForWidth())
        self.lblLogo.setSizePolicy(sizePolicy)
        self.lblLogo.setMaximumSize(QtCore.QSize(100, 27))
        self.lblLogo.setText("")
        self.lblLogo.setPixmap(QtGui.QPixmap(":/icons/images/garmin.png"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setIndent(1)
        self.lblLogo.setObjectName("lblLogo")
        self.gridLayout.addWidget(self.lblLogo, 0, 0, 1, 1)
        self.psbBrowse = QtWidgets.QPushButton(self.frmMain)
        self.psbBrowse.setObjectName("psbBrowse")
        self.gridLayout.addWidget(self.psbBrowse, 5, 0, 1, 1)
        self.txeOutput = QtWidgets.QTextEdit(self.frmMain)
        self.txeOutput.setStyleSheet("")
        self.txeOutput.setReadOnly(True)
        self.txeOutput.setObjectName("txeOutput")
        self.gridLayout.addWidget(self.txeOutput, 8, 1, 1, 1)
        self.lblHint = QtWidgets.QLabel(self.frmMain)
        self.lblHint.setMinimumSize(QtCore.QSize(0, 20))
        self.lblHint.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblHint.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lblHint.setObjectName("lblHint")
        self.gridLayout.addWidget(self.lblHint, 0, 1, 1, 1)
        self.lnePath = QtWidgets.QLineEdit(self.frmMain)
        self.lnePath.setEnabled(True)
        self.lnePath.setReadOnly(True)
        self.lnePath.setObjectName("lnePath")
        self.gridLayout.addWidget(self.lnePath, 5, 1, 1, 1)
        self.psbStart = QtWidgets.QPushButton(self.frmMain)
        self.psbStart.setMinimumSize(QtCore.QSize(90, 0))
        self.psbStart.setStyleSheet("background-color: rgb(0, 124, 195);\n"
"color: rgb(225, 225, 225);")
        self.psbStart.setObjectName("psbStart")
        self.gridLayout.addWidget(self.psbStart, 8, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(100, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frmMain)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Garmin Language message replacer"))
        self.psbBrowse.setText(_translate("MainWindow", "Browse"))
        self.lblHint.setText(_translate("MainWindow", "Please, select desired language file to replace messages:"))
        self.psbStart.setText(_translate("MainWindow", "START\n"
"Conversion"))
from . import resources_rc
