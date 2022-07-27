import os, sys, time, datetime, openpyxl, pyautogui, pyperclip, shutil, threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIntValidator
from openpyxl.drawing.image import Image

from logger import Logger
from form import Ui_Window


class Macro:
    main_window = (950, 60)
    btn_camera = (342, 135)
    btn_search = (227, 670)
    btn_gallery = (42, 735)
    item_1 = (70, 220)
    result_1 = (110, 350, 1)
    result_2 = (340, 350, 2)
    btn_share = (332, 90)
    btn_copy = (42, 515)
    btn_escape = (350, 930)

    def __init__(self):
        pass

    def moveWindow(self):
        pyautogui.moveTo(self.main_window[0], self.main_window[1])
        pyautogui.dragTo(210, 20, duration=0.25)

    @staticmethod
    def click(coordinate):
        pyautogui.moveTo(coordinate[0], coordinate[1], 0.25)
        pyautogui.doubleClick()
        # pyautogui.click(coordinate[0], coordinate[1])

    @staticmethod
    def singleClick(coordinate):
        pyautogui.moveTo(coordinate[0], coordinate[1], 0.25)
        pyautogui.click()

    @staticmethod
    def scroll(constant: int = 0):
        pyautogui.moveTo(200, 626)
        pyautogui.dragTo(200, 500 + constant, duration=1)


class Excel:
    def setup_sheet(self):
        self.doc = openpyxl.load_workbook(self.tmp)
        self.ws = self.doc.active

    def write(self, row, links, index):
        self.setup_sheet()
        img0 = Image("__temp0.png")
        img0.width, img0.height = 132, 132
        img1 = Image("__temp221.png")
        img1.width, img1.height = 132, 132
        self.ws.add_image(img0, f"I{row}")
        self.ws.add_image(img1, f"J{row}")
        self.ws[f"K{row}"].hyperlink = links[0]
        self.ws[f"L{row}"].hyperlink = links[1]
        self.ws[f'K{row}'].value = links[0]
        self.ws[f'L{row}'].value = links[1]
        self.ws[f'K{row}'].style = "Hyperlink"
        self.ws[f'L{row}'].style = "Hyperlink"
        self.doc.save(self.tmp)
        MW.count += 1
        log.info(f"Write Item[{index}]; row={row}, count={MW.count}")

    def finalSave(self):
        shutil.copy(self.tmp, self.res)
        os.remove(self.tmp)

    def __init__(self):
        fd = MW.files_dir[:-1]
        fn = fd[fd.rindex('/') + 1:]
        od = fd[:fd.rindex('/')][:fd[:fd.rindex('/')].rindex('/')] + "\\result\\"
        self.set_directory(fn, od)

    def set_directory(self, filename, out_dir):
        self.out_directory = out_dir
        self.filename = filename
        self.tmp = os.getcwd() + "\\_temp.xlsx"
        self.res = self.out_directory + self.filename + ".xlsx"

    def create_template(self):
        self.doc = openpyxl.load_workbook(MW.excelFilepath)
        self.ws = self.doc.active
        self.ws['I1'] = "사진1"
        self.ws['J1'] = "사진2"
        self.ws['K1'] = "링크1"
        self.ws['L1'] = "링크2"
        self.ws['M1'] = "구매수/가격1"
        self.ws['N1'] = "구매수/가격2"
        self.ws['O1'] = "타오바오 상품명"
        self.ws.column_dimensions['I'].width = 17.63
        self.ws.column_dimensions['J'].width = 17.63
        self.doc.save(self.tmp)


