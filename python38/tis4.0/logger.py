# -*- coding: utf-8 -*-
# tis4/logger.py

import os, logging, datetime
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self, name: str = None):
        filedir = os.getcwd() + "\\log\\"
        if not os.path.isdir(filedir):
            os.makedirs(filedir)

        self.filename = filedir + datetime.datetime.now().strftime('%y%m%d_%H%M') + '.log'
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter(
            u'%(asctime)s [%(levelname)s] %(name)s[%(lineno)d]: "%(message)s"')
        self.file_handler = logging.FileHandler(self.filename)

        log_max_size = 10 * 1024 * 1024  # 20MB
        log_file_count = 20
        rotatingFileHandler = logging.handlers.RotatingFileHandler(
            filename=self.filename,
            maxBytes=log_max_size,
            backupCount=log_file_count
        )
        rotatingFileHandler.setFormatter(self.formatter)
        self.logger.addHandler(rotatingFileHandler)