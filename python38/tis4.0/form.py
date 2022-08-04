# -*- coding: utf-8 -*-
# tis4/form.py


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(361, 656)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\dev\\public\\python38\\tis4\\mih.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_file.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.btn_file.setObjectName("btn_file")
        self.le_loaddelay = QtWidgets.QLineEdit(self.centralwidget)
        self.le_loaddelay.setGeometry(QtCore.QRect(110, 151, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le_loaddelay.setFont(font)
        self.le_loaddelay.setObjectName("le_loaddelay")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(20, 330, 111, 41))
        self.btn_start.setObjectName("btn_start")
        self.lb_filedir = QtWidgets.QLabel(self.centralwidget)
        self.lb_filedir.setGeometry(QtCore.QRect(20, 50, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lb_filedir.setFont(font)
        self.lb_filedir.setObjectName("lb_filedir")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 270, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.le_fetchdelay = QtWidgets.QLineEdit(self.centralwidget)
        self.le_fetchdelay.setGeometry(QtCore.QRect(110, 190, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le_fetchdelay.setFont(font)
        self.le_fetchdelay.setObjectName("le_fetchdelay")
        self.le_indexmin = QtWidgets.QLineEdit(self.centralwidget)
        self.le_indexmin.setGeometry(QtCore.QRect(110, 270, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le_indexmin.setFont(font)
        self.le_indexmin.setObjectName("le_indexmin")
        self.le_indexmax = QtWidgets.QLineEdit(self.centralwidget)
        self.le_indexmax.setGeometry(QtCore.QRect(190, 270, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le_indexmax.setFont(font)
        self.le_indexmax.setObjectName("le_indexmax")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 270, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(147, 340, 191, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 310, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 130, 321, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 380, 321, 251))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.btn_index = QtWidgets.QPushButton(self.centralwidget)
        self.btn_index.setGeometry(QtCore.QRect(250, 150, 81, 41))
        self.btn_index.setObjectName("btn_index")
        self.skipPush = QtWidgets.QCheckBox(self.centralwidget)
        self.skipPush.setGeometry(QtCore.QRect(250, 230, 101, 20))
        self.skipPush.setObjectName("skipPush")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.le_erhp = QtWidgets.QLineEdit(self.centralwidget)
        self.le_erhp.setGeometry(QtCore.QRect(130, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le_erhp.setFont(font)
        self.le_erhp.setText("")
        self.le_erhp.setObjectName("le_erhp")
        self.skipRename = QtWidgets.QCheckBox(self.centralwidget)
        self.skipRename.setGeometry(QtCore.QRect(250, 200, 101, 20))
        self.skipRename.setObjectName("skipRename")
        self.multiFiles = QtWidgets.QCheckBox(self.centralwidget)
        self.multiFiles.setGeometry(QtCore.QRect(120, 9, 101, 31))
        self.multiFiles.setObjectName("multiFiles")
        self.le_ocv_offset = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ocv_offset.setGeometry(QtCore.QRect(110, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le_ocv_offset.setFont(font)
        self.le_ocv_offset.setObjectName("le_ocv_offset")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "TIS 4"))
        self.btn_file.setText(_translate("Window", "Select"))
        self.le_loaddelay.setText(_translate("Window", "12"))
        self.btn_start.setText(_translate("Window", "Start"))
        self.lb_filedir.setText(_translate("Window", "None"))
        self.label_3.setText(_translate("Window", "Load Delay"))
        self.label_4.setText(_translate("Window", "Fetch Delay"))
        self.label_5.setText(_translate("Window", "Index Range"))
        self.le_fetchdelay.setText(_translate("Window", "2"))
        self.le_indexmin.setText(_translate("Window", "0"))
        self.le_indexmax.setText(_translate("Window", "0"))
        self.label_6.setText(_translate("Window", "~"))
        self.btn_index.setText(_translate("Window", "Index"))
        self.skipPush.setText(_translate("Window", "Skip Push"))
        self.label_2.setText(_translate("Window", "Report Number"))
        self.skipRename.setText(_translate("Window", "Skip Rename"))
        self.multiFiles.setText(_translate("Window", "Multiple Files"))
        self.le_ocv_offset.setText(_translate("Window", "5"))
        self.label_7.setText(_translate("Window", "OCV Offset"))