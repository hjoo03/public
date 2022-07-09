# -*- coding: utf-8 -*-
# Created: 06/25/2022 04:31
# filename: run.py

import os, sys, time, datetime
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *
from PyQt5 import uic
import chromedriver_autoinstaller
import subprocess

form_class = uic.loadUiType("IS_Settings.ui")[0]
form_class2 = uic.loadUiType("IS_ProgressInfo.ui")[0]


class WebDriver:
	def __init__(self):

		options = Options()
		extension_path = os.path.dirname(os.path.realpath(__file__)) + "/extensions/taobao_image_searcher.crx"
		options.add_extension(extension_path)
		options.add_argument(
			"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")
		subprocess.Popen(
			r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
		option = Options()
		option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
		chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
		self.driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
		self.driver.implicitly_wait(5)
		url = "https://search.shopping.naver.com/search/category/100000021"
		# self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
		self.driver.get(url)
		time.sleep(3)
		self.driver.maximize_window()
		self.action = ActionChains(self.driver)
		self.search_button_path = "/html/body/div[2]/div/div[1]/div[1]/div[1]"

		self.output = []

		"""
		f = open("config.txt", 'r')
		f.readlines()
		"""

	def main(self, amount):
		for i in range(1, amount+1):  # Amount of items to Search
			self.search(i)
			self.fetch_information()

	def close_tab(self, count=1):
		tabs = self.driver.window_handles
		for i in range(count):
			self.driver.switch_to.window(tabs[1])
			self.driver.close()
			tabs = self.driver.window_handles
		self.driver.switch_to.window(tabs[0])

	def search(self, item_no):
		self.hover_pointer(self.xpath(item_no))
		time.sleep(0.15)
		try:
			self.driver.find_element(By.XPATH, self.search_button_path).click()  # Open Extension
		except selenium.common.exceptions.ElementNotInteractableException:
			print("DO NOT Move Mouse Pointer!! Retrying...")
			time.sleep(0.5)
			self.driver.find_element(By.XPATH, self.search_button_path).click()  # Open Extension

		time.sleep(2)
		try:
			self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/div/div/div/div[1]").click()  # Taobao Lite Search
		except selenium.common.exceptions.NoSuchElementException:
			time.sleep(2)
			self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/div/div/div/div[1]").click()  # Taobao Lite Search
		time.sleep(5)

	def hover_pointer(self, target):
		self.action.move_to_element(self.driver.find_element(By.XPATH, target)).perform()

	@staticmethod
	def xpath(item_no):
		return f"// *[ @ id = \"__next\"] / div / div[2] / div / div[3] / div[1] / ul / div / div[{item_no}] / li / div / div[1]"

	def fetch_information(self, amount=12):
		"""
		end = datetime.datetime.now() + datetime.timedelta(seconds=3)
		item_list = self.driver.find_element(By.CLASS_NAME, "simplebar-content")
		while True:
			self.driver.execute_script("arguments[0].scrollBy(0, 2000)", item_list)  # Scroll down to show more information
			time.sleep(1)
			if datetime.datetime.now() > end:
				break
		"""
		close_button = "/html/body/div[2]/div/div[1]/div[1]/div/div[3]/div/div[3]/div[1]"
		for i in range(1, amount+1):  # Amount of items to fetch (Default: 30)
			# TODO: If result is not enough, it has to stop fetching
			xpaths = self.analyzer_xpath(i)  # title, price, sells, seller, location
			self.output = []
			for j in range(5):
				try:
					self.output.append(self.driver.find_element(By.XPATH, xpaths[j]).text)
				except selenium.common.exceptions.NoSuchElementException:
					time.sleep(0.5)
					self.output.append(self.driver.find_element(By.XPATH, xpaths[j]).text)

			print(i, end='')
			print(self.output)
		self.driver.find_element(By.XPATH, close_button).click()
		time.sleep(0.5)

	@staticmethod
	def analyzer_xpath(item_no):
		base_xpath = f"//*[@id=\"ap-sbi-alipriceTaobao-result\"]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[{item_no}]/div/"
		title = base_xpath + "div[3]"
		price = base_xpath + "div[2]/div[1]"
		sells = base_xpath + "div[2]/div[3]"
		seller = base_xpath + "div[4]/div[1]/span"
		location = base_xpath + "div[4]/div[2]"

		return title, price, sells, seller, location


class Excel:
	def __init__(self):
		write_wb = Workbook()
		sheet_title = f""  # 카테고리 이름으로 하면 될듯?
		write_ws = write_wb.create_sheet(sheet_title)
		write_ws.append(["제목", "가격", "구매 수", "판매자", "지역"])


class SettingsWindow(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.onlyInt = QIntValidator()

		self.progress_window = None
		self.money = 0
		self.translate = 0
		self.min_p = 0
		self.max_p = 0
		self.min_b = 0
		self.max_b = 0
		self.p_i = 0
		self.p_c = 0
		self.minprice.setValidator(self.onlyInt)
		self.maxprice.setValidator(self.onlyInt)
		self.minbuy.setValidator(self.onlyInt)
		self.maxbuy.setValidator(self.onlyInt)
		self.peritem.setValidator(self.onlyInt)
		self.percategory.setValidator(self.onlyInt)
		self.minprice.textChanged.connect(self.s_m1_p())
		self.maxprice.textChanged.connect(self.s_m2_p)
		self.minbuy.textChanged.connect(self.s_m1_b)
		self.maxbuy.textChanged.connect(self.s_m2_b)
		self.peritem.textChanged.connect(self.s_p_i)
		self.percategory.textChanged.connect(self.s_p_c)

		self.pushButton.clicked.connect(self.start)  # button triggers start()

		self.cb_money.currentTextChanged.connect(self.set_money_settings)
		self.cb_translate.currentTextChanged.connect(self.set_translate_settings)

	def start(self):
		wd = WebDriver()
		wd.main()
		"""
		Actual Code
		"""
		self.progress_window = ProgressWindow()
		self.clear_button.clicked.connect(self.progress_window.output_clear())

	def s_m1_p(self):
		self.min_p = self.minprice.text()

	def s_m2_p(self):
		self.max_p = self.maxprice.text()

	def s_m1_b(self):
		self.min_b = self.minbuy.text()

	def s_m2_b(self):
		self.max_b = self.maxbuy.text()

	def s_p_i(self):
		self.p_i = self.peritem.text()

	def s_p_c(self):
		self.p_c = self.percategory.text()

	def set_money_settings(self):
		self.money = self.cb_money.currentIndex()

	def set_translate_settings(self):
		self.translate = self.cb_translate.currentIndex()


class ProgressWindow(QMainWindow, form_class2):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()

		pass

	def output(self, msg):
		self.textbrowser.append(msg)

	def output_clear(self):
		self.textbrowser.clear()

"""
if __name__ == "__main__":
	app = QApplication(sys.argv)
	sw = SettingsWindow()
	sw.show()
	app.exec_()
"""

if __name__ == "__main__":
	wd = WebDriver()
	wd.main(5)

