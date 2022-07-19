# -*- coding: utf-8 -*-
# tis/excel.py

import os, openpyxl, shutil
from openpyxl.drawing.image import Image
from openpyxl_image_loader import SheetImageLoader


class Excel:
    def __init__(self):
        if not os.path.isdir(os.getcwd() + "\\temp\\img\\"):
            os.makedirs(os.getcwd() + "\\temp\\img")

        self.doc = None
        self.ws = None
        self.read_sheet = None
        self.ex_exists = False
        self.extra = 0
        self.finished_items = 0
        self.current_file = 1
        self.in_directory = ''
        self.out_directory = ''
        self.filename = ''
        self.index_range = []
        self.skips = 0
        self.skipped_list = []

    def set_directory(self, in_dir, out_dir, filename):
        self.in_directory = in_dir
        self.out_directory = out_dir + '\\'
        self.filename = filename
        self.read_sheet = openpyxl.load_workbook(self.in_directory).active
        self.create_template()

    def setup_sheet(self):
        self.doc = openpyxl.load_workbook(self.out_directory + self.filename + f"_{self.current_file:02}.xlsx")
        self.ws = self.doc.active

    def setup_extra_sheet(self):
        self.doc = openpyxl.load_workbook(self.out_directory + self.filename + "_high-sales.xlsx")
        self.ws = self.doc.active

    def setup_new_sheet(self):
        self.doc = openpyxl.Workbook()
        self.ws = self.doc.active

    def write(self, data: dict, last_row: int, split: int):
        """
        writes main data in the sheet
        :param split: int
        :param last_row: int, for splitting files
        :param data: tuple, (index, [link1, "2, sales1, price1, sales2, price2], extra_data)
        :return index: int
        """
        extra_data = [data[2]]
        self.write_extra(extra_data)

        if self.finished_items % split == 0 and self.finished_items != 0:
            self.setup_sheet()
            self.ws.delete_rows(2, last_row - 1)
            self.current_file += 1
            self.doc.save(self.out_directory + self.filename + f"_{self.current_file:02}.xlsx")

        if self.finished_items % 5 == 0:
            self.setup_sheet()
            for row in range(2, last_row):
                i = self.ws[f'A{row}'].value
                if i in self.skipped_list:
                    self.ws.delete_rows(row, 1)
            self.skips = 0

        self.setup_sheet()
        index = data[0]
        info = data[1]
        row = self.finished_items % split + 2 + self.skips
        self.ws.add_image(Image(os.getcwd() + rf"\temp\img\{index}_0.jpg"), f"I{row}")
        self.ws.add_image(Image(os.getcwd() + rf"\temp\img\{index}_1.jpg"), f"J{row}")
        self.ws[f'K{row}'].hyperlink = info[0]
        self.ws[f'L{row}'].hyperlink = info[1]
        self.ws[f'K{row}'].value = info[0]
        self.ws[f'L{row}'].value = info[1]
        self.ws[f'K{row}'].style = "Hyperlink"
        self.ws[f'L{row}'].style = "Hyperlink"
        self.ws[f'M{row}'] = f"{info[2]}/{info[3]}"
        self.ws[f'N{row}'] = f"{info[4]}/{info[5]}"
        self.doc.save(self.out_directory + self.filename + f"_{self.current_file:02}.xlsx")
        self.finished_items += 1
        shutil.rmtree(os.getcwd() + "\\temp\\img\\")
        os.makedirs(os.getcwd() + "\\temp\\img")

        return index

    def write_extra(self, data):
        """
        writes extra data in the sheet
        :param data: list, [list of [link, title, sales, price]]
        :return:
        """
        if not self.ex_exists:
            self.create_extra_sheet()
        self.setup_extra_sheet()

        for data_ in data:
            for d in data_:
                self.ws[f'A{self.extra + 2}'] = self.extra
                self.ws[f'C{self.extra + 2}'].hyperlink = d[0]
                self.ws[f'C{self.extra + 2}'].value = d[0]
                self.ws[f'C{self.extra + 2}'].style = "Hyperlink"
                self.ws[f'B{self.extra + 2}'] = d[1]
                self.ws[f'D{self.extra + 2}'] = d[2]
                self.ws[f'E{self.extra + 2}'] = d[3]
                self.extra += 1

        self.doc.save(self.out_directory + self.filename + "_high-sales.xlsx")

    def create_extra_sheet(self):
        self.setup_new_sheet()
        self.ws.append(["Index", "타오바오 상품명", "링크", "구매수", "가격"])
        self.doc.save(self.out_directory + self.filename + "_high-sales.xlsx")
        self.ex_exists = True

    def create_template(self):
        self.doc = openpyxl.load_workbook(self.in_directory)
        self.ws = self.doc.active
        self.ws['I1'] = "사진1"
        self.ws['J1'] = "사진2"
        self.ws['K1'] = "링크1"
        self.ws['L1'] = "링크2"
        self.ws['M1'] = "구매수/가격1"
        self.ws['N1'] = "구매수/가격2"
        self.ws['O1'] = "타오바오 상품명"
        self.doc.save(self.out_directory + self.filename + f"_{self.current_file:02}.xlsx")

    @staticmethod
    def extract_image(index, cell, sheet):  # openpyxl_image_loader.SheetImageLoader
        image_loader = SheetImageLoader(sheet)
        image = image_loader.get(cell)
        rgb_image = image.convert("RGB")
        rgb_image.save(os.getcwd() + rf"\temp\img_{index}.jpg")
        del image, rgb_image, image_loader
        return f"file:///{os.getcwd()}/temp/img_{index}.jpg", os.getcwd() + rf"\temp\img_{index}.jpg", f"img_{index}.jpg"

    def index_to_row(self, index: int) -> int:
        for row in self.index_range:
            if index == int(self.read_sheet[f'A{row}'].value):
                return row

    def row_to_index(self, row: int) -> int:
        return int(self.read_sheet[f'A{row}'].value)
