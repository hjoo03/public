# -*- coding: utf-8 -*-
# tis/gui.py

import os, datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
from form import Window
from run import start


# noinspection PyArgumentList
class MainWindow(QMainWindow, Window):
    def __init__(self):
        super().__init__()
        self.onlyInt = QIntValidator()
        self.o_file_dir = ''
        self.t_file_dir = ''
        self.filename = "file"
        self.min_p = 0
        self.min_b = 0
        self.min_b_e = 200
        self.p_i = 10
        self.a_i = 30
        self.start_row = 2
        self.google_lens_code = "yDmH0d"
        self.minprice.setValidator(self.onlyInt)
        self.minbuy.setValidator(self.onlyInt)
        self.minbuy_extra.setValidator(self.onlyInt)
        self.peritem.setValidator(self.onlyInt)
        self.a_item.setValidator(self.onlyInt)
        self.startrow_lb.setValidator(self.onlyInt)
        self.minprice.textChanged.connect(self.s_m1_p)
        self.minbuy.textChanged.connect(self.s_m1_b)
        self.minbuy_extra.textChanged.connect(self.s_m_e)
        self.peritem.textChanged.connect(self.s_p_i)
        self.a_item.textChanged.connect(self.s_a_i)
        self.startrow_lb.textChanged.connect(self.s_sr)
        self.filename_lb.textChanged.connect(self.set_filename)
        self.googlens.textChanged.connect(self.set_goog_lens_code)

        self.status.setStyleSheet("Color : green")
        self.pushButton.clicked.connect(self.start)  # button triggers start()
        self.file_button.clicked.connect(self.select_file)
        self.file_button_2.clicked.connect(self.select_dir)

        self.thread, self.worker = None, None
        self.end = 0
        self.now = 0
        self.skipped = []
        self.consecutive_skips = 0

    def start(self) -> None:
        start(self.o_file_dir, self.t_file_dir, self.filename, self.min_p, self.min_b, self.min_b_e, self.p_i, self.a_i, self.start_row, self.google_lens_code)

    def select_file(self):
        file_filter = "Excel File (*.xlsx *.xls)"
        self.o_file_dir = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select an Excel File",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter=file_filter
        )[0]
        self.file_label.setText(self.o_file_dir)
        self.file_label.repaint()

    def select_dir(self):
        self.t_file_dir = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Select a folder"
        )
        self.file_label_2.setText(self.t_file_dir)
        self.file_label_2.repaint()

    def s_m1_p(self):
        self.min_p = self.minprice.text()

    def s_m1_b(self):
        self.min_b = self.minbuy.text()

    def s_m_e(self):
        self.min_b_e = self.minbuy_extra.text()

    def s_p_i(self):
        self.p_i = self.peritem.text()

    def s_a_i(self):
        self.a_i = self.a_item.text()

    def s_sr(self):
        self.start_row = self.startrow_lb.text()

    def set_filename(self):
        self.filename = self.filename_lb.text()

    def set_goog_lens_code(self):
        self.google_lens_code = self.googlens.text()

    def warning_error01(self):
        QMessageBox.warning(self, "[E01] FileError", "No File Selected!")

    def warning_error02(self):
        QMessageBox.warning(self, "[E02] FileError", "No Target Directory Selected!")

    def warning_error03(self, ts):
        QMessageBox.warning(self, "[E03] UnknownError", f"Unknown Error occurred at [{ts}]")


def timestamp():
    return f"[{str(datetime.datetime.now())[:len(str(datetime.datetime.now())) - 7]}]"