class MainWindow(QMainWindow, Ui_Window):
    images = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.onlyInt = QIntValidator()
        self.files_dir = ''
        self.excelFilepath = ''
        self.btn_file.clicked.connect(self.select_dir)
        self.btn_start.clicked.connect(self.start)
        self.btn_index.clicked.connect(self.index)

        self.btn_start.setEnabled(False)

        self.loadDelay = 5
        self.fetchDelay = 0  # TODO: indexRange
        self.indexRange = (0, 0)

        self.count = 0

    def start(self):
        self.btn_start.setEnabled(False)
        self.loadDelay = int(self.le_loaddelay.text())
        self.Ex.create_template()
        if not self.indexValidator():
            self.btn_start.setEnabled(True)
            self.warning_error01()
            return
        if not self.files_dir:
            self.btn_start.setEnabled(True)
            self.warning_error02()
            return
        self.fetchDelay = int(self.le_fetchdelay.text())
        self.worker = Worker()
        self.worker.start()

    def select_dir(self):
        self.files_dir = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Select a folder"
        ) + '\\'
        self.lb_filedir.setText(self.files_dir)
        self.lb_filedir.repaint()

    def indexValidator(self):
        iMax = int(self.le_indexmax.text())
        # iMin = int(self.le_indexmin.text())
        if iMax == 0:
            return True
        else:
            """
            if iMin < 0 or iMin > iMax:
                return False
            """
            return False
        # return True

    def index(self):
        self.Ex = Excel()
        files = os.listdir(self.files_dir)
        if self.skipPush.isChecked():
            for file in files:
                if ".xlsx" not in file:
                    self.images.append(int(file[:-4]))
                else:
                    self.excelFilepath = self.files_dir + file
        else:
            os.system(rf"platform-tools\adb.exe shell mkdir sdcard/taobao/{self.Ex.filename}/")
            for file in files:
                if ".xlsx" not in file:
                    index = file[file.rindex("_")+1:file.rindex(".jpg")]
                    os.rename(self.files_dir + file, self.files_dir + f"{int(index):04}.jpg")
                    self.images.append(int(index))
                    os.system(rf"platform-tools\adb.exe push {self.files_dir}" +
                              f"{int(index):04}.jpg sdcard/taobao/{self.Ex.filename}/{int(index):04}.jpg")
                else:
                    self.excelFilepath = self.files_dir + file

        self.progressBar.setRange(0, len(self.images))
        self.btn_start.setEnabled(True)
        self.output(f"Index Done; found {len(self.images)} items")
        if self.skipPush.isChecked():
            self.output(f"Skipped Push")
        else:
            self.output(f"Pushed {len(self.images)} items")
        self.btn_index.setEnabled(False)

    def output(self, msg):
        self.textBrowser.append(f"[{str(datetime.datetime.now())[5:len(str(datetime.datetime.now())) - 7]}] " + msg)

    def warning_error01(self):
        QMessageBox.warning(self, "[E01] FunctionError", "Custom Index Range is not Supported")
        # QMessageBox.warning(self, "[E01] IOError", "Check Index Range!")

    def warning_error02(self):
        QMessageBox.warning(self, "[E02] IOError", "No File Directory Selected!")


