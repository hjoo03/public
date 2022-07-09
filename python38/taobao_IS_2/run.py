# Resolution: 960 × 1080 (Half of FHD)
# Chrome Only


import os, sys, time, datetime
import selenium.common.exceptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl import Workbook
from PyQt5.QtWidgets import *
from PyQt5 import uic
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess


# form_class = uic.loadUiType("IS_main.ui")[0]


class WebDriver:
	def __init__(self):
		subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
		option = Options()
		option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
		option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36")
		chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
		self.driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
		self.driver.implicitly_wait(5)


"""
class MainWindow(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
"""


WD = WebDriver()
