# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\dev\public\python38\Mafia42\searchuser\sub.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SubWindow(object):
    def setupUi(self, SubWindow):
        SubWindow.setObjectName("SubWindow")
        SubWindow.resize(485, 924)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Joo/Documents/joo/main/지나/지나당근.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubWindow.setWindowIcon(icon)
        SubWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(5, 1, 471, 901))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        self.textBrowser.setFont(font)
        self.textBrowser.setAccessibleDescription("")
        self.textBrowser.setObjectName("textBrowser")
        SubWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SubWindow)
        self.statusbar.setObjectName("statusbar")
        SubWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubWindow)
        QtCore.QMetaObject.connectSlotsByName(SubWindow)

    def retranslateUi(self, SubWindow):
        _translate = QtCore.QCoreApplication.translate
        SubWindow.setWindowTitle(_translate("SubWindow", "User Information"))
