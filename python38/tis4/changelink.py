import os
import time

import requests
import openpyxl


def change_link(link):
    while True:
        try:
            r = requests.get(link)
            break
        except requests.exceptions.ConnectionError:
            pass
        print("Got ConnectionError; Sleeping for 30 secs")
        time.sleep(30)
    r.encoding = 'utf-8'
    res = r.text
    d = res[res.index(r"var url = '")+11:]
    e = d.index("&pri")
    f = d[:e]
    return f


files = os.listdir("input\\")
for file in files:
    print(file)
    doc = openpyxl.load_workbook("input\\" + file)
    ws = doc.active
    for col in (10, 11):
        cnt = 1
        for cellObj in list(ws.columns)[col]:
            a = str(cellObj.value)
            if "링크" not in a and "m.tb.cn" in a:
                while True:
                    try:
                        l = change_link(a)
                        break
                    except ValueError:
                        print("Got Captcha Penalty; Sleeping for 5 mins")
                        time.sleep(300)
                cellObj.value = l
                cellObj.hyperlink = l
                cellObj.style = "Hyperlink"
                print(f"{cnt}: {l}")
                cnt += 1

    doc.save("R_"+file)
    print("saved")
