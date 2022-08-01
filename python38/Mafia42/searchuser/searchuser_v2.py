# -*- coding: utf-8 -*-

import requests, json, sys, datetime, sqlite3, os
import pandas as pd
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic

from main import Ui_MainWindow
from sub import Ui_SubWindow

version = '2.4'

# Patch Notes
###########################################################################
# 2.3
# Added Exception for wrong SQL Password
# Added DB Update warning when usernames not accord with each other
# Simplified Source Code
# 2.4 (2022/08/01)
# uses sqlite to run without sql installed
# integrated ui files to the code
# Put db files to the following path: {os.getcwd()}\source\
###########################################################################
# Last Updated : 2022/08/01 23:57 +09


class Sql:
    """
    def __init__(self):
        self.cursor = Win.user_db.cursor(pymysql.cursors.DictCursor)

    def search_id(self, string):
        global validity
        statement = f"SELECT DISTINCT nickname, id FROM {Win.table} WHERE nickname = '{string}'"
        self.cursor.execute(statement)

        try:
            idData = self.cursor.fetchall()[0]
            return idData

        except IndexError:
            validity = False
            return
    """
    def __init__(self) -> None:
        for file in os.listdir("source\\"):
            if ".db" in file:
                db = file
        self.conn = sqlite3.connect("source\\" + db)
        self.database = db
        db_name = "userdata"
        d = pd.read_sql(f"SELECT * FROM {db_name}", self.conn)
        self.data = d.set_index("index")
        
    def search_id(self, nickname: str) -> int:  # TODO: Return results even when the cases don't match (Use .upper or .lower)
        df = self.data
        try:
            user_id = df[df.nickname == nickname].iloc[0].id
            return {"id": user_id, "nickname": nickname}
        except IndexError:
            try:
                user_id = df[df.nickname == nickname].iloc[0].id
                return {"id": user_id, "nickname": nickname}
            except IndexError:
                return 0            

