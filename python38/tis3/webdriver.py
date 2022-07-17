# -*- coding: utf-8 -*-
# tis3/webdriver.py

import subprocess, os, time, pyautogui
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from subprocess import CREATE_NO_WINDOW  # Only available in Windows
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from urllib import parse
# from webdriver_manager.chrome import ChromeDriverManager

from logger import Logger
from excel import Excel

log = Logger()


class WebDriver:
    def __init__(self, glc):
        self.google_lens_code = glc
        subprocess.Popen(
            r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
        option = Options()
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        option.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")
        # chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        # self.chrome_service = ChromeService(ChromeDriverManager().install())
        self.chrome_service = ChromeService("chromedriver.exe")
        self.chrome_service.creationflags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=self.chrome_service, options=option)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        log.info("Webdriver Initiated")

        # TODO: 로그인이 안된 상태에서 검색이 안되므로 프로그램 실행 최초 로그인 필요

        self.try_again_button_path = "//*[@id=\"ap-sbi-taobao-result\"]/div/div[2]/div/div[1]/div[2]/div"
        self.login_button_path = "//*[@id=\"ap-sbi-taobao-result\"]/div/div[2]/div/div[2]/div[2]/div"
        self.verify_button_path = "//*[@id=\"ap-sbi-taobao-result\"]/div/div[2]/div/div[3]/div[2]/div"
        self.search_button_path = f"//*[@id=\"{self.google_lens_code}\"]/div[4]/div/div[1]/div[1]/div[1]/div[1]"

    def main(self, cell, limit, sheet):
        """
        opens image file at the driver
        then searches it on taobao
        :param cell: str, target cell
        :param limit: int, limit of items per image
        :param sheet: Workbook.Sheet(), for preventing I/O on closed file
        :return data: json, {response_code: CODE, data: list of [title, price, sales]}
        """
        img_links = Excel().extract_image(cell, sheet)
        log.info(f"extracted image from sheet \"{sheet}\" {cell}. filename: {img_links[2]}")
        self.driver.get(img_links[0])
        os.remove(img_links[1])
        log.info(f"removed image file: {img_links[2]}")
        return self.search(limit)

    def search(self, limit):
        time.sleep(0.2)
        click(960, 540, 'r')
        time.sleep(0.5)
        click(1000, 680)  # y=650
        time.sleep(4)
        click(1835, 130)  # x=1850
        time.sleep(1)
        self.close_tab_from_front()
        data = self.taobao_extension(limit)
        if not data:  # Unsuccessful Search
            SW.status.setStyleSheet("Color : red")
            SW.status.setText("Skipping...")
            time.sleep(3)
            data = self.analyze(limit)
            if data:
                SW.status.setStyleSheet("Color : green")
                SW.status.setText("Normal")
                return {"response_code": 916, "data": data}

            if data:
                return {"response_code": 916, "data": data}
            else:
                return {"response_code": 1}

        return {"response_code": 916, "data": data}

    def taobao_extension(self, limit):
        self.action.move_to_element(self.driver.find_element(By.XPATH,
                                                             f"//*[@id=\"{self.google_lens_code}\"]/div[3]/c-wiz/div/c-wiz/div/div[1]/div/div[2]/div/div/div/div/div[4]")).perform()
        time.sleep(0.15)
        try:
            self.driver.find_element(By.XPATH, self.search_button_path).click()
        except selenium.common.exceptions.ElementNotInteractableException:
            print("DO NOT Move Mouse Pointer!! Retrying...")
            time.sleep(0.5)
            self.action.move_to_element(self.driver.find_element(By.XPATH,
                                                                 f"//*[@id=\"{self.google_lens_code}\"]/div[3]/c-wiz/div/c-wiz/div/div[1]/div/div[2]/div/div/div/div/div[4]")).perform()
            time.sleep(0.15)
            self.driver.find_element(By.XPATH, self.search_button_path).click()
        try:
            wait = WebDriverWait(self.driver, 15)
            _ = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, self.path_analyzer(1)[0])))
        except selenium.common.exceptions.TimeoutException:
            return

        return self.analyze(limit)

    def analyze(self, limit):
        data = []
        for i in range(1, limit + 1):  # limits amount of items to fetch (Default: 30)
            end_of_list = False
            paths = self.path_analyzer(i)
            output = []  # title, price, sales
            cnt = 0
            for path in paths:
                try:
                    res = self.driver.find_element(By.CSS_SELECTOR, path).text
                    if cnt == 1:
                        res = float(res[1:].replace(',', ''))
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

    def add_link(self, data):
        """
        gets link and analyzes data
        then saves image at temporary directory
        :param data: tuple, (row, [item1, item2], [price1, sales1], [price2, sales2], extra_data)
        # extra_data: [index, title, sales, price]
        :return analyzed_data: tuple, (row, [link1, "2, sales1, "2, price1, "2], extra_data)
        """
        extra_data = []
        for [index, title, sales, price] in data[4]:
            self.driver.find_element(By.CSS_SELECTOR, self.path_analyzer(index + 1)[0]).click()
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])
            link = self.parse_url(self.driver.current_url)
            self.close_tab_from_back()
            extra_data.append([link, title, sales, price])

        links = []
        for i in range(2):
            self.driver.find_element(By.CSS_SELECTOR, self.path_analyzer(data[1][i] + 1)[0]).click()
            time.sleep(1)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(0.2)
            links.append(self.parse_url(self.driver.current_url))
            self.close_tab_from_back()
            img_path = f"#ap-sbi-taobao-result > div > div.ap-list.ap-list--gallery > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div:nth-child({data[1][i] + 1}) > div > div.ap-is-link.ap-product-image > img"
            # imgUrl = self.driver.find_element(By.CSS_SELECTOR, img_path).get_attribute("src")
            self.download_img(img_path, os.getcwd() + rf"\temp\img\{data[0]}_{i}.jpg")

        return data[0], [links[0], links[1], data[2][1], data[3][1], data[2][0], data[3][0]], extra_data

    def close_extension(self):
        close_button = f"//*[@id=\"{SW.google_lens_code}\"]/div[4]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[1]"
        self.driver.find_element(By.XPATH, close_button).click()
        time.sleep(0.5)

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
            return parse.unquote(url[url.index("url=") + 4:url.index("%26ns")], encoding="utf-8")
        elif "member/login.html" in url:
            return url[url.index("redirect=") + 9:url.index("&ns")]
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
            log.error("Invalid Session ID")
            return
        for i in range(count):
            self.driver.switch_to.window(tabs[0])
            self.driver.close()
            try:
                tabs = self.driver.window_handles
            except selenium.common.exceptions.InvalidSessionIdException:
                log.error("Invalid Session ID")
        try:
            self.driver.switch_to.window(tabs[0])
        except selenium.common.exceptions.InvalidSessionIdException:
            log.error("Invalid Session ID")

    def close_tab_from_back(self, count=1):
        tabs = self.driver.window_handles
        for i in range(count):
            self.driver.switch_to.window(tabs[len(tabs) - 1])
            self.driver.close()
            tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])


def click(x, y, rl='l'):
    if rl == 'r':
        pyautogui.rightClick(x, y)
    else:
        pyautogui.click(x, y)
