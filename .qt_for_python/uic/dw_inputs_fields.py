# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\dev\public\python38\tis4\temp\data\dev\Anaconda\Lib\site-packages\qdarkstyle\example\ui\dw_inputs_fields.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(703, 557)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.fontComboBox = QtWidgets.QFontComboBox(self.dockWidgetContents)
        self.fontComboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.fontComboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout.addWidget(self.fontComboBox, 1, 1, 1, 1)
        self.fontComboBoxDis = QtWidgets.QFontComboBox(self.dockWidgetContents)
        self.fontComboBoxDis.setEnabled(False)
        self.fontComboBoxDis.setMinimumSize(QtCore.QSize(0, 0))
        self.fontComboBoxDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fontComboBoxDis.setObjectName("fontComboBoxDis")
        self.gridLayout.addWidget(self.fontComboBoxDis, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBoxEdit = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBoxEdit.setEditable(True)
        self.comboBoxEdit.setObjectName("comboBoxEdit")
        self.comboBoxEdit.addItem("")
        self.comboBoxEdit.addItem("")
        self.comboBoxEdit.addItem("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/qss_icons/dark/rc/window_undock_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxEdit.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/qss_icons/dark/rc/window_close_focus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBoxEdit.addItem(icon1, "")
        self.gridLayout.addWidget(self.comboBoxEdit, 2, 1, 1, 1)
        self.comboBoxEditDis = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBoxEditDis.setEnabled(False)
        self.comboBoxEditDis.setEditable(True)
        self.comboBoxEditDis.setObjectName("comboBoxEditDis")
        self.comboBoxEditDis.addItem("")
        self.comboBoxEditDis.addItem("")
        self.comboBoxEditDis.addItem("")
        self.comboBoxEditDis.setItemText(2, "")
        self.gridLayout.addWidget(self.comboBoxEditDis, 2, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)
        self.lineEditDis = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEditDis.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDis.sizePolicy().hasHeightForWidth())
        self.lineEditDis.setSizePolicy(sizePolicy)
        self.lineEditDis.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditDis.setObjectName("lineEditDis")
        self.gridLayout.addWidget(self.lineEditDis, 3, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.dockWidgetContents)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 1, 1, 1)
        self.textEditDis = QtWidgets.QTextEdit(self.dockWidgetContents)
        self.textEditDis.setEnabled(False)
        self.textEditDis.setMinimumSize(QtCore.QSize(0, 0))
        self.textEditDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEditDis.setObjectName("textEditDis")
        self.gridLayout.addWidget(self.textEditDis, 4, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.dockWidgetContents)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 5, 1, 1, 1)
        self.plainTextEditDis = QtWidgets.QPlainTextEdit(self.dockWidgetContents)
        self.plainTextEditDis.setEnabled(False)
        self.plainTextEditDis.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEditDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plainTextEditDis.setObjectName("plainTextEditDis")
        self.gridLayout.addWidget(self.plainTextEditDis, 5, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 6, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 6, 1, 1, 1)
        self.spinBoxDis = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxDis.setEnabled(False)
        self.spinBoxDis.setMinimumSize(QtCore.QSize(0, 0))
        self.spinBoxDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spinBoxDis.setObjectName("spinBoxDis")
        self.gridLayout.addWidget(self.spinBoxDis, 6, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_17.setMinimumSize(QtCore.QSize(0, 0))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 7, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 7, 1, 1, 1)
        self.doubleSpinBoxDis = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.doubleSpinBoxDis.setEnabled(False)
        self.doubleSpinBoxDis.setMinimumSize(QtCore.QSize(0, 0))
        self.doubleSpinBoxDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.doubleSpinBoxDis.setObjectName("doubleSpinBoxDis")
        self.gridLayout.addWidget(self.doubleSpinBoxDis, 7, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 8, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.dockWidgetContents)
        self.timeEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.timeEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 8, 1, 1, 1)
        self.timeEditDis = QtWidgets.QTimeEdit(self.dockWidgetContents)
        self.timeEditDis.setEnabled(False)
        self.timeEditDis.setMinimumSize(QtCore.QSize(0, 0))
        self.timeEditDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.timeEditDis.setObjectName("timeEditDis")
        self.gridLayout.addWidget(self.timeEditDis, 8, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 9, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.dockWidgetContents)
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.dateEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 9, 1, 1, 1)
        self.dateEditDis = QtWidgets.QDateEdit(self.dockWidgetContents)
        self.dateEditDis.setEnabled(False)
        self.dateEditDis.setMinimumSize(QtCore.QSize(0, 0))
        self.dateEditDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dateEditDis.setObjectName("dateEditDis")
        self.gridLayout.addWidget(self.dateEditDis, 9, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 10, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.dockWidgetContents)
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.dateTimeEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 10, 1, 1, 1)
        self.dateTimeEditDis = QtWidgets.QDateTimeEdit(self.dockWidgetContents)
        self.dateTimeEditDis.setEnabled(False)
        self.dateTimeEditDis.setMinimumSize(QtCore.QSize(0, 0))
        self.dateTimeEditDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dateTimeEditDis.setObjectName("dateTimeEditDis")
        self.gridLayout.addWidget(self.dateTimeEditDis, 10, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 11, 0, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.gridLayout.addWidget(self.label_51, 12, 0, 1, 3)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        self.fontComboBox.editTextChanged['QString'].connect(self.fontComboBoxDis.setEditText) # type: ignore
        self.lineEdit.textEdited['QString'].connect(self.lineEditDis.setText) # type: ignore
        self.spinBox.valueChanged['int'].connect(self.spinBoxDis.setValue) # type: ignore
        self.doubleSpinBox.valueChanged['double'].connect(self.doubleSpinBoxDis.setValue) # type: ignore
        self.timeEdit.timeChanged['QTime'].connect(self.timeEditDis.setTime) # type: ignore
        self.dateEdit.dateTimeChanged['QDateTime'].connect(self.dateEditDis.setDateTime) # type: ignore
        self.dateTimeEdit.dateTimeChanged['QDateTime'].connect(self.dateTimeEditDis.setDateTime) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "Inputs - Fields"))
        self.label.setText(_translate("DockWidget", "Enabled"))
        self.label_2.setText(_translate("DockWidget", "Disabled"))
        self.label_12.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_12.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_12.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_12.setText(_translate("DockWidget", "FontComboBox"))
        self.fontComboBox.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.fontComboBox.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.fontComboBox.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.fontComboBoxDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.fontComboBoxDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.fontComboBoxDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_3.setText(_translate("DockWidget", "<html><head/><body><p><span style=\" font-weight:600;\">ComboBox</span></p></body></html>"))
        self.comboBoxEdit.setItemText(0, _translate("DockWidget", "ComboBoxEditable"))
        self.comboBoxEdit.setItemText(1, _translate("DockWidget", "Option 1 No Icon"))
        self.comboBoxEdit.setItemText(2, _translate("DockWidget", "Option 2 No Icon"))
        self.comboBoxEdit.setItemText(3, _translate("DockWidget", "Option 1 With Icon"))
        self.comboBoxEdit.setItemText(4, _translate("DockWidget", "Option 2 With Icon"))
        self.comboBoxEditDis.setItemText(0, _translate("DockWidget", "ComboBoxEditable"))
        self.comboBoxEditDis.setItemText(1, _translate("DockWidget", "Second option"))
        self.label_13.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_13.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_13.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_13.setText(_translate("DockWidget", "LineEdit"))
        self.lineEdit.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.lineEdit.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.lineEdit.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.lineEdit.setText(_translate("DockWidget", "LineEdit"))
        self.lineEditDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.lineEditDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.lineEditDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.lineEditDis.setText(_translate("DockWidget", "LineEdit"))
        self.label_14.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_14.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_14.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_14.setText(_translate("DockWidget", "TextEdit"))
        self.textEdit.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.textEdit.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.textEdit.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.textEdit.setHtml(_translate("DockWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">TextEdit</span></p></body></html>"))
        self.textEditDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.textEditDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.textEditDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.textEditDis.setHtml(_translate("DockWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">TextEdit</span></p></body></html>"))
        self.label_15.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_15.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_15.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_15.setText(_translate("DockWidget", "PlainTextEdit"))
        self.plainTextEdit.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.plainTextEdit.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.plainTextEdit.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.plainTextEdit.setPlainText(_translate("DockWidget", "PlainTextEdit"))
        self.plainTextEditDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.plainTextEditDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.plainTextEditDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.plainTextEditDis.setPlainText(_translate("DockWidget", "PlainTextEdit"))
        self.label_16.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_16.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_16.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_16.setText(_translate("DockWidget", "SpinBox"))
        self.spinBox.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.spinBox.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.spinBox.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.spinBoxDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.spinBoxDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.spinBoxDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_17.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_17.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_17.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_17.setText(_translate("DockWidget", "DoubleSpinBox"))
        self.doubleSpinBox.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.doubleSpinBox.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.doubleSpinBox.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.doubleSpinBoxDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.doubleSpinBoxDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.doubleSpinBoxDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_18.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_18.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_18.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_18.setText(_translate("DockWidget", "TimeEdit"))
        self.timeEdit.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.timeEdit.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.timeEdit.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.timeEditDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.timeEditDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.timeEditDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_19.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_19.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_19.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_19.setText(_translate("DockWidget", "DateEdit"))
        self.dateEdit.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.dateEdit.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.dateEdit.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.dateEditDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.dateEditDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.dateEditDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_20.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_20.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_20.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_20.setText(_translate("DockWidget", "TimeDateEdit"))
        self.dateTimeEdit.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.dateTimeEdit.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.dateTimeEdit.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.dateTimeEditDis.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.dateTimeEditDis.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.dateTimeEditDis.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_51.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_51.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_51.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_51.setText(_translate("DockWidget", "Inside DockWidget"))
import style_rc
