# -*- coding: utf-8 -*-
# tis/run.py

import os, sys, datetime, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, Qt

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
        self.delay = 10
        self.splits = 100
        self.auto_start = True
        self.pause = False
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
        self.checkBox.stateChanged.connect(self.set_as)

        self.status.setStyleSheet("Color : green")
        self.pushButton.clicked.connect(self.start)
        self.pausebtn.clicked.connect(self.pauseF)
        self.splitfile.clicked.connect(self.split)
        self.file_button.clicked.connect(self.select_file)
        self.file_button_2.clicked.connect(self.select_dir)
        self.pausebtn.setEnabled(False)
        self.pushButton.setEnabled(False)

        self.thread, self.worker = None, None
        self.total_items = 0
        self.consecutive_skips = 0
        self.last_row = 0
        self.sig = None

    def split(self):
        self.splitfile.setEnabled(False)
        self.thread = QThread(parent=self)
        self.worker = Worker2()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)

        # noinspection PyUnresolvedReferences
        self.worker.finished.connect(self.thread.quit)
        # noinspection PyUnresolvedReferences
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        Excel.set_directory(self.o_file_dir, self.t_file_dir, self.filename)
        if not self.o_file_dir:
            self.warning_error01()
            return
        if not self.t_file_dir:
            self.warning_error02()
            return

        s = int(self.start_row)
        while True:
            if not Excel.read_sheet[f'A{s}'].value and Excel.read_sheet[f'A{s}'].value != 0:
                self.total_items = s - int(self.start_row)
                break
            s += 1
        Excel.index_range = range(self.start_row, self.start_row + self.total_items)
        log.info(f"File: {self.o_file_dir}; total_items={self.total_items}")

        self.thread.start()

    def start(self) -> None:
        self.pushButton.setEnabled(False)
        self.pausebtn.setEnabled(True)
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        # noinspection PyUnresolvedReferences
        self.worker.finished.connect(self.thread.quit)
        # noinspection PyUnresolvedReferences
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.pause = False
        log.info(f"Thread Started; start_row={self.start_row}, delay={self.delay}, split={self.splits}")
        self.current_label.setText(f"Current {self.last_row}/{self.total_items}")
        self.thread.start()

    def pauseF(self):
        self.pausebtn.setEnabled(False)
        self.pushButton.setEnabled(True)
        self.pause = True
        MW.set_status("red", "Pausing")

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

    def set_as(self, state):
        if state == Qt.checked:
            self.auto_start = True
        else:
            self.auto_start = False

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


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.WD = None
        self.signal = Signal()

    def run(self):
        for cnt, row in enumerate(range(int(MW.start_row), int(MW.start_row) + MW.total_items), start=1):
            if MW.pause:
                try:
                    self.WD.close_driver()
                    del self.WD
                except AttributeError:
                    pass
                except NameError:
                    pass
                MW.set_status("blue", "Idle")
                MW.start_row = row
                MW.startrow_lb.setText(str(row))
            """
            if cnt % 5 == 1:
                try:
                    self.WD.close_driver()
                    del self.WD
                except AttributeError:
                    pass
                self.WD = WebDriver()
                self.signal.signal_status.connect(MW.set_status)
            """
            self.WD = WebDriver()
            self.signal.signal_status.connect(MW.set_status)

            part_row = row - (MW.splits + 6) * (Excel.current_file - 1)
            res = self.main(row, part_row)
            if res["response_code"] == 3:
                # noinspection PyUnresolvedReferences
                self.finished.emit()
                return
            elif res["response_code"] == 2 and cnt % 5 != 0:
                self.WD = WebDriver()
                self.signal.signal_status.connect(MW.set_status)
        # noinspection PyUnresolvedReferences
        self.finished.emit()

    def main(self, row, part_row) -> dict:
        res = self.wd_data(row, part_row)
        if res["response_code"] == 3:
            log.error("3 consecutive skips - return error.")
            return res
        elif res["response_code"] in (1, 2):
            return res
        MW.last_row = row
        time.sleep(int(MW.delay))

        return {"response_code": 100}

    def wd_data(self, row, part_row):
        d = self.WD.main(part_row, MW.p_i, Excel.now_sheet, Excel.row_to_index(row), MW.min_p, MW.min_b, MW.min_b_e, MW.a_i)
        if d["response_code"] != 100:
            Excel.skipped_list.append(d["index"])
            Excel.skips += 1
            MW.consecutive_skips += 1
            if MW.consecutive_skips == 2:
                log.info(f"2 consecutive fails - sleeping for {MW.delay * 20} seconds.")
                MW.set_status("red", "Sleeping")
                self.WD.close_driver()
                del self.WD
                time.sleep(int(MW.delay) * 20)
                MW.set_status("green", "Running")
                return {"response_code": 2}
            if MW.consecutive_skips > 2:
                MW.startrow_lb.setText(str(row-3))
                MW.start_row = int(row) - 3
                MW.warning_error03(timestamp())
                return {"response_code": 3}
            MW.set_status("green", "Running")

            return {"response_code": 1}

        Excel.write(d["data"], row)
        MW.current_label.setText(f"Current {Excel.finished_items}/{MW.total_items}")
        MW.e_saved_label.setText(f"Extra_Saved {Excel.extra}")
        MW.consecutive_skips = 0
        return {"response_code": 100}


class Worker2(QObject):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        MW.set_status("blue", "Splitting")
        Excel.split_file(int(MW.splits) + 6, int(MW.start_row), int(MW.total_items))
        MW.set_status("blue", "Idle")
        MW.pushButton.setEnabled(True)

        if MW.auto_start:
            MW.set_status("green", "Running")
            MW.start()
        # noinspection PyUnresolvedReferences
        self.finished.emit()


def timestamp() -> str:
    return f"[{str(datetime.datetime.now())[:len(str(datetime.datetime.now())) - 7]}]"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = MainWindow()
    log = Logger("mainLogger").logger
    Excel = Excel()
    MW.show()
    app.exec_()