# noinspection PyArgumentList
class MainWindow(QMainWindow, Ui_MainWindow):
    global validity

    def __init__(self):
        global validity

        super().__init__()
        self.setupUi(self)
        self.data_info()
        self.win2 = None
        validity = False
        self.id = ""
        self.nickname = ""
        self.data = {}
        self.output_data = ""
        self.datatype = 0
        self.onlyInt = QIntValidator()

        self.idinput.setValidator(self.onlyInt)

        self.datatype_dict = {0: None, 1: "ID", 2: "nickname", 3: "Refresh"}

        """
        f = open("settings.txt")
        settings = f.readlines()
        user = settings[1][5:].strip()
        password = settings[2][9:].strip()
        self.table = settings[5][9:].strip()

        try:
            self.user_db = pymysql.connect(
                user=user,
                password=password,
                host="127.0.0.1",
                db="mafia42",
                charset="utf8"
            )
            self.output(f"Connected to SQL Database; Table: '{self.table}'")
        except pymysql.err.OperationalError:
            self.warning_error07()
            exit()
        f.close()
        """
        self.Sql = Sql()
        self.output(f"Connected to Database; Database: {self.Sql.database}")
        
        self.output(f"Mafia42 User Search Client v{version}")
        self.idinput.textChanged.connect(self.fetch_id)
        self.nickinput.textChanged.connect(self.fetch_nickname)
        self.searchbtn.clicked.connect(self.analyze)  # button triggers analyze()

    def analyze(self, refresh):
        global validity, last_fetch

        if not refresh:
            if self.id and self.nickname:
                self.warning_error01()
                return

            if not self.id and not self.nickname:
                self.warning_error02()
                return

            input_data, self.datatype = (self.id, 1) if self.id else (self.nickname, 2)

            if not self.datatype:
                self.warning_error05()
                return

            if self.datatype == 1:
                pass

            else:
                try:
                    sql_data = self.Sql.search_id(input_data)
                    input_data, db_nickname = sql_data['id'], sql_data['nickname']

                except TypeError:
                    validity = False
                    self.warning_error06(self.nickname)
                    return

            self.data = self.check(input_data)

            if not validity:
                return
            validity = False
            self.output_data = ""
            if self.datatype == 2:
                if self.data['NICKNAME'] != db_nickname:
                    self.warning_warn01(self.data['NICKNAME'], db_nickname)

            last_fetch = input_data

        else:
            self.output_data = ""
            payload = {'id': last_fetch}
            r = requests.post("https://mafia42.com/api/user/user-info", data=payload)
            res = json.loads(r.text)
            self.data = res['userData']
            self.datatype = 3

        self.advanced_info()

        for item in fetch_data:
            self.output_data += f"{item}: {self.data[item]}\n"

        self.output_data += f"Timestamp: {self.time()}"

        self.output(f"[{self.time()}] Fetched {self.data['NICKNAME']} (Type: {self.datatype_dict[self.datatype]})")

        self.win2 = SubWindow()

    def check(self, arg):
        global validity

        if not arg:
            self.warning_error09()
            return

        payload = {'id': arg}
        r = requests.post("https://mafia42.com/api/user/user-info", data=payload)

        if r.status_code == 500:
            self.warning_error03(arg)
            validity = False
            return

        try:
            res = json.loads(r.text)
            validity = True
            return res['userData']

        except json.decoder.JSONDecodeError:
            self.warning_error04()
            validity = False
            return

    def fetch_id(self):
        self.id = self.idinput.text()

    def fetch_nickname(self):
        self.nickname = self.nickinput.text()

    def warning_error01(self):
        QMessageBox.warning(self, "[E01] ValueError", "Too Many Input Values!")

    def warning_error02(self):
        QMessageBox.warning(self, "[E02] ValueError", "No Input Value!")

    def warning_error03(self, arg):
        QMessageBox.warning(self, "[E03] Response 500", "No such id: %s !" % arg)

    def warning_error04(self):
        QMessageBox.warning(self, "[E04] JSONDecodeError", "Unknown Error! Check source code for more information.")

    def warning_error05(self):
        QMessageBox.warning(self, "[E05] DataTypeError", "Unknown Error! Check source code for more information.")

    def warning_error06(self, arg):
        QMessageBox.warning(self, "[E06] ValueError", "No such user: %s !" % arg)

    def warning_error07(self):
        QMessageBox.warning(self, "[E07] SQL Operational Error", "Check SQL Password!")

    def warning_error08(self):
        QMessageBox.warning(self, "[E08] Validity Error", "Unknown Error! Check source code for more information.")

    def warning_error09(self):
        QMessageBox.warning(self, "[E09] TypeError", "MainWindow.check() missing 1 required argument: int id")

    def warning_warn01(self, arg1, arg2):
        QMessageBox.warning((self, "[W01] Database Alert", "Database and Server doesn't match(%s, %s)" % arg1, arg2))

    def output(self, msg):
        self.console.append(msg)

    def output_clear(self):
        self.console.clear()

    def keyPressEvent(self, k):
        if k.key() == Qt.Key_Return:
            self.analyze(0)

    @staticmethod
    def time():
        return str(datetime.datetime.now())[:len(str(datetime.datetime.now()))-7]

    @staticmethod
    def data_info():
        global fetch_data, guild_position, frame, death_cause, nametag, gem, gem_level

        fetch_data = ['ID', 'NICKNAME', 'fame', 'rankpoint', 'LUNA', 'MONEY', 'EXPERIENCE', 'nickname_color',
                      'current_gem',
                      'frame', 'current_nametag', 'current_collection', 'lastlogin_time', 'introduce', 'death_cause',
                      'win_count', 'lose_count', 'max_friend', 'banned_time', 'is_use_death_cause', 'guild_id',
                      'guild_name',
                      'guild_initial', 'guild_level', 'guild_point', 'guild_initial_color', 'has_new_friend_chat',
                      'current_skin', 'collection2', 'current_collection2', 'current_collection3', 'rankpoint2',
                      'EXPERIENCE2',
                      'MONEY2', 'collection', 'gem', 'emoticon', 'skin', 'nametag', 'tmp_int1', 'tmp_int2']
        guild_position = {'null': 'null', '2': '길드원', '3': '전투원', '4': '운영진', '5': '마스터'}
        frame = {1: '기본 테두리', 2: '은 테두리', 3: '금 테두리', 4: '백금 테두리', 7: '마스터 테두리',
                 10: '뱀파이어 테두리 (낮은 확률로 명성 차감 엽서 보낼 때 차감량 증가)', 11: '루돌프 테두리 (명성 대량 상승 엽서 상승량 증가)',
                 12: '카네이션 테두리 (마엽 받을 때 기간 10% 감소)', 13: '삼각자 테두리 (마엽 보낼 때 기간 10% 증가)',
                 14: '토끼 테두리 (낮은 확률로 명성 상승 엽서 상승량 증가)',
                 16: '얼음 테두리 (명성 차감 엽서 받을 시 기간 감소)',
                 18: '추억의 필름 (엽서를 보낼 때 경험치 증가)',
                 23: '다이아몬드 테두리 (시민팀 보석 확률 증가)',
                 26: '메이드의 해골 (명성 차감 엽서 보낼 시 기간 증가)',
                 28: '눈의 결정 테두리 (제련 소모 루블 감소)',
                 29: '이무기의 집착 (명성 대량 차감 엽서 보낼 시 차감량 증가)', 30: '접근 금지선 테두리 (명성 대량 차감 엽서 받을 때 차감량 감소)',
                 33: '타락한 깃털 (명성 차감 엽서 보낼 시 기간 증가)', 34: '코기코기 테두리 (엽서를 보낼 때 경험치 증가)',
                 36: '결사대원의 후드 (명성 차감 엽서 받을 시 기간 감소)',
                 45: '신목 조각 테두리 (제련 소모 루블 감소)', 46: '승천 테두리 (엽서 보낼 때 300루블 획득)',
                 47: '지름신 테두리 (엽서를 보낼 때 300루블 획득)', 58: '우주복 헬멧 테두리 (명성 차감 엽서 받을 때 기간 감소)',
                 62: '겨울 경찰 테두리 (명성 대량 증가 엽서 보낼 시 +1)',
                 63: '흑호랑단 테두리 (명성 대량 차감 엽서 차감량 증가)', 64: '기복 테두리 (낮은 확률로 명성 상승 엽서 보낼 때 상승량 증가)'}
        death_cause = {0: '사망확인서 미사용', 1: '기본 사망확인서 사용', 2: '부고 기사 사용', 3: '사망광고판 사용'}
        nametag = {1171: '기본 명패', 1156: '은으로 만든 표식', 131: '신비한 합창', 17: '광전사의 피 (RP 상승량 증가)', 16: '금강석 방패 (RP 하락량 감소)',
                   24: '가능성의 떡잎 (게임 경험치 증가)', 25: '행운의 금화 (게임 루블 획득 증가)', 27: '투명 명패', 30: '황금알을 낳는 거위 (출석 시 루블 지급)',
                   41: '조율자의 천칭 (RP 상승 증가, 하락 감소)', 58: '사치스런 장신구 (결제시 루블 지급)', 80: '검은 마녀의 저주 (투표 대상 최후의 반론 시간 감소)',
                   214: '웨딩 스톤 (연인 배정 확률 보조)', 328: '교육자의 영광 (초보 채널 접속 가능)', 871: '충성스러운 백사의 명패 (도배 제한 완화)',
                   1113: 'Trick or Treat! (시간 증가/감소 강화)', 1313: '패쇄된 호실의 기록 (도배 제한 완화)', 1170: '축신의 갑주 (RP 상승/하락 감소)',
                   1169: '선계의 기둥 (RP 상승 증가, 하락 감소)', 1360: '말린 장미 회랑 (RP 상승 증가, 하락 감소)'}
        gem_level = ['원석', '영롱한 원석', '하급', '영롱한 하급', '중급', '영롱한 중급', '상급', '영롱한 상급', '최상급', '영롱한 최상급',
                     '장인급', '영롱한 장인급', '기적급', '영롱한 기적급', '15강', '16강 (풀강)']
        gem = {115: '테러리스트', 110: '기자', 113: '사립탐정', 106: '영매', 102: '의사', 107: '군인', 103: '스파이', 100: '마피아',
               129: '해커', 121: '판사', 126: '마술사', 111: '짐승인간', 125: '자경단원', 123: '간호사', 130: '심리학자', 109: '연인',
               133: '공무원', 101: '경찰', 114: '도굴꾼', 128: '과학자', 112: '건달', 132: '용병', 124: '교주', 122: '도둑',
               120: '예언자', 118: '성직자', 116: '마담', 127: '마녀', 108: '정치인'}

    def advanced_info(self):
        try:
            self.data['guild_level'] = str(
                self.data['guild_level']) + f" ({guild_position[str(self.data['guild_level'])]})"
        except KeyError:
            self.data['guild_level'] = str(self.data['guild_level']) + " (Unknown)"

        try:
            self.data['frame'] = str(self.data['frame']) + f" ({frame[int(self.data['frame'])]})"
        except KeyError:
            self.data['frame'] = str(self.data['frame']) + " (Unknown)"

        try:
            self.data['is_use_death_cause'] = str(
                self.data['is_use_death_cause']) + f" ({death_cause[int(self.data['is_use_death_cause'])]})"
        except KeyError:
            self.data['is_use_death_cause'] = str(self.data['is_use_death_cause']) + " (Unknown)"

        try:
            self.data['current_nametag'] = str(
                self.data['current_nametag']) + f" ({nametag[int(self.data['current_nametag'])]})"
        except KeyError:
            self.data['current_nametag'] = str(self.data['current_nametag']) + " (Unknown)"

        try:
            gem_ = gem[int(str(self.data['current_gem'])[0:3])] + ' / ' + gem_level[
                int(str(self.data['current_gem'])[3:5]) - 1]
            self.data['current_gem'] = gem_
        except KeyError:
            self.data['current_gem'] = str(self.data['current_gem']) + " (미장착)"
        except ValueError:
            self.data['current_gem'] = str(self.data['current_gem']) + " (Unknown)"
        color_code = 16777216 + self.data['nickname_color']
        hex_code = "%.6X" % color_code
        red = "%d" % int(hex_code[0:2], 16)
        green = "%d" % int(hex_code[2:4], 16)
        blue = "%d" % int(hex_code[4:6], 16)
        self.data['nickname_color'] = f"{hex_code} (R: {red}/G: {green}/B: {blue})"
        if self.data['fame']*0.015 <= 20:
            self.data['fame'] = str(self.data['fame']) + f" (권위의 엽서: -20)"
        else:
            self.data['fame'] = str(self.data['fame']) + f" (권위의 엽서: {int((-1)*self.data['fame']*0.015 - 20)})"


class SubWindow(QMainWindow, Ui_SubWindow):
    def __init__(self):  # noinspection PyArgumentList
        super().__init__()
        self.setupUi(self)
        self.show()
        self.textBrowser.append(Win.output_data)

    def keyPressEvent(self, k):
        if k.key() == Qt.Key_F5:
            self.close()
            Win.analyze(1)

        elif k.key() == Qt.Key_Escape or Qt.Key_Return:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Win = MainWindow()
    Win.show()
    app.exec_()
