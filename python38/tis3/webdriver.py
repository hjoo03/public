# -*- coding: utf-8 -*-
# tis3/webdriver.py

import subprocess, os, sys, time, pyautogui
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from subprocess import CREATE_NO_WINDOW  # Only available in Windows
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
from urllib import parse
from PyQt5.QtCore import pyqtSignal, QObject
from logger import Logger

# server_log = Logger("selenium.webdriver.remote.remote_connection").logger
# server_log.setLevel(20)


class Signal(QObject):
    signal_status = pyqtSignal(str, str)

    def emit_signal(self, arg1, arg2):
        # noinspection PyUnresolvedReferences
        self.signal_status.emit(arg1, arg2)


class WebDriver:
    def __init__(self, fd):
        # subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
        self.fd = fd
        self.search_button_path = "/html/body/div/div/div[1]/div[1]/div[1]"
        self.try_again_button_path = "//*[@id=\"ap-sbi-taobao-result\"]/div/div[2]/div/div[1]/div[2]/div"
        self.login_button_path = "//*[@id=\"ap-sbi-taobao-result\"]/div/div[2]/div/div[2]/div[2]/div"
        self.verify_button_path = "//*[@id=\"ap-sbi-taobao-result\"]/div/div[2]/div/div[3]/div[2]/div"

    def config_log(self):
        self.log = Logger(self.fd, "webdriver").logger

    def open_driver(self):
        subprocess.Popen(r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
        if getattr(sys, 'frozen', False):
            chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
            self.chrome_service = ChromeService(chromedriver_path)
        else:
            self.chrome_service = ChromeService("chromedriver.exe")
        self.chrome_service.creationflags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.option)
        self.action = ActionChains(self.driver)
        self.log.info("Webdriver Initiated")
        time.sleep(2)

        self.driver.get("https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Ftaobao.com")
        wait = WebDriverWait(self.driver, 5)
        _ = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id=\"login-form\"]/div[4]/button")))
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//*[@id=\"login-form\"]/div[4]/button").click()
        self.log.info("Login Success")
        time.sleep(5)

        self.driver.get("https://shop-phinf.pstatic.net/20210215_231/1613380295198ISOkx_JPEG/14516078878939416_96934398.jpg?type=m120")
        self.taobao_extension(0)
        time.sleep(5)
        self.log.info("Webdriver Configuration Completed")

    def main(self, row, limit, sheet, index, mp, ms, mse, al):
        """
        get request image file to the driver
        then searches it on taobao
        finally analyzes it and returns the data
        :param al: int, analysis limit
        :param index: excel index of the image
        :param mse: int
        :param ms: int
        :param mp: int
        :param row: int, target row
        :param limit: int, limit of items per image
        :param sheet: Workbook.Sheet(), for preventing I/O on closed file
        :return data: json, {response_code: CODE, data: tuple, (index, basic_data, extra_data)}
        """
        img_link = sheet[f"C{row}"].value
        self.driver.get(img_link)
        Signal().emit_signal("green", "Searching")
        raw_data = self.search(limit)
        if raw_data["response_code"] == 1:
            self.log.info(f"Index: {index} Skipped")
            return {"response_code": 1, "index": index}
        Signal().emit_signal("green", "Fetching Data")
        return self.add_link([index, self.analyze(raw_data, mp, ms, mse, al)])

    def search(self, limit):
        data = self.taobao_extension(limit)
        if not data:  # Unsuccessful Search
            Signal().emit_signal("red", "Retrying")
            time.sleep(3)
            data = self.fetch(limit)
            if data:
                Signal().emit_signal("green", "Normal")
                return {"response_code": 100, "data": data}
            else:
                return {"response_code": 1}

        return {"response_code": 100, "data": data}

    def taobao_extension(self, limit):
        self.action.move_to_element(self.driver.find_element(By.XPATH, f"/html/body/img")).perform()
        try:
            self.driver.find_element(By.XPATH, self.search_button_path).click()
        except selenium.common.exceptions.ElementNotInteractableException:
            print("DO NOT Move Mouse Pointer!! Retrying...")
            time.sleep(0.2)
            self.action.move_to_element(self.driver.find_element(By.XPATH, f"/html/body/img")).perform()
            time.sleep(0.05)
            self.driver.find_element(By.XPATH, self.search_button_path).click()
        try:
            wait = WebDriverWait(self.driver, 20)
            _ = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, self.path_analyzer(1)[0])))
            time.sleep(4)
        except selenium.common.exceptions.TimeoutException:
            try:
                wait = WebDriverWait(self.driver, 15)
                _ = wait.until(ec.element_to_be_clickable((By.XPATH, self.verify_button_path)))
                self.driver.find_element(By.XPATH, self.verify_button_path).click()
                self.drag()
                self.close_tab_from_back()
                try:
                    wait = WebDriverWait(self.driver, 20)
                    _ = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, self.path_analyzer(1)[0])))
                    time.sleep(4)
                except selenium.common.exceptions.TimeoutException:
                    self.log.error("Loading Error")
                    return
            except selenium.common.exceptions.TimeoutException:
                try:
                    wait = WebDriverWait(self.driver, 5)
                    _ = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, self.path_analyzer(1)[0])))
                    time.sleep(4)
                except selenium.common.exceptions.TimeoutException:
                    try:
                        wait = WebDriverWait(self.driver, 10)
                        _ = wait.until(ec.element_to_be_clickable((By.XPATH, self.try_again_button_path)))
                        self.driver.find_element(By.XPATH, self.try_again_button_path).click()
                        wait = WebDriverWait(self.driver, 20)
                        _ = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, self.path_analyzer(1)[0])))
                        time.sleep(4)
                    except selenium.common.exceptions.TimeoutException:
                        self.log.error("Loading Error")
                        return

        return self.fetch(limit)

    def fetch(self, limit):
        data = []
        for i in range(1, limit+1):  # limits amount of items to fetch (Default: 30)
            end_of_list = False
            paths = self.path_analyzer(i)
            output = []  # title, price, sales
            cnt = 0
            for path in paths:
                try:
                    res = self.driver.find_element(By.CSS_SELECTOR, path).text
                    if cnt == 1:
                        res = int(res[1:-3].replace(',', ''))
                    elif cnt == 2:
                        try:
                            res = int(res[:-3])
                        except ValueError:
                            res = 0

                    output.append(res)
                except selenium.common.exceptions.NoSuchElementException:
                    end_of_list = True
                    break
                cnt += 1
            if output:
                data.append(output)
            if end_of_list:
                break

        return data

    @staticmethod
    def analyze(data, min_price, min_sales, min_sales_extra, analyze_limit):
        """
        analyzes data
        :param analyze_limit: int
        :param min_sales_extra: int
        :param data: dict, {response_code: CODE, data: [list of [title, price, sales]]}
        :param min_price: int
        :param min_sales: int
        :return: tuple, ([item1, item2], [price1, sales1], [price2, sales2], extra_data)
        """
        data_list = data["data"]
        data = data_list

        extra_data = []
        for (index, [title, price, sales]) in enumerate(data_list):
            if sales >= int(min_sales_extra):
                extra_data.append([index, title, sales, price])

        sales_list = []
        for d in data_list[:int(analyze_limit)]:
            if (d[1] < min_price) or (d[2] < min_sales):
                sales_list.append(-1)
            else:
                sales_list.append(d[2])
        sorted_list = sorted(sales_list, reverse=True)
        s_1 = sales_list.index(sorted_list[0])
        if len(sales_list) == 1:
            return [s_1, 0], [data[s_1][1], data[s_1][2]], [0, 0], extra_data
        if sorted_list[0] == sorted_list[1]:
            salesM = sorted_list[0]
            s_2 = sales_list[sales_list.index(salesM) + 1:].index(salesM) + sales_list.index(salesM) + 1
        else:
            s_2 = sales_list.index(sorted_list[1])

        return [s_1, s_2], [data[s_1][1], data[s_1][2]], [data[s_2][1], data[s_2][2]], extra_data

    def add_link(self, data):
        """
        adds link to the data
        then saves image at temporary directory
        :param data: list, [index, [[item1, item2], [price1, sales1], [price2, sales2], extra_data]]
        # extra_data: [index, title, sales, price]
        :return: json, {response_code: CODE, data: tuple, (index, basic_data, extra_data)}
        """
        extra_data = []
        for [index, title, sales, price] in data[1][3]:
            self.driver.find_element(By.CSS_SELECTOR, self.path_analyzer(index+1)[0]).click()
            time.sleep(0.5)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(0.2)
            link = self.parse_url(self.driver.current_url)
            self.close_tab_from_back()
            extra_data.append([link, title, sales, price])

        links = []
        # img_links = []
        for i in range(2):
            self.driver.find_element(By.CSS_SELECTOR, self.path_analyzer(data[1][0][i]+1)[0]).click()
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(1)
            links.append(self.parse_url(self.driver.current_url))
            self.close_tab_from_back()

            img_path = f"#ap-sbi-taobao-result > div > div.ap-list.ap-list--gallery > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div:nth-child({data[1][0][i]+1}) > div > div.ap-is-link.ap-product-image > img"
            # imgUrl = self.driver.find_element(By.CSS_SELECTOR, img_path).get_attribute("src")
            # img_links.append(imgUrl)
            self.download_img(img_path, os.getcwd() + rf"\temp\img\{data[0]}_{i}.jpg")

        self.log.info(f"Index: {data[0]} Fetched")
        output = [data[0], [links[0], links[1], data[1][1][1], data[1][1][0], data[1][2][1], data[1][2][0]], extra_data]
        return {"response_code": 100, "data": output}

    """
    def close_extension(self):
        close_button = f"/html/body/div/div/div[1]/div[1]/div/div[3]/div/div[3]/div[1]"
        self.driver.find_element(By.XPATH, close_button).click()
        time.sleep(0.5)
    """

    @staticmethod
    def drag():
        time.sleep(5)
        pyautogui.moveTo(490, 580)
        pyautogui.drag(370, 20, 2, pyautogui.easeInQuad, button="left")
        time.sleep(5)

    def download_img(self, css_path, file_path):
        with open(file_path, "wb") as file:
            img = self.driver.find_element(By.CSS_SELECTOR, css_path)
            file.write(img.screenshot_as_png)

    def close_driver(self):
        try:
            self.close_tab_from_front(len(self.driver.window_handles))
            self.driver.quit()
        except selenium.common.exceptions.InvalidSessionIdException:
            pass

    @staticmethod
    def parse_url(url):
        if "ali_redirect.html?url" in url:
            return parse.unquote(url[url.index("url=")+4:url.index("%26ns")], encoding="utf-8")
        elif "member/login.html" in url:
            return url[url.index("redirect=")+9:url.index("&ns")]
        else:
            return url

    @staticmethod
    def path_analyzer(item_no):
        base_path = f"#ap-sbi-taobao-result > div > div.ap-list.ap-list--gallery > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div:nth-child({item_no}) > div > "
        price = base_path + "div.ap-tb-deal-info > div.ap-product-price"
        sales = base_path + "div.ap-tb-deal-info > div.ap-tb-sales"
        title = base_path + "div.ap-is-link.ap-product-title"
        return title, price, sales

    def close_tab_from_front(self, count=1):
        try:
            tabs = self.driver.window_handles
        except selenium.common.exceptions.InvalidSessionIdException:
            return
        for i in range(count):
            self.driver.switch_to.window(tabs[0])
            self.driver.close()
            try:
                tabs = self.driver.window_handles
            except selenium.common.exceptions.InvalidSessionIdException:
                return
        try:
            self.driver.switch_to.window(tabs[0])
        except selenium.common.exceptions.InvalidSessionIdException:
            self.log.error("Invalid Session ID")

    def close_tab_from_back(self, count=1):
        tabs = self.driver.window_handles
        for i in range(count):
            self.driver.switch_to.window(tabs[len(tabs)-1])
            self.driver.close()
            tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])
