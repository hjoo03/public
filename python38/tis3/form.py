# -*- coding: utf-8 -*-
# tis3/form.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Window(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(842, 388)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../carrot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(150, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 30, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.minprice = QtWidgets.QLineEdit(self.centralwidget)
        self.minprice.setGeometry(QtCore.QRect(180, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.minprice.setFont(font)
        self.minprice.setObjectName("minprice")
        self.minbuy = QtWidgets.QLineEdit(self.centralwidget)
        self.minbuy.setGeometry(QtCore.QRect(150, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.minbuy.setFont(font)
        self.minbuy.setObjectName("minbuy")
        self.peritem = QtWidgets.QLineEdit(self.centralwidget)
        self.peritem.setGeometry(QtCore.QRect(90, 170, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.peritem.setFont(font)
        self.peritem.setObjectName("peritem")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(80, 260, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.file_label = QtWidgets.QLabel(self.centralwidget)
        self.file_label.setGeometry(QtCore.QRect(170, 260, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.file_label.setFont(font)
        self.file_label.setObjectName("file_label")
        self.file_button = QtWidgets.QPushButton(self.centralwidget)
        self.file_button.setGeometry(QtCore.QRect(10, 260, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.file_button.setFont(font)
        self.file_button.setObjectName("file_button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.minbuy_extra = QtWidgets.QLineEdit(self.centralwidget)
        self.minbuy_extra.setGeometry(QtCore.QRect(120, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.minbuy_extra.setFont(font)
        self.minbuy_extra.setObjectName("minbuy_extra")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 200, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.current_label = QtWidgets.QLabel(self.centralwidget)
        self.current_label.setGeometry(QtCore.QRect(650, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.current_label.setFont(font)
        self.current_label.setObjectName("current_label")
        self.file_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.file_button_2.setGeometry(QtCore.QRect(10, 310, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.file_button_2.setFont(font)
        self.file_button_2.setObjectName("file_button_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(80, 310, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.file_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.file_label_2.setGeometry(QtCore.QRect(210, 310, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.file_label_2.setFont(font)
        self.file_label_2.setObjectName("file_label_2")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(170, 340, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.filename_lb = QtWidgets.QLineEdit(self.centralwidget)
        self.filename_lb.setGeometry(QtCore.QRect(250, 340, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.filename_lb.setFont(font)
        self.filename_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filename_lb.setObjectName("filename_lb")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(560, 340, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.a_item = QtWidgets.QLineEdit(self.centralwidget)
        self.a_item.setGeometry(QtCore.QRect(90, 130, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.a_item.setFont(font)
        self.a_item.setObjectName("a_item")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(30, 170, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(150, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(710, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.status_2 = QtWidgets.QLabel(self.centralwidget)
        self.status_2.setGeometry(QtCore.QRect(650, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_2.setFont(font)
        self.status_2.setObjectName("status_2")
        self.e_saved_label = QtWidgets.QLabel(self.centralwidget)
        self.e_saved_label.setGeometry(QtCore.QRect(650, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.e_saved_label.setFont(font)
        self.e_saved_label.setObjectName("e_saved_label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.startrow_lb = QtWidgets.QLineEdit(self.centralwidget)
        self.startrow_lb.setGeometry(QtCore.QRect(490, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.startrow_lb.setFont(font)
        self.startrow_lb.setObjectName("startrow_lb")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(380, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.delayt = QtWidgets.QLineEdit(self.centralwidget)
        self.delayt.setGeometry(QtCore.QRect(490, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.delayt.setFont(font)
        self.delayt.setObjectName("delayt")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(390, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        # self.split_lb = QtWidgets.QLineEdit(self.centralwidget)
        # self.split_lb.setGeometry(QtCore.QRect(490, 130, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        # self.split_lb.setFont(font)
        # self.split_lb.setObjectName("split_lb")
        # self.label_9 = QtWidgets.QLabel(self.centralwidget)
        # self.label_9.setGeometry(QtCore.QRect(410, 130, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        # self.label_9.setFont(font)
        # self.label_9.setObjectName("label_9")
        # self.splitfile = QtWidgets.QPushButton(self.centralwidget)
        # self.splitfile.setGeometry(QtCore.QRect(470, 200, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        # self.splitfile.setFont(font)
        # self.splitfile.setObjectName("splitfile")
        # self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        # self.checkBox.setGeometry(QtCore.QRect(700, 100, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        # self.checkBox.setFont(font)
        # self.checkBox.setChecked(True)
        # self.checkBox.setObjectName("checkBox")
        self.pausebtn = QtWidgets.QPushButton(self.centralwidget)
        self.pausebtn.setGeometry(QtCore.QRect(760, 30, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pausebtn.setFont(font)
        self.pausebtn.setObjectName("pausebtn")
        SettingsWindow.setCentralWidget(self.centralwidget)
        self.label_2.setBuddy(self.minprice)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)
        SettingsWindow.setTabOrder(self.minprice, self.minbuy)
        SettingsWindow.setTabOrder(self.minbuy, self.peritem)
        SettingsWindow.setTabOrder(self.peritem, self.pushButton)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Taobao Image Searcher"))
        self.label.setText(_translate("SettingsWindow", "기본 설정"))
        self.label_2.setText(_translate("SettingsWindow", "가격 하한 (USD) :"))
        self.label_4.setText(_translate("SettingsWindow", "구매 수 하한 :"))
        self.label_12.setText(_translate("SettingsWindow", "상품 당"))
        self.label_13.setText(_translate("SettingsWindow", "개의 결과를 분석합니다."))
        self.pushButton.setText(_translate("SettingsWindow", "Start"))
        self.minprice.setText(_translate("SettingsWindow", "0"))
        self.minbuy.setText(_translate("SettingsWindow", "0"))
        self.peritem.setText(_translate("SettingsWindow", "30"))
        self.label_14.setText(_translate("SettingsWindow", "Selected File:"))
        self.file_label.setText(_translate("SettingsWindow", "None"))
        self.file_button.setText(_translate("SettingsWindow", "Select"))
        self.label_5.setText(_translate("SettingsWindow", "구매 수가 "))
        self.minbuy_extra.setText(_translate("SettingsWindow", "200"))
        self.label_6.setText(_translate("SettingsWindow", "이상인 항목을 추가로 가져옵니다."))
        self.current_label.setText(_translate("SettingsWindow", "Current 0/0"))
        self.file_button_2.setText(_translate("SettingsWindow", "Select"))
        self.label_15.setText(_translate("SettingsWindow", "Selected Directory:"))
        self.file_label_2.setText(_translate("SettingsWindow", "None"))
        self.label_16.setText(_translate("SettingsWindow", "File Name: "))
        self.filename_lb.setText(_translate("SettingsWindow", "file"))
        self.label_17.setText(_translate("SettingsWindow", "_nn.xlsx"))
        self.a_item.setText(_translate("SettingsWindow", "10"))
        self.label_18.setText(_translate("SettingsWindow", "상품 당"))
        self.label_19.setText(_translate("SettingsWindow", "개의 결과 중"))
        self.status.setText(_translate("SettingsWindow", "Normal"))
        self.status_2.setText(_translate("SettingsWindow", "Status:"))
        self.e_saved_label.setText(_translate("SettingsWindow", "Extra_Saved 0"))
        self.label_7.setText(_translate("SettingsWindow", "Start row:"))
        self.startrow_lb.setText(_translate("SettingsWindow", "2"))
        self.label_8.setText(_translate("SettingsWindow", "Delay (sec) :"))
        self.delayt.setText(_translate("SettingsWindow", "120"))
        self.label_10.setText(_translate("SettingsWindow", "고급 설정"))
        # self.split_lb.setText(_translate("SettingsWindow", "100"))
        # self.label_9.setText(_translate("SettingsWindow", "Split files:"))
        # self.splitfile.setText(_translate("SettingsWindow", "Split"))
        # self.checkBox.setText(_translate("SettingsWindow", "Auto Start"))
        self.pausebtn.setText(_translate("SettingsWindow", "Pause"))
