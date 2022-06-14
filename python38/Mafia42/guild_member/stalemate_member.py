import requests
import tkinter as tk
import datetime
import tkinter.font as tkfont

# Previous Modified Date: 2022/03/09
# Modified Date: 2022/06/10
# 스테일메이트 길원관리 v3.7
version = '3.7'

# 현재는 길원 아이디 리스트를 직접 업데이트 해줘야 함 (추가만 해도 됨)

memberlist = [4580329, 63058380, 106496216, 361215476, 30097564,  # 일반 길드원 (Update 시마다 새로운 줄에 추가 멤버 닉네임 작성)
              3716221, 28687294, 69634984, 24140787, 15343494, 8872082,
              105704067, 21697307, 105565785, 106174400, 17151257, 24064761,
              15529530, 487552, 23758405, 12210194, 46486002, 356794670, 7512887,
              403180267, 362085, 3826195, 84524061, 26956551, 22249579, 1027754406,
              30593146, 390469814, 497678063, 73553423, 5303788, 69878702,
              409476413, 1065308531, 30593146, 70242975, 71054491, 14013372, 60080884,  # 220122 향기, 열효율, 꽁땅지, 빱, 체인, 케넨, 나는누굴까욤 (펠담은 전투원으로 임시조치)
              1027826564, 73730418, 103386247, 70539990, 11240880, 83615106, 63149909, 23041744,  # 220226 곰반죽, 단지, 댕이, 수학SH, 오예우, 준법시민42, 졲발, 포항식칼
              409509258, 2396642, 11240880, 1065783508, 1065591738,  # 220309 쎈장, 얼의남자친구, 오예우, 명월보름냥, 파리파리날파
              70790213, 107303736, 561265491, 561266286, 178614361,  # 220329 세구님, 냐옹데스까, 맢168, 청록영, 글카
              10851195, 27273340, 1065470180, 61227866, 193718979, 105565785,  # 220610 1일정지, HONGLU, K잼사냥꾼, 냥냥한강쥐, 땐, 루하테니조
              75341853, 63373460, 77274710, 107697104, 17711570, 758047809,  # 220610 묻어버리게쪙, 백한, 온섬, 이둬, 주사
              63115546, 560040513, 575952678, 107305098, 22238401, 22223715, 1065948212]  # 220610 편색, 풋딩, 픙, 필살, 희철, 덪지, 08LiF

memberlist = list(set(memberlist))  # 중복제거 위함
managerlist = [83611662, 76136895, 31588347, 68043957, 66474671]  # 운영진 // 220122 온새 추가 // 220329 믈 추가

master = [14014488]  # 마스터

data = ['NICKNAME', 'guild_id', 'rankpoint', 'fame', 'win_count', 'lose_count', 'EXPERIENCE']
temp1 = []
output = ''


def fetchinfo(userid):
    global temp1, data

    payload = {'id': f'{userid}'}
    reqraw = requests.post('https://mafia42.com/api/user/user-info', data=payload)
    req = reqraw.content.decode('utf-8', 'replace')

    for each in data:
        tempdata = req[req.index(each) + len(each) + 2:req[req.index(each) + len(each) + 2:].index(',') + len(req[:req.index(each) + len(each) + 2])]
        temp1.append(tempdata)


def analyze():
    global temp1, output, number
    temp2 = []
    temp3 = []
    temp4 = []

    for i in range(0, len(temp1), 7):  # 뽑아올 데이터 개수
        temp2.append([temp1[i], temp1[i + 1], temp1[i + 2], temp1[i + 3], temp1[i + 4], temp1[i + 5], temp1[i + 6]])

    temp1 = []

    for i in temp2:
        if i not in temp3:
            temp3.append(i)

    for [a, b, c, d, e, f, g] in temp3:  # 'NICKNAME', 'guild_id', 'rankpoint', 'fame', 'win_count', 'lose_count', 'EXPERIENCE'
        if b == '42271':  # Stalemate's guild_id
            name = a[1:len(a) - 1]
            games = int(float(e)) + int(float(f))
            temp4.append([name, c, d, games])
            number += 1

    temp4.sort()

    for [a, b, c, d] in temp4:
        output = f"""{output}{a} {b} {c} {d}\n"""


def outputwindow():
    global output, version, number

    window = tk.Tk()
    title = 'SMGM v%s' % version
    window.title(title)
    window.geometry('240x740')
    textheight = number + 1
    text = tk.Text(window, height=textheight)
    text.pack()

    font = tkfont.Font(family="Malgun Gothic", size=10)
    text.configure(font=font)
    text.insert(1.0, output)

    window.mainloop()


def run(x):
    for member in x:
        fetchinfo(member)

    analyze()


number = 0

run(master)
run(managerlist)
run(memberlist)

output = f'''{output}최종 업데이트: {datetime.datetime.now()}'''
output = output[:len(output) - 7]

outputwindow()