class Worker(QThread):
    def __init__(self):
        super().__init__()
        log.info("Worker Thread Initiated")
        self.itemCoordinates = []
        self.count = 0

    def run(self):
        self.preMain()
        done = []
        for (count, item) in enumerate(self.itemCoordinates):

            """
            if count % 4 == 0 and count != 0:
                imageRow = int(count / 4)
                if imageRow % 3 == 2:
                    Macro.scroll(-10)
                else:
                    if imageRow % 60 == 0:
                        Macro.scroll(-10)
                    else:
                        Macro.scroll()
            """
            if count % 8 == 0 and count != 0:
                for i in done:
                    os.system(rf"platform-tools\adb.exe shell rm sdcard/taobao/{MW.Ex.filename}/{i:04}.jpg")
                os.system(r"platform-tools\adb.exe devices")
                os.system(r"platform-tools\adb.exe shell am force-stop com.taobao.taobao")
                time.sleep(2)
                done = []
                self.launchTaobaoApp()
                time.sleep(1)
                Macro.click(Macro.btn_camera)
                time.sleep(3)
                Macro.click(Macro.btn_gallery)
                time.sleep(3)

            done.append(item[2])
            Macro.click(item)
            time.sleep(MW.loadDelay)
            self.fetchData(item[2], len(MW.images) - count + 1)
            while True:
                Macro.singleClick(Macro.btn_escape)
                time.sleep(0.5)
                if pyautogui.locateOnScreen("taobaoCamera.png", confidence=0.9):
                    break
            Macro.click(Macro.btn_gallery)
            time.sleep(0.5)
            time.sleep(MW.fetchDelay)
        self.endTime = datetime.datetime.now()
        self.totalTime = self.endTime - self.startTime
        MW.output(f"Fetch Done; total={MW.count}; {self.totalTime.total_seconds() // 3600}h {self.totalTime.total_seconds() // 60}m")
        log.info(f"Fetch Done; total={MW.count}; {self.totalTime.total_seconds() // 3600}h {self.totalTime.total_seconds() // 60}m")
        MW.output("Deleting SubThread")
        self.deleteLater()
        self.quit()
        self.wait(3000)
        del self.debugger, self

    @staticmethod
    def fetchData(index, writeRow):
        links = []
        error = pyautogui.locateOnScreen("taobaoError.png", confidence=0.9)  # TODO: add-binary
        if error:
            MW.output("Error Popup Detected")
            Macro.click((360, 500))
            time.sleep(5)
        error1 = pyautogui.locateOnScreen("taobaoError_.png", confidence=0.9)
        if error1:
            MW.output("Error Popup Detected")
            Macro.click((360, 500))
            time.sleep(5)
        for result in (Macro.result_1, Macro.result_2):
            c = 221 if result[2] == 2 else 0
            pyautogui.screenshot(f"__temp{c}.png", region=(1+c, 228, 216, 216))
            Macro.click(result)
            time.sleep(2)
            Macro.click(Macro.btn_share)
            time.sleep(2)
            Macro.click(Macro.btn_copy)
            time.sleep(2)
            while True:
                Macro.singleClick(Macro.btn_escape)
                time.sleep(2)
                if pyautogui.locateOnScreen("taobaoItemDetail.png", confidence=0.9):
                    break
            while True:
                Macro.singleClick(Macro.btn_escape)
                time.sleep(2)
                if pyautogui.locateOnScreen("taobaoItemList.png", confidence=0.9):
                    break
            l = pyperclip.paste()
            try:
                links.append(l[4:l.index('「') - 8])
            except ValueError:
                links.append(l)
        MW.Ex.write(writeRow, links, index)
        os.remove("__temp0.png")
        os.remove("__temp221.png")
        MW.progressBar.setValue(MW.count)
        MW.output(f"Item[{index}]; row={writeRow}, count={MW.count}")

    def preMain(self):
        self.connectDebugger()
        MW.output(f"Attached Debugger to the device")
        time.sleep(2)
        self.launchTaobaoApp()
        MW.output(f"Launched Taobao App")
        Macro().moveWindow()
        time.sleep(1)
        Macro.click(Macro.btn_camera)
        time.sleep(5)
        Macro.click(Macro.btn_gallery)
        time.sleep(5)
        for (count, index) in enumerate(reversed(sorted(MW.images))):
            x = (count % 4) * 106
            y = 106 if (count // 4) % 2 == 1 else 0
            self.itemCoordinates.append((Macro.item_1[0] + x, Macro.item_1[1] + y, index))
        MW.output(f"Start Fetch")
        self.startTime = datetime.datetime.now()

    @staticmethod
    def launchTaobaoApp():  # TODO: add-binary
        os.system(r"platform-tools\adb.exe shell am start -n com.taobao.taobao/com.taobao.tao.TBMainActivity")
        time.sleep(3)

    def connectDebugger(self):
        self.debugger = Debugger()
        self.debugger.start()


class Debugger(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        os.system(r"platform-tools\scrcpy.exe -d")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = MainWindow()
    log = Logger().logger
    MW.show()
    app.exec_()
