import requests, datetime
import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox

# Created Date: 2022/01/22
# Latest Modified Date: 2022/03/07 16:43

version = 3.4

fetch_data = ['NICKNAME', 'guild_id', 'rankpoint', 'fame', 'win_count', 'lose_count', 'EXPERIENCE',
              'EXPERIENCE2', 'LUNA', 'MONEY', 'MONEY2', 'banned_time', 'collection',
              'collection2', 'current_collection', 'current_collection2', 'current_collection3',
              'current_gem', 'current_nametag', 'current_skin', 'emoticon', 'rankpoint2',
              'frame', 'gem', 'guild_initial', 'ID', 'guild_initial_color',
              'guild_level', 'guild_name', 'guild_point', 'has_new_friend_chat', 'skin',
              'is_use_death_cause', 'lastlogin_time', 'max_friend', 'nametag', 'nickname_color',
              'tmp_int1', 'tmp_int2']
output = ''

guild_position = {'null': 'null', '2': '길드원', '3': '전투원', '4': '운영진', '5': '마스터'}

frame = {1: '기본 테두리', 2: '은 테두리', 3: '금 테두리', 4: '백금 테두리', 7: '마스터 테두리',
         10: '뱀파이어 테두리 (낮은 확률로 명성 차감 엽서 보낼 때 차감량 증가)', 11: '루돌프 테두리 (명성 대량 상승 엽서 상승량 증가)',
         12: '카네이션 테두리 (마엽 받을 때 기간 10% 감소)', 13: '삼각자 테두리 (마엽 보낼 때 기간 10% 증가)',
         14: '토끼 테두리 (낮은 확률로 명성 상승 엽서 상승량 증가)',
         16: '얼음 테두리 (명성 차감 엽서 받을 시 기간 감소)',
         18: '추억의 필름 (엽서를 보낼 때 경험치 증가)',
         23: '다이아몬드 테두리 (시민팀 보석 확률 증가)', 28: '눈의 결정 테두리 (제련 소모 루블 감소)',
         29: '이무기의 집착 (명성 대량 차감 엽서 보낼 시 차감량 증가)', 30: '접근 금지선 테두리 (명성 대량 차감 엽서 받을 때 차감량 감소)',
         33: '타락한 깃털 (명성 차감 엽서 보낼 시 기간 증가)', 34: '코기코기 테두리 (엽서를 보낼 때 경험치 증가)',
         36: '결사대원의 후드 (명성 차감 엽서 받을 시 기간 감소)',
         45: '신목 조각 테두리 (제련 소모 루블 감소)', 46: '승천 테두리 (엽서 보낼 때 300루블 획득)',
         47: '지름신 테두리 (엽서를 보낼 때 300루블 획득)', 58: '우주복 헬멧 테두리 (명성 차감 엽서 받을 때 기간 감소)',
         62: '겨울 경찰 테두리 (명성 대량 증가 엽서 보낼 시 +1)',
         63: '흑호랑단 테두리 (명성 대량 차감 엽서 차감량 증가)', 64: '기복 테두리 (낮은 확률로 명성 상승 엽서 보낼 때 상승량 증가)'}

death_cause = {0: '사망확인서 미사용', 1: '기본 사망확인서 사용'}


def check(no):
    global validity

    payload = {'id': f'''{no}'''}
    reqraw = requests.post('https://mafia42.com/api/user/user-info', data=payload)

    if str(reqraw) == '<Response [500]>':
        validity = False

    else:
        validity = True


