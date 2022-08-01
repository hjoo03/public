# -*- coding: utf-8 -*-
# tis4/run.py

import os, sys, time, datetime, openpyxl, pyautogui, pyperclip, shutil, threading, requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIntValidator, QTextCursor
from openpyxl.drawing.image import Image

from logger import Logger
from form import Ui_Window

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '\\'


# TODO: add-binary mih.ico
class Macro:
    main_window = (950, 60)
    btn_camera = (342, 135)
    btn_search = (227, 670)
    btn_gallery = (42, 735)
    btn_gallery_lower = (42, 840)
    item_1 = (70, 220)
    result_1 = (110, 350, 1)
    result_2 = (340, 350, 2)
    btn_share = (332, 90)
    btn_copy = (42, 515)
    btn_escape = (350, 930)
    btn_escapeItemDetail = (25, 90)

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

    @staticmethod
    def beforeLocate():
        pyautogui.moveTo(2, 2, 0.1)
        time.sleep(0.1)

    @staticmethod
    def drag():  # TODO: needs to be fixed
        pyautogui.moveTo(90, 620, 0.1)
        time.sleep(0.5)
        pyautogui.dragTo(410, 645, 2.5, pyautogui.easeInOutQuad)


class Excel:
    def setup_sheet(self):
        self.doc = openpyxl.load_workbook(self.tmp)
        self.ws = self.doc.active

    def write(self, row, links):
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
        """
        self.ws[f'M{row}'].value = prices[0]
        self.ws[f'N{row}'].value = prices[1]
        """
        self.doc.save(self.tmp)
        MW.count += 1

    def finalSave(self):
        if not os.path.isdir(os.getcwd() + "\\result\\"):
            os.makedirs(os.getcwd() + "\\result")
        shutil.copy(self.tmp, self.res)
        # os.remove(self.tmp)

    def __init__(self):
        fd = MW.files_dir[:-1]
        fn = fd[fd.rindex('/') + 1:]
        # od = fd[:fd.rindex('/')][:fd[:fd.rindex('/')].rindex('/')] + "\\result\\"
        self.set_directory(fn)

    def set_directory(self, filename):
        self.filename = filename
        self.tmp = os.getcwd() + f"\\_temp_{filename}_result.xlsx"
        self.res = os.getcwd() + "\\result\\" + self.filename + "_result.xlsx"

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
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.onlyInt = QIntValidator()
        self.files_dir = ''
        self._files_dir = ''
        self.excelFilepath = ''
        self.btn_file.clicked.connect(self.select_dir)
        self.skipPush.stateChanged.connect(self.fixState)
        self.skipRename.clicked.connect(self.fixState_)
        self.multiFiles.stateChanged.connect(self.multiFileMethod)
        self.btn_start.setEnabled(False)

        self.loadDelay = 12
        self.fetchDelay = 0  # TODO: indexRange
        self.indexRange = (0, 0)

        self.count = 0

    def multiFileMethod(self):
        if self.multiFiles.isChecked():
            if self.files_dir and self.files_dir != '/':
                self.btn_start.setEnabled(True)
            self.btn_start.clicked.connect(self.multiStart)
            self.btn_index.setEnabled(False)
            self.skipRename.setChecked(False)
            self.skipPush.setChecked(False)
            self.skipPush.setEnabled(False)
            self.skipRename.setEnabled(False)
        else:
            if not self.multiFiles.isChecked():
                self.btn_start.setEnabled(False)
            self.btn_start.clicked.connect(self.start)
            self.btn_index.clicked.connect(self.index)
            self.btn_index.setEnabled(True)
            self.skipPush.setEnabled(True)
            self.skipRename.setEnabled(True)

    def start(self):
        self.btn_start.setEnabled(False)
        if not self.indexValidator():
            self.btn_start.setEnabled(True)
            self.warning_error01()
            return
        if not self.files_dir:
            self.btn_start.setEnabled(True)
            self.warning_error02()
            return
        self.loadDelay = int(self.le_loaddelay.text())
        self.fetchDelay = int(self.le_fetchdelay.text())
        self.errorReportNumber = str(self.le_erhp.text())
        self.worker = Worker()
        self.worker.start()

    def select_dir(self):
        self.files_dir = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Select a folder"
        ) + '/'
        self.lb_filedir.setText(self.files_dir)
        self.lb_filedir.repaint()
        self.files_dir_ = self.files_dir
        if self.multiFiles.isChecked():
            self.btn_start.setEnabled(True)

    def multiStart(self):
        self.workerFinished = False
        self.multiWorker = MultiWorker()
        self.multiWorker.start()

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

    def fixState(self):
        if self.skipPush.isChecked():
            self.skipRename.setChecked(True)

    def fixState_(self):
        if self.skipPush.isChecked() and not self.skipRename.isChecked():
            self.skipRename.setChecked(False)
            self.skipPush.setChecked(False)

    def index(self):
        self.Ex = Excel()
        files = os.listdir(self.files_dir)
        self.realImages = []
        if self.skipPush.isChecked() and self.skipRename.isChecked():
            for file in files:
                if ".xlsx" in file:
                    if "~$" not in file[0:3]:
                        self.excelFilepath = self.files_dir + file
            self.Ex.create_template()
            self.Ex.setup_sheet()
            for cellObj in reversed(list(MW.Ex.ws.columns)[0]):
                try:
                    index = cellObj.value
                    if (index and index != "Index") or index == 0:
                        self.realImages.append(int(index))
                except ValueError:
                    self.output("ERROR: Invalid Literal!")
                    return
        elif self.skipRename.isChecked():
            os.system(Rf"platform-tools\adb.exe shell mkdir sdcard/taobao/{self.Ex.filename}/")
            for file in files:
                if ".xlsx" in file:
                    if "~$" not in file[0:3]:
                        self.excelFilepath = self.files_dir + file
            self.Ex.create_template()
            self.Ex.setup_sheet()
            for cellObj in reversed(list(MW.Ex.ws.columns)[0]):
                try:
                    index = cellObj.value
                    if (index and index != "Index") or index == 0:
                        self.realImages.append(int(index))
                except ValueError:
                    self.output("ERROR: Invalid Literal!")
                    return
            for index in self.realImages:
                os.system(Rf"platform-tools\adb.exe push {self.files_dir}" +
                          f"{int(index):04}.jpg sdcard/taobao/{self.Ex.filename}/{int(index):04}.jpg")
        else:
            os.system(Rf"platform-tools\adb.exe shell mkdir sdcard/taobao/{self.Ex.filename}/")
            for file in files:
                if ".xlsx" not in file:
                    index = file[file.rindex("_")+1:file.rindex(".jpg")]
                    os.rename(self.files_dir + file, self.files_dir + f"{int(index):04}.jpg")
                else:
                    if "~$" not in file[0:3]:
                        self.excelFilepath = self.files_dir + file
            self.Ex.create_template()
            self.Ex.setup_sheet()
            for cellObj in reversed(list(MW.Ex.ws.columns)[0]):
                try:
                    index = cellObj.value
                    if (index and index != "Index") or index == 0:
                        self.realImages.append(int(index))
                except ValueError:
                    self.output("ERROR: Invalid Literal!")
                    return
            for index in self.realImages:
                os.system(Rf"platform-tools\adb.exe push {self.files_dir}" +
                          f"{int(index):04}.jpg sdcard/taobao/{self.Ex.filename}/{int(index):04}.jpg")
        self.progressBar.setValue(0)
        self.progressBar.setRange(0, len(self.realImages))
        self.btn_start.setEnabled(True)
        self.output(f"Index Done; found {len(self.realImages)} items")
        if self.skipPush.isChecked():
            self.output(f"Skipped Push")
        else:
            self.output(f"Pushed {len(self.realImages)} items")
        self.btn_index.setEnabled(False)

    def output(self, msg, error=False):
        if error:
            log.error(msg)
        else:
            log.info(msg)
        self.textBrowser.append(f"[{str(datetime.datetime.now())[11:19]}] " + msg)
        self.textBrowser.moveCursor(QTextCursor.End)

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
        self.itemIndices = []
        self.count = 0
        self.consecutiveSkips = 0
        self.skips = []

    def run(self):
        self.preMain()
        done = []
        skipConstant = 0
        for (count, index) in enumerate(MW.realImages):
            if (count + skipConstant) % 8 == 0 and count != 0:
                log.info(f"Restarting Debugger; count={count}, skipConstant={skipConstant}")
                if done:
                    for i in done:
                        os.system(Rf"platform-tools\adb.exe shell rm sdcard/taobao/{MW.Ex.filename}/{i:04}.jpg")
                    MW.output(f"Deleted Images: ~{done[len(done) - 1]:04}.jpg")
                else:
                    MW.output("Deleted Nothing")
                os.system(R"platform-tools\adb.exe devices")
                os.system(R"platform-tools\adb.exe shell am force-stop com.taobao.taobao")
                MW.output("Restarted Debugger")
                time.sleep(2)
                done = []
                self.launchTaobaoApp()
                time.sleep(3)
                Macro.singleClick(Macro.btn_camera)
                time.sleep(3)
                oldGallery = pyautogui.locateOnScreen(BASE_DIR + "taobaoOldGallery.png", region=(140, 700, 160, 110),
                                                      confidence=0.9)
                Macro.singleClick(Macro.btn_gallery if oldGallery else Macro.btn_gallery_lower)
                time.sleep(3)

            done.append(index)
            Macro.click(self.itemCoordinates[(count + skipConstant) % 8])
            time.sleep(MW.loadDelay)
            Macro.beforeLocate()
            if not pyautogui.locateOnScreen(BASE_DIR + "taobaoItemList.png", region=(0, 30, 460, 400), confidence=0.9):
                MW.output("Sleeping Extra Time")
                time.sleep(20 - MW.loadDelay)
            if not self.fetchData(index, len(MW.realImages) - count + 1):
                skipConstant = 7 - (count % 8)
                self.skips.append((index, len(MW.realImages) - count + 1))
                if self.consecutiveSkips == 3:
                    self.sendReport("error", doneCount=count)
                    return
                self.consecutiveSkips += 1
            else:
                self.consecutiveSkips = 0
            tries = 0
            while True:
                if tries > 5:
                    self.quit()
                    self.wait(2000)
                    return
                Macro.singleClick(Macro.btn_escape)
                time.sleep(3)
                Macro.beforeLocate()
                if pyautogui.locateOnScreen(BASE_DIR + "taobaoCamera.png", confidence=0.9, region=(300, 60, 150, 100)):
                    break
                if pyautogui.locateOnScreen(BASE_DIR + "taobaoMain.png", confidence=0.9, region=(270, 850, 170, 80)):
                    MW.output("Returned from Main")
                    Macro.click(Macro.btn_camera)
                    time.sleep(2)
                    break
                tries += 1
            oldGallery = pyautogui.locateOnScreen(BASE_DIR + "taobaoOldGallery.png", region=(140, 700, 160, 110), confidence=0.9)
            Macro.singleClick(Macro.btn_gallery if oldGallery else Macro.btn_gallery_lower)
            time.sleep(MW.fetchDelay)
            self.lastDone = count

        self.endTime = datetime.datetime.now()
        self.totalTime = self.endTime - self.startTime
        MW.output(f"Fetch Done; total={MW.count}; {self.totalTime.total_seconds() // 3600}h {self.totalTime.total_seconds() // 60}m")
        for i in done:
            os.system(Rf"platform-tools\adb.exe shell rm sdcard/taobao/{MW.Ex.filename}/{i:04}.jpg")
        MW.output(f"Deleted Images: ~{done[len(done) - 1]:04}.jpg")
        MW.Ex.finalSave()
        self.sendReport("success", doneCount=self.lastDone)
        MW.output("Killing ADB")
        os.system(R"platform-tools\adb.exe kill-server")
        MW.output("Deleting SubThread")
        del self.debugger
        MW.workerFinished = True
        self.deleteLater()
        self.quit()

    def fetchData(self, index, writeRow) -> 0 or 1:
        links = []
        urls = []
        Macro.beforeLocate()
        error = pyautogui.locateOnScreen(BASE_DIR + "taobaoError.png", region=(20, 400, 410, 140), confidence=0.9)  # TODO: add-binary
        if error:
            MW.output("Error Popup Detected", error=True)
            Macro.click((360, 500))
            time.sleep(15)
            if pyautogui.locateOnScreen(BASE_DIR + "taobaoErrorLoading.png", region=(60, 300, 300, 450), confidence=0.8):
                MW.output("errorLoading Detected", error=True)
                time.sleep(30)
        Macro.beforeLocate()
        error1 = pyautogui.locateOnScreen(BASE_DIR + "taobaoError_.png", region=(20, 400, 410, 140), confidence=0.9)
        if error1:
            MW.output("Error Popup Detected", error=True)
            Macro.click((360, 500))
            time.sleep(15)
            if pyautogui.locateOnScreen(BASE_DIR + "taobaoErrorLoading.png", region=(60, 300, 300, 450), confidence=0.8):
                MW.output("errorLoading Detected", error=True)
                time.sleep(30)
        offset = 0
        Macro.beforeLocate()
        if not pyautogui.locateOnScreen(BASE_DIR + "taobaoCharacterResult.png", region=(0, 240, 100, 60), confidence=0.95):
            if not pyautogui.locateOnScreen(BASE_DIR + "taobaoFilter1.png", region=(0, 170, 330, 60), confidence=0.95):
                if not pyautogui.locateOnScreen(BASE_DIR + "taobaoFilter2.png", region=(0, 170, 330, 60), confidence=0.95):
                    if not pyautogui.locateOnScreen(BASE_DIR + "taobaoFilter3.png", region=(0, 170, 330, 60), confidence=0.95):
                        if not pyautogui.locateOnScreen(BASE_DIR + "taobaoFilter4.png", region=(0, 170, 330, 60), confidence=0.95):
                            if not pyautogui.locateOnScreen(BASE_DIR + "taobaoFilter5.png", region=(0, 170, 330, 60), confidence=0.95):
                                if not pyautogui.locateOnScreen(BASE_DIR + "taobaoFilter6.png", region=(0, 170, 330, 60), confidence=0.95):
                                    if not pyautogui.locateOnScreen(BASE_DIR + "taobaoItemList.png", region=(0, 30, 460, 200), confidence=0.9):
                                        MW.output("Offset Level = 2")
                                        offset = 100
                                    else:
                                        MW.output("Offset Level = 1")
                                        offset = 50
        else:
            MW.output("Offset Level = -1")
            offset = -170
        for result in (Macro.result_1, Macro.result_2):
            c = 221 if result[2] == 2 else 0
            Macro.beforeLocate()
            time.sleep(1)  # Load Images
            pyautogui.screenshot(f"__temp{c}.png", region=(1 + c, 228 - offset, 216, 216))
            if offset == -170:
                Macro.click((result[0], result[1] + 200))
            else:
                Macro.click(result)
            time.sleep(2.5)
            if pyautogui.locateOnScreen(BASE_DIR + "taobaoVerify.png", region=(30, 200, 400, 600), confidence=0.9):
                Macro.singleClick(Macro.btn_escape)
                time.sleep(2)
            Macro.click(Macro.btn_share)
            time.sleep(2)
            try:
                copyLinkBtn = pyautogui.center(pyautogui.locateOnScreen(BASE_DIR + "taobaoCopyLink.png", confidence=0.9))
            except TypeError:
                MW.count += 1
                ts = datetime.datetime.now().timestamp()
                if not os.path.isdir(os.getcwd() + "\\screenshots\\"):
                    os.makedirs(os.getcwd() + "\\screenshots")
                pyautogui.screenshot(Rf"screenshots\{ts}.png")
                log.error(f"Saved Screenshot: {ts}.png")
                MW.output(f"Skip item[{index}]; row={writeRow}, count={MW.count}", error=True)
                return
            Macro.click(copyLinkBtn)
            time.sleep(2)
            for _ in range(0, 2):
                Macro.singleClick(Macro.btn_escapeItemDetail)
                time.sleep(1.5)
            tries = 0
            while True:
                if tries > 6:
                    return
                if not pyautogui.locateOnScreen(BASE_DIR + "taobaoItemDetail.png", region=(0, 830, 180, 80), confidence=0.95):
                    if not pyautogui.locateOnScreen(BASE_DIR + "taobaoItemDetail2.png", region=(0, 845, 165, 60), confidence=0.95):
                        break
                Macro.singleClick(Macro.btn_escapeItemDetail)
                time.sleep(3)
                tries += 1
            l = pyperclip.paste()
            try:
                links.append(l[4:l.index('「') - 8])
            except ValueError:
                links.append(l)
        # prices = []
        """        
        for link in links:
            url, price = self.redirect_link(link)
            urls.append(url)
            prices.append(price)
        """
        MW.Ex.write(writeRow, links)
        os.remove("__temp0.png")
        os.remove("__temp221.png")
        MW.progressBar.setValue(MW.count)
        MW.output(f"Item[{index}]; row={writeRow}, count={MW.count}")
        return 1

    def preMain(self):
        self.connectDebugger()
        MW.output(f"Attached Debugger to the device")
        time.sleep(5)
        self.launchTaobaoApp()
        MW.output(f"Launched Taobao App")
        Macro().moveWindow()
        time.sleep(3)
        Macro.click(Macro.btn_camera)
        time.sleep(3)
        oldGallery = pyautogui.locateOnScreen(BASE_DIR + "taobaoOldGallery.png", region=(140, 700, 160, 110), confidence=0.9)
        Macro.singleClick(Macro.btn_gallery if oldGallery else Macro.btn_gallery_lower)
        time.sleep(3)
        for i in range(0, 8):
            x = Macro.item_1[0] + ((i % 4) * 106)
            y = Macro.item_1[1] + (106 if (i // 4) % 2 == 1 else 0)
            self.itemCoordinates.append((x, y))
        MW.output(f"Start Fetch")
        self.startTime = datetime.datetime.now()

    """
    @staticmethod
    def redirect_link(link) -> tuple:
        r = requests.get(link)
        r.encoding = "utf-8"
        res = r.text
        res1 = res[res.index("var url = ") + 11:]
        price = res1[res1.index("&price")+7:res1.index("&source")]
        return res1[:res1.index("&price")], price
    """

    @staticmethod
    def launchTaobaoApp():  # TODO: add-binary
        os.system(R"platform-tools\adb.exe shell am start -n com.taobao.taobao/com.taobao.tao.TBMainActivity")

    @staticmethod
    def sendReport(reportType, doneCount=0):
        os.system(R"platform-tools\adb.exe shell am force-stop com.samsung.android.messaging")
        time.sleep(3)
        os.system(R"platform-tools\adb.exe shell am start -n com.samsung.android.messaging/com.android.mms.ui.ConversationComposer")
        ts = datetime.datetime.now()
        time.sleep(3)
        Macro.singleClick((390, 790))
        time.sleep(2)
        pyautogui.typewrite(str(MW.errorReportNumber), interval=0.02)
        time.sleep(3)
        Macro.singleClick((200, 500))
        if reportType == "error":
            pyautogui.typewrite(f"{ts}-!!!!!!400!!!!!!({doneCount})", interval=0.01)
        elif reportType == "success":
            pyautogui.typewrite(f"{ts}-______200______({doneCount})", interval=0.01)
        time.sleep(3)
        Macro.singleClick((410, 510))

    def connectDebugger(self):
        self.debugger = Debugger()
        self.debugger.start()


class MultiWorker(QThread):
    def __init__(self):
        super().__init__()
        log.info("MultiWorker Thread Initiated")

    def run(self):
        multiFiles = os.listdir(MW.files_dir_)
        MW.output(f"MultiFetch Start; fileCount={len(multiFiles)}")
        for (cnt, file) in enumerate(multiFiles, start=1):
            MW.files_dir = MW.files_dir_ + file + '\\'
            MW.index()
            MW.start()
            while True:
                time.sleep(10)
                if MW.workerFinished:
                    MW.output(f"File {cnt}/{len(multiFiles)} Done")
                    break
            MW.workerFinished = False
            del MW.worker
            time.sleep(5)
            MW.count = 0


class Debugger(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        os.system(R"platform-tools\scrcpy.exe -d")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = MainWindow()
    log = Logger().logger
    MW.show()
    app.exec_()
