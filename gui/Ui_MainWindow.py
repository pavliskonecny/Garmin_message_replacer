# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
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
        self.layMainWindow = QtWidgets.QHBoxLayout()
        self.layMainWindow.setObjectName("layMainWindow")
        self.layLeft = QtWidgets.QGridLayout()
        self.layLeft.setContentsMargins(-1, 0, 20, -1)
        self.layLeft.setObjectName("layLeft")
        self.psbAbout = QtWidgets.QToolButton(self.centralwidget)
        self.psbAbout.setEnabled(True)
        self.psbAbout.setMinimumSize(QtCore.QSize(100, 27))
        self.psbAbout.setMaximumSize(QtCore.QSize(100, 27))
        self.psbAbout.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.psbAbout.setFocusPolicy(QtCore.Qt.NoFocus)
        self.psbAbout.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.psbAbout.setAcceptDrops(False)
        self.psbAbout.setToolTip("")
        self.psbAbout.setStatusTip("")
        self.psbAbout.setWhatsThis("")
        self.psbAbout.setAccessibleName("")
        self.psbAbout.setAccessibleDescription("")
        self.psbAbout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.psbAbout.setAutoFillBackground(True)
        self.psbAbout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/garmin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.psbAbout.setIcon(icon1)
        self.psbAbout.setIconSize(QtCore.QSize(100, 27))
        self.psbAbout.setShortcut("")
        self.psbAbout.setAutoRepeat(False)
        self.psbAbout.setAutoExclusive(False)
        self.psbAbout.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.psbAbout.setAutoRaise(True)
        self.psbAbout.setArrowType(QtCore.Qt.NoArrow)
        self.psbAbout.setObjectName("psbAbout")
        self.layLeft.addWidget(self.psbAbout, 0, 1, 1, 1, QtCore.Qt.AlignTop)
        self.psbStart = QtWidgets.QPushButton(self.centralwidget)
        self.psbStart.setEnabled(True)
        self.psbStart.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.psbStart.setFont(font)
        self.psbStart.setAutoFillBackground(False)
        self.psbStart.setStyleSheet(":enabled {\n"
" color:  rgb(225, 225, 225);\n"
"background-color: rgb(0, 124, 195);\n"
"}\n"
"\n"
":disabled {\n"
" color:  rgb(120, 120, 120);\n"
" background-color: rgb(204, 204, 204);\n"
"}")
        self.psbStart.setAutoDefault(False)
        self.psbStart.setDefault(False)
        self.psbStart.setFlat(False)
        self.psbStart.setObjectName("psbStart")
        self.layLeft.addWidget(self.psbStart, 1, 1, 1, 1, QtCore.Qt.AlignTop)
        self.layMainWindow.addLayout(self.layLeft)
        self.layRight = QtWidgets.QVBoxLayout()
        self.layRight.setObjectName("layRight")
        self.lblHint = QtWidgets.QLabel(self.centralwidget)
        self.lblHint.setMinimumSize(QtCore.QSize(0, 20))
        self.lblHint.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblHint.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lblHint.setObjectName("lblHint")
        self.layRight.addWidget(self.lblHint)
        self.layBrowse = QtWidgets.QHBoxLayout()
        self.layBrowse.setObjectName("layBrowse")
        self.psbBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.psbBrowse.setEnabled(True)
        self.psbBrowse.setObjectName("psbBrowse")
        self.layBrowse.addWidget(self.psbBrowse)
        self.lnePath = QtWidgets.QLineEdit(self.centralwidget)
        self.lnePath.setEnabled(True)
        self.lnePath.setReadOnly(True)
        self.lnePath.setObjectName("lnePath")
        self.layBrowse.addWidget(self.lnePath)
        self.layRight.addLayout(self.layBrowse)
        self.chcbOverwrite = QtWidgets.QCheckBox(self.centralwidget)
        self.chcbOverwrite.setChecked(True)
        self.chcbOverwrite.setObjectName("chcbOverwrite")
        self.layRight.addWidget(self.chcbOverwrite)
        self.chcbBackup = QtWidgets.QCheckBox(self.centralwidget)
        self.chcbBackup.setChecked(True)
        self.chcbBackup.setObjectName("chcbBackup")
        self.layRight.addWidget(self.chcbBackup)
        self.layMainWindow.addLayout(self.layRight)
        self.verticalLayout.addLayout(self.layMainWindow)
        self.txeOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.txeOutput.setStyleSheet("")
        self.txeOutput.setReadOnly(True)
        self.txeOutput.setObjectName("txeOutput")
        self.verticalLayout.addWidget(self.txeOutput)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actAbout = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actAbout.setIcon(icon2)
        self.actAbout.setObjectName("actAbout")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Garmin message replacer 1.0.2"))
        self.psbStart.setText(_translate("MainWindow", "START\n"
"messages\n"
"replacing"))
        self.lblHint.setText(_translate("MainWindow", "Please, select desired language file *.GTT to replace messages:"))
        self.psbBrowse.setText(_translate("MainWindow", "Browse ..."))
        self.chcbOverwrite.setText(_translate("MainWindow", "Overwrite origin language file *.GTT"))
        self.chcbBackup.setText(_translate("MainWindow", "Make backup of language and settings files - if available"))
        self.actAbout.setText(_translate("MainWindow", "About"))
        self.actAbout.setToolTip(_translate("MainWindow", "About"))
from . import resources_rc
