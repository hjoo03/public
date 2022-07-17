# -*- coding: utf-8 -*-
# tis3/logger.py

import os, logging, datetime
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self):
        if not os.path.isdir(os.getcwd() + "\\log\\"):
            os.makedirs(os.getcwd() + "\\log")

        self.filename = os.getcwd() + '\\log\\' + datetime.datetime.now().strftime('%y%m%d_%H%M') + '.log'
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter(
            u'%(asctime)s [%(levelname)s] File "%(filename)s", line %(lineno)d, in %(funcName)s: "%(message)s"')
        self.file_handler = logging.FileHandler(self.filename)

        log_max_size = 20 * 1024 * 1024  # 20MB
        log_file_count = 20
        rotatingFileHandler = logging.handlers.RotatingFileHandler(
            filename=self.filename,
            maxBytes=log_max_size,
            backupCount=log_file_count
        )
        rotatingFileHandler.setFormatter(self.formatter)
        self.logger.addHandler(rotatingFileHandler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)
