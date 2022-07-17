# -*- coding: utf-8 -*-
# tis3/run.py TODO: Incomplete

import sys, time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, QObject, pyqtSignal

# local imports
from logger import Logger
from webdriver import WebDriver
from excel import Excel
from gui import MainWindow


def start(ofd, tfd, fn, mp, ms, mse, pi, ai, sr, glc) -> None:
    """
    this method only runs once
    :param ofd: str - original file directory
    :param tfd: str - target file directory
    :param fn: str - filename
    :param mp: int - minimum price
    :param ms: int - minimum sells
    :param mse: int - minimum extra sells
    :param pi: int - data per item
    :param ai: int - analyzed data per item
    :param sr: int - start row
    :param glc: str - google lens code
    :return:
    """
    # Setup Threads
    thread = QThread()
    worker = Worker(Excel, fn, mp, ms, mse, pi, ai, sr, glc)
    worker.moveToThread(thread)
    thread.started.connect(worker.run)
    worker.finished.connect(thread.quit)
    worker.finished.connect(worker.deleteLater)
    thread.finished.connect(thread.deleteLater)

    # Check Excel File
    if not ofd:
        MW.warning_error01()
        return
    if not tfd:
        MW.warning_error02()
        return

    # Read File
    Excel.setup_read_sheet(ofd, "export")
    Excel.copy_file()
    s = int(sr)
    while True:
        if not Excel.sheet[f'A{s}'].value and Excel.sheet[f'A{s}'].value != 0:
            end = s - 1
            break
        s += 1
    MW.saved_label.setText(f"Saved {MW.now}/{end - 1}")
    Excel.setup_target_sheet_init()
    thread.start()


class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, E, fn, mp, ms, mse, pi, ai, sr, glc):
        super().__init__()
        self.WD = None
        self.accumulated_data = []
        self.St = E
        self.fn, self.mp, self.ms, self.mse, self.pi, self.ai, self.sr, self.glc = fn, mp, ms, mse, pi, ai, sr, glc

    def run(self):
        cycles = 0
        for rows in range(int(self.sr), MW.end + 1, 8):
            res = self.main(rows)
            if res["response_code"] == 2:
                # noinspection PyUnresolvedReferences
                self.finished.emit()
                return

            cycles += 1

            if cycles % 4 == 0:
                time.sleep(200)

        skipped_rows = []

        sk_r = []
        for i in range(len(SW.skipped)):
            sk_r.append(SW.skipped[i])
            if i % 7 == 0:
                skipped_rows.append(sk_r)
                sk_r = []

        cycles = 0
        for rows in skipped_rows:
            self.main(rows)
            cycles += 1

            if cycles % 4 == 0:
                time.sleep(180)

        # noinspection PyUnresolvedReferences
        self.finished.emit()

    def main(self, rows):
        self.WD = WebDriver(self.glc)
        self.accumulated_data = []
        for row in range(rows, rows + 8):
            res = self.wd_data(row)
            if res["response_code"] == 2:
                log.error("3 consecutive skips. return error")
                return res
        self.St.write(self.accumulated_data)
        log.info(f"Saved {len(self.accumulated_data)} items")
        SW.saved_label.setText(f"Saved {SW.now}/{SW.end - 1}")

        self.WD.close_driver()
        del self.WD
        time.sleep(2)
        return {"response_code": 916}

    def wd_data(self, row):
        d = self.WD.main(f"B{row}", SW.p_i, self.St.sheet)
        if d["response_code"] != 916:
            SW.skipped.append(row)
            SW.status.setStyleSheet("Color : green")
            SW.status.setText("Normal")
            SW.consecutive_skips += 1
            if SW.consecutive_skips == 2:
                time.sleep(180)
            if SW.consecutive_skips > 2:
                SW.startrow_lb.setText(str(int(SW.now) - 3))
                SW.start_row = int(SW.now) - 3
                SW.warning_error03(timestamp())
                return {"response_code": 2}

            return {"response_code": 3}

        data = self.WD.add_link(self.St.find_sales_high([row, d["data"]], SW.min_p, SW.min_b))
        self.WD.close_extension()
        SW.now += 1
        SW.current_label.setText(f"Current {SW.now}/{SW.end - 1}")
        self.accumulated_data.append(data)
        SW.consecutive_skips = 0
        return {"response_code": 916}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = MainWindow()
    log = Logger()
    WD = WebDriver()
    Excel = Excel()
    MW.show()
    app.exec_()