def fetch(no):
    global fetch_data, output

    payload = {'id': no}
    reqraw = requests.post('https://mafia42.com/api/user/user-info', data=payload)
    req = reqraw.content.decode('utf-8', 'replace')
    temp1 = []

    for x in fetch_data:
        tempdata = req[req.index(f'''{x}''') + len(x) + 2:req[req.index(f'''{x}''') + len(x) + 2:].index(',') + len(req[:req.index(f'''{x}''') + len(x) + 2])]
        temp1.append(tempdata)

    temp1.append(req[req.index('"guild_initial_background_color"') + 33:][:req[req.index('"guild_initial_background_color"') + 33:].index('}')])

    # 특수문자 하트가 tkinter 창 응답없음을 유발하기 때문에 제거
    reqtemp = req[req.index('"introduce"') + 13:][:req[req.index('"introduce"') + 13:].index('"is_use') - 2]

    try:
        reqtemp = reqtemp.replace('ᰔ', '♡')  # 하트 1

    except ValueError:
        pass

    try:
        reqtemp = reqtemp.replace('ᩚ', '♡')  # 하트 2

    except ValueError:
        pass

    temp1.append(reqtemp)

    reqtemp = req[req.index('"death_cause"') + 15:][:req[req.index('"death_cause"') + 15:].index('"tmp_int') - 2]

    try:
        reqtemp = reqtemp.replace('ᰔ', '♡')  # 하트 1

    except ValueError:
        pass

    try:
        reqtemp = reqtemp.replace('ᩚ', '♡')  # 하트 2

    except ValueError:
        pass

    temp1.append(reqtemp)

    # Additional Information
    level = guild_position[temp1[27]]

    try:
        frameinfo = frame[int(temp1[22])]

    except KeyError:
        frameinfo = 'Unknown'

    try:
        deathcauseinfo = death_cause[int(temp1[32])]

    except KeyError:
        deathcauseinfo = 'Unknown'

    timestamp = str(datetime.datetime.now())[:len(str(datetime.datetime.now())) - 7]

    def nullshow(indexlist):
        for index in indexlist:
            if temp1[index] == 'null':
                temp1[index] = ' null '

    nullshow([28, 24])

    nicknamecolorraw = 16777215 + int(str(temp1[36])) + 1
    nicknamecolor = "%.6X" % nicknamecolorraw
    redcolor = '%d' % int(nicknamecolor[0:2], 16)
    greencolor = '%d' % int(nicknamecolor[2:4], 16)
    bluecolor = '%d' % int(nicknamecolor[4:6], 16)

    output = f'''<Basic Information>\nID: {temp1[25]}\nnickname: {temp1[0][1:len(temp1[0])-1]}\nfame: {temp1[3]} (권위의 엽서: -{int(int(temp1[3])*0.018+20)})\nrankpoint: {temp1[2]}\nexperience: {temp1[6]}\nmoney: {temp1[9]}\nluna: {temp1[8]}\nnickname color: {nicknamecolor} (R: {redcolor}/G: {greencolor}/B: {bluecolor})\nintroduce: {temp1[40]}\ndeath cause: {temp1[41]}
<Guild Information>\nguild name: {temp1[28][1:len(temp1[28])-1]}\nposition: {temp1[27]} ({level})\nguild point: {temp1[29]}\nguild initial: {temp1[24][1:len(temp1[24])-1]}\nguild id: {temp1[1]}\nguild color: {temp1[26]}\nguild backcolor: {temp1[39]}
<Advanced Information>\nlast login: {temp1[33][1:len(temp1[33])-1]}\nmax friend: {temp1[34]}\nwin: {temp1[4]}\nloss: {temp1[5]}\nlast ban: {temp1[11][1:len(temp1[11])-1]}\ncurrent collection: {temp1[14][1:len(temp1[14])-1]}\ncurrent gem: {temp1[17][1:len(temp1[17])-1]}\ncurrent nametag: {temp1[18]}\ncurrent skin: {temp1[19][1:len(temp1[19])-1]}\nframe: {temp1[22]} ({frameinfo})\ndeath cause usage: {temp1[32]} ({deathcauseinfo})\nnew friend chat: {temp1[30]}\nexperience2: {temp1[7]}\nmoney2: {temp1[10]}\ncollection: {temp1[12]}\ncollection2: {temp1[13]}\ncurrent collection2: {temp1[15]}
current collection3: {temp1[16]}\nemoticon: {temp1[20]}\nrankpoint2: {temp1[21]}\ngem: {temp1[23][1:len(temp1[23])-1]}\nskin: {temp1[31]}\nnametag: {temp1[35]}\ntmp_int1: {temp1[37]}\ntmp_int2: {temp1[38]}\nTimestamp: {timestamp}'''


def outputwindow():
    global version, output, win

    win = tk.Tk()
    title = 'Userdata Fetch Client v%s' % version
    win.title(title)
    win.geometry('450x700')
    textheight = len(fetch_data) + 7

    text = tk.Text(win, height=textheight)
    text.pack()
    font = tkfont.Font(family="Malgun Gothic", size=9)
    text.configure(font=font)
    text.insert(1.0, output)
    text.tag_add('title', '1.0', '1.30')
    text.tag_add('title', '12.0', '12.30')
    text.tag_add('title', '20.0', '20.30')
    text.tag_config('title', foreground='red')

    lengthlist = [30, 4, 10, 6, 11, 12, 7, 6, 16, 11, 13, 30, 12, 10, 13, 15, 10, 13, 17, 30, 12, 12, 5,
                  6, 10, 20, 13, 17, 14, 7, 18, 17, 13, 8, 12, 13, 21, 21, 10, 12, 5, 6, 9, 10, 10, 11]

    def texttag(line, length):
        text.tag_add('info', f'''{line}.{length}''', f'''{line}.100''')

    count = 1
    for i in lengthlist:
        texttag(count, i)
        count += 1

    text.tag_config('info', foreground='blue')
    win.bind('<F5>', run)
    win.mainloop()


def confirminput(event):
    inputid = entry.get()

    if inputid == '':
        tkinter.messagebox.showerror(title='Error', message='Input Not Detected!')

    else:

        check(inputid)

        if not validity:
            tkinter.messagebox.showerror(title='Error', message='Invalid ID! (Response 500)')

        else:
            w.destroy()
            fetch(inputid)
            outputwindow()


def run(init):
    global version, w, entry

    try:
        win.destroy()

    except (tkinter.TclError, NameError):
        pass

    w = tk.Tk()
    title = 'Userdata Fetch Client v%s' % version
    w.title(title)
    w.geometry('320x50')
    entry = tk.Entry(w)
    font = tkfont.Font(family="Malgun Gothic", size=10)
    entry.configure(font=font)
    entry.pack()
    btn = tk.Button(w, height=1, width=10, text="Confirm", command=lambda: confirminput(btn))
    btn.pack()
    w.bind('<Return>', lambda event: confirminput(event))
    w.mainloop()


# Trigger Function
run(None)
