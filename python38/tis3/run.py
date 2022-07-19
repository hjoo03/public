# -*- coding: utf-8 -*-
# tis/run.py

import os, sys, datetime, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot

# Local Imports
from form import Window
from webdriver import WebDriver, Signal
from logger import Logger
from excel import Excel


class MainWindow(QMainWindow, Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.onlyInt = QIntValidator()
        self.o_file_dir = ''
        self.t_file_dir = ''
        self.filename = "file"
        self.e_saved = 0
        self.min_p = 0
        self.min_b = 0
        self.min_b_e = 200
        self.p_i = 30
        self.a_i = 10
        self.start_row = 2
        self.delay = 200
        self.splits = 100
        self.minprice.setValidator(self.onlyInt)
        self.minbuy.setValidator(self.onlyInt)
        self.minbuy_extra.setValidator(self.onlyInt)
        self.peritem.setValidator(self.onlyInt)
        self.a_item.setValidator(self.onlyInt)
        self.startrow_lb.setValidator(self.onlyInt)
        self.delayt.setValidator(self.onlyInt)
        self.split_lb.setValidator(self.onlyInt)
        self.minprice.textChanged.connect(self.s_m1_p)
        self.minbuy.textChanged.connect(self.s_m1_b)
        self.minbuy_extra.textChanged.connect(self.s_m_e)
        self.peritem.textChanged.connect(self.s_p_i)
        self.a_item.textChanged.connect(self.s_a_i)
        self.startrow_lb.textChanged.connect(self.s_sr)
        self.filename_lb.textChanged.connect(self.set_filename)
        self.delayt.textChanged.connect(self.sd)
        self.split_lb.textChanged.connect(self.ss)

        self.status.setStyleSheet("Color : green")
        self.pushButton.clicked.connect(self.start)  # button triggers start()
        self.file_button.clicked.connect(self.select_file)
        self.file_button_2.clicked.connect(self.select_dir)

        self.thread, self.worker = None, None
        self.total_items = 0
        self.current_row = 0
        self.skipped = []
        self.consecutive_skips = 0

    def start(self) -> None:
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        # noinspection PyUnresolvedReferences
        self.worker.finished.connect(self.thread.quit)
        # noinspection PyUnresolvedReferences
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        if not self.o_file_dir:
            self.warning_error01()
            return
        if not self.t_file_dir:
            self.warning_error02()
            return

        Excel.set_directory(self.o_file_dir, self.t_file_dir, self.filename)

        s = int(self.start_row)
        while True:
            if not Excel.read_sheet[f'A{s}'].value and Excel.read_sheet[f'A{s}'].value != 0:
                self.total_items = s - int(self.start_row)
                break
            s += 1
        Excel.index_range = range(self.start_row, self.start_row + self.total_items)
        self.current_label.setText(f"Current {self.current_row}/{self.total_items}")
        self.thread.start()

    def select_file(self):
        file_filter = "Excel File (*.xlsx)"
        self.o_file_dir = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select an Excel File",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter=file_filter
        )[0]
        self.file_label.setText(self.o_file_dir)
        self.file_label.repaint()
        self.filename_lb.setText(self.o_file_dir[self.o_file_dir.rindex('/') + 1:self.o_file_dir.rindex('.xlsx')] + "_result")
        self.filename_lb.repaint()
        self.filename = self.o_file_dir[self.o_file_dir.rindex('/') + 1:self.o_file_dir.rindex('.xlsx')] + "_result"

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

    def sd(self):
        self.delay = self.delayt.text()

    def ss(self):
        self.splits = self.split_lb.text()

    def set_filename(self):
        self.filename = self.filename_lb.text()

    def warning_error01(self):
        QMessageBox.warning(self, "[E01] FileError", "No File Selected!")

    def warning_error02(self):
        QMessageBox.warning(self, "[E02] FileError", "No Target Directory Selected!")

    def warning_error03(self, ts):
        QMessageBox.warning(self, "[E03] UnknownError", f"Unknown Error occurred at [{ts}]")

    @pyqtSlot(str, str)
    def set_status(self, color: str, msg: str):
        self.status.setStyleSheet(f"Color : {color}")
        self.status.setText(msg)

    """
    @pyqtSlot(str, int)
    def search_status(self, label: str, number: int):
        if label == 'e':
            self.e_saved_label.setText(f"Extra_Saved {number}")
        elif label == 'c':
            self.current_label.setText(f"Current {number}/{self.total_items}")
    """


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.WD = None
        self.signal = Signal()

    def run(self):
        for cnt, row in enumerate(range(int(MW.start_row), int(MW.start_row) + MW.total_items), start=1):
            if cnt % 5 == 1:
                try:
                    self.WD.close_driver()
                    del self.WD
                except AttributeError:
                    pass
                self.WD = WebDriver()
                self.signal.signal_status.connect(MW.set_status)
            res = self.main(row)
            if res["response_code"] == 2:
                # noinspection PyUnresolvedReferences
                self.finished.emit()
                return

        # noinspection PyUnresolvedReferences
        self.finished.emit()

    def main(self, row) -> dict:
        res = self.wd_data(row)
        if res["response_code"] == 2:
            log.error("3 consecutive skips. return error")
            return res

        return {"response_code": 100}

    def wd_data(self, row):
        d = self.WD.main(row, MW.p_i, Excel.read_sheet, Excel.row_to_index(row), MW.min_p, MW.min_b, MW.min_b_e, MW.a_i)
        if d["response_code"] != 100:
            Excel.skipped_list.append(d["index"])
            Excel.skips += 1
            MW.set_status("green", "Normal")
            MW.consecutive_skips += 1
            if MW.consecutive_skips == 2:
                time.sleep(int(MW.delay))
            if MW.consecutive_skips > 2:
                MW.startrow_lb.setText(str(row-3))
                MW.start_row = int(row) - 3
                MW.warning_error03(timestamp())
                return {"response_code": 2}

            return {"response_code": 1}

        Excel.write(d["data"], row, int(MW.splits))
        MW.current_label.setText(f"Current {Excel.finished_items}/{MW.total_items}")
        MW.e_saved_label.setText(f"Extra_Saved {Excel.extra}")
        MW.consecutive_skips = 0
        return {"response_code": 100}


def timestamp() -> str:
    return f"[{str(datetime.datetime.now())[:len(str(datetime.datetime.now())) - 7]}]"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = MainWindow()
    log = Logger().logger
    Excel = Excel()
    MW.show()
    app.exec_()
