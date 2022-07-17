# -*- coding: utf-8 -*-
# tis/excel.py

import os, openpyxl, shutil, datetime
from openpyxl.drawing.image import Image
from openpyxl_image_loader import SheetImageLoader


class Excel:
    def __init__(self):
        if not os.path.isdir(os.getcwd() + "\\temp\\img\\"):
            os.makedirs(os.getcwd() + "\\temp\\img")

        self.doc = None
        self.sheet = None
        self.ws = None
        self.extra = 0

    def setup_read_sheet(self, file_directory, sheet_name):
        self.doc = openpyxl.load_workbook(file_directory)
        self.sheet = self.doc[sheet_name]

    def setup_target_sheet(self):
        self.doc = openpyxl.load_workbook(SW.t_file_dir + "/" + SW.filename + ".xlsx")
        self.ws = self.doc.active

    def write(self, data):
        """
        writes main data in the sheet
        :param data: tuple, list of (row, [link1, "2, sales1, "2, price1, "2], extra_data)
        :return:
        """
        self.setup_target_sheet()
        extra_data = []
        for item in data:
            extra_data.append(item[2])

        self.write_extra(extra_data)
        for (row, info, _) in data:
            self.ws.add_image(Image(os.getcwd() + rf"\temp\img\{row}_0.jpg"), f"H{row}")
            self.ws.add_image(Image(os.getcwd() + rf"\temp\img\{row}_1.jpg"), f"I{row}")
            self.ws[f'J{row}'] = info[0]
            self.ws[f'K{row}'] = info[1]
            self.ws[f'L{row}'] = f"{info[2]}/{info[4]}"
            self.ws[f'M{row}'] = f"{info[3]}/{info[5]}"

        self.doc.save(SW.t_file_dir + "/" + SW.filename + ".xlsx")
        SW.e_saved_label.setText(f"Extra_Saved {self.extra}")
        shutil.rmtree(os.getcwd() + "\\temp\\img\\")
        os.makedirs(os.getcwd() + "\\temp\\img")

    def write_extra(self, data):
        """
        writes extra data in the sheet
        :param data: list, list of [link, title, sales, price]
        :return:
        """
        for data_ in data:
            for d in data_:
                self.ws[f'J{SW.end + self.extra + 1}'] = d[0]
                self.ws[f'L{SW.end + self.extra + 1}'] = f"{d[2]}/{d[3]}"
                self.ws[f'N{SW.end + self.extra + 1}'] = d[1]
                self.extra += 1

    @staticmethod
    def find_sales_high(data, min_price, min_sales):
        """
        analyzes data
        :param data: list, [row, list of [title, price, sales]]
        :param min_price: int
        :param min_sales: int
        :return high_sales_data: tuple, (row, [item1, item2], [price1, sales1], [price2, sales2], extra_data)
        """
        data_list = data[1]
        index = 0
        extra_data = []
        for (title, price, sales) in data_list:
            if sales >= int(SW.min_b_e):
                extra_data.append([index, title, sales, price])
            index += 1

        sales_list = []
        for d in data[1]:
            if (d[1] < min_price) or (d[2] < min_sales):
                sales_list.append(-1)
            else:
                sales_list.append(d[2])
        sorted_list = sorted(sales_list, reverse=True)
        s_1 = sales_list.index(sorted_list[0])
        if len(sales_list) == 1:
            return data[0], [s_1, 0], [data[1][s_1][1], data[1][s_1][2]], [0, 0], extra_data
        if sorted_list[0] == sorted_list[1]:
            salesM = sorted_list[0]
            s_2 = sales_list[sales_list.index(salesM) + 1:].index(salesM) + sales_list.index(salesM) + 1
        else:
            s_2 = sales_list.index(sorted_list[1])

        return data[0], [s_1, s_2], [data[1][s_1][1], data[1][s_1][2]], [data[1][s_2][1], data[1][s_2][2]], extra_data

    def setup_target_sheet_init(self):
        self.doc = openpyxl.load_workbook(SW.t_file_dir + "/" + SW.filename + ".xlsx")
        self.ws = self.doc.active
        self.ws['H1'] = "사진1"
        self.ws['I1'] = "사진2"
        self.ws['J1'] = "링크1"
        self.ws['K1'] = "링크2"
        self.ws['L1'] = "구매수/가격1"
        self.ws['M1'] = "구매수/가격2"
        self.ws['N1'] = "타오바오 상품명"

        self.doc.save(SW.t_file_dir + "/" + SW.filename + ".xlsx")

    @staticmethod
    def extract_image(cell, sheet):  # openpyxl_image_loader.SheetImageLoader
        image_loader = SheetImageLoader(sheet)
        image = image_loader.get(cell)
        ts = str(datetime.datetime.now().timestamp())
        rgb_image = image.convert("RGB")
        rgb_image.save(os.getcwd() + rf"\temp\img_{ts}.jpg")
        del image, rgb_image, image_loader
        return f"file:///{os.getcwd()}/temp/img_{ts}.jpg", os.getcwd() + rf"\temp\img_{ts}.jpg", f"img_{ts}.jpg"

    @staticmethod
    def copy_file():
        shutil.copy(SW.o_file_dir, SW.t_file_dir + "/" + SW.filename + ".xlsx")
