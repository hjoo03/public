import requests, ray, time, json, sqlite3
import pandas as pd
from datetime import datetime, timedelta

# Latest Modified Date : 2022/08/02
# Mafia42 userdb fetcher


version = "2.3"

end = int(json.loads(requests.post("https://mafia42.com/board/get-lastDiscussion",
                                   json={"articles": {"page": 0}}).text)["articleData"][0]["article_id"]) + 1

f = open("settings.txt", 'r')
settings = f.readlines()
last_fetch = int(settings[8][11:].strip())
print("last_fetch=", last_fetch)
f.close()

f = open("userlist.txt", 'r')
ul = f.readlines()
userlist = []
for item in ul:
    userlist.append(int(item[:-1]))
f.close()
total = end - last_fetch + 1 + len(userlist)
date = str(datetime.now())[5:7] + str(datetime.now())[8:10]
main_output = []
split1 = []
split2 = []
old_users = []
new_users = []
if end - last_fetch <= 20000:
    split2.append((last_fetch, end))

else:
    i = last_fetch
    while True:
        split2.append((i, i + 19999))

        if end - i < 40000:
            split2.append((i + 20000, end))
            break

        i += 20000

if len(userlist) <= 20000:
    split1.append((0, len(userlist)-1))
else:
    i = 0
    while True:
        split1.append((i, i + 19999))

        if len(userlist)-1 - i < 40000:
            split1.append((i + 20000, len(userlist)-1))
            break
        i += 20000

ray.init(num_cpus=8)


def timestamp():
    return str(datetime.now())[:len(str(datetime.now())) - 7]


@ray.remote
def fetch(article_id):
    try:
        r = requests.get(f"https://mafia42.com/api/show-lastDiscussion/{article_id}")

    except OSError:
        print(f"[ERROR][{timestamp()}] OSError: letting server rest")
        time.sleep(30)
        r = requests.get(f"https://mafia42.com/api/show-lastDiscussion/{article_id}")

    except requests.exceptions.ConnectionError:
        print(f"[ERROR][{timestamp()}] requests.exceptions.ConnectionError: letting server rest")
        time.sleep(10)
        r = requests.get(f"https://mafia42.com/api/show-lastDiscussion/{article_id}")

    res = json.loads(r.text)
    if res['responseCode'] == 6:
        return res['boardData']['nickname'], res['boardData']['user_id']
    else:
        return


@ray.remote
def fetch_old(user_id):
    payload = {"id": user_id}
    try:
        r = requests.post(f"https://mafia42.com/api/user/user-info", data=payload)

    except OSError:
        print(f"[ERROR][{timestamp()}] OSError: letting server rest")
        time.sleep(30)
        r = requests.post(f"https://mafia42.com/api/user/user-info", data=payload)

    except requests.exceptions.ConnectionError:
        print(f"[ERROR][{timestamp()}] requests.exceptions.ConnectionError: letting server rest")
        time.sleep(10)
        r = requests.post(f"https://mafia42.com/api/user/user-info", data=payload)

    try:
        res = json.loads(r.text)
        return res['userData']['NICKNAME'], res['userData']['ID']

    except json.decoder.JSONDecodeError:
        return None


def main(x, y):
    global cnt
    starttime = datetime.now()
    results = [fetch.remote(x) for x in range(x, y)]

    while len(results):
        done, results = ray.wait(results)
        cnt += 1

        if cnt % 5000 == 0:
            print(f"[DEBUG][{timestamp()}] main(): {cnt} fetched")

        data = ray.get(done[0])
        if data:
            if len(data) == 2:
                if str(data[1]) not in userlist:
                    new_users.append(data)
                    file = open("userlist.txt", 'a')
                    file.write(str(data[1])+"\n")
                    file.close()

    cnt += 1
    endtime = datetime.now()
    ups = round((y - x + 1) / (endtime - starttime).seconds, 1) if endtime - starttime != 0 else 0
    estimatedmin = round((total - cnt)/ups/60, 1) if ups != 0 else 0
    ett = str(datetime.now() + timedelta(minutes=estimatedmin))
    print(f"[DEBUG][{timestamp()}] partial fetch complete ({ups} users/sec, {estimatedmin} mins remaining)")
    print(f"[INFO][{timestamp()}] estimated endtime: {ett[:len(ett)-7]}")
    ray.shutdown()


def main_old(x, y):
    global cnt
    starttime = datetime.now()
    results = [fetch_old.remote(userlist[x]) for x in range(x, y)]

    while len(results):
        done, results = ray.wait(results)
        cnt += 1

        if cnt % 5000 == 0:
            print(f"[DEBUG][{timestamp()}] main_old(): {cnt} fetched")
        data = ray.get(done[0])

        if data:
            if len(data) == 2:
                old_users.append(data)

    cnt += 1
    endtime = datetime.now()
    ups = round((y - x + 1) / (endtime - starttime).seconds, 1) if endtime - starttime != 0 else 0
    estimatedmin = round((total - cnt) / ups / 60, 1) if ups != 0 else 0
    ett = str(datetime.now() + timedelta(minutes=estimatedmin))
    print(
        f"[DEBUG][{timestamp()}] partial fetch complete ({ups} users/sec, {estimatedmin} mins remaining)")
    print(f"[INFO][{timestamp()}] estimated endtime: {ett[:len(ett) - 7]}")
    ray.shutdown()


class Sql:
    def __init__(self):
        self.date = str(datetime.now().date()).replace("-", "")[2:]
        self.conn = sqlite3.connect(f"userlist_{self.date}.db")
        self.df = pd.DataFrame({"id": "", "nickname": ""}, index=range(0, 1))
    
    def insert(self, data):
        nickname_list = []
        id_list = []
        for (nickname, user_id) in data:
            nickname_list.append(nickname)
            id_list.append(user_id)
        data_to_insert = {"id": id_list, "nickname": nickname_list}
        df_to_insert = pd.DataFrame(data_to_insert, index=range(0, len(data)))
        self.df = pd.concat([self.df, df_to_insert])

    @staticmethod
    def update():
        file = open("settings.txt", 'w')
        for count, line in enumerate(settings):
            if count != 8:
                file.write(line)
            else:
                file.write(f"last_fetch={end}")
        file.close()

    def save(self):
        d = self.df
        try:
            df = d if not d.drop_duplicates() else d.drop_duplicates()
        except ValueError:
            df = d
        df.to_sql("userdata", self.conn)
        
sql = Sql()
cnt = 1
print(f"[{timestamp()}] Fetch Initiated")
for (s, e) in split1:
    if __name__ == "__main__":
        main_old(s, e)
sql.insert(old_users)

for (s, e) in split2:
    if __name__ == "__main__":
        main(s, e)
sql.insert(new_users)
sql.save()
sql.update()
print(f"[{timestamp()}] fetchuser_v2 Complete!")
