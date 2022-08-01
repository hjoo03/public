import os, openpyxl, requests


def change_link(link):
    while True:
        try:
            r = requests.get(link)
            break
        except requests.exceptions.ConnectionError:
            pass
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
                l = change_link(a)
                cellObj.value = l
                cellObj.hyperlink = l
                cellObj.style = "Hyperlink"
                print(f"{cnt}: {l}")
                cnt += 1
                
    doc.save("R_"+file)
    print("saved")
