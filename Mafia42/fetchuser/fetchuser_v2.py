import requests, ray, time, json, pymysql
from datetime import datetime, timedelta

# Latest Modified Date : 2022/04/29
# Mafia42 userdb fetcher


version = "2.0"

end = int(json.loads(requests.post("https://mafia42.com/board/get-lastDiscussion",
                                   json={"articles": {"page": 0}}).text)["articleData"][0]["article_id"]) + 1

f = open("settings.txt", 'r')
settings = f.readlines()
username = settings[1][5:].strip()
password = settings[2][9:].strip()
last_fetch = int(settings[8][11:].strip())
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
        time.sleep(10)
        r = requests.get(f"https://mafia42.com/api/show-lastDiscussion/{article_id}")

    except requests.exceptions.ConnectionError:
        print(f"[ERROR][{timestamp()}] requests.exceptions.ConnectionError: letting server rest")
        time.sleep(10)
        r = requests.get(f"https://mafia42.com/api/show-lastDiscussion/{article_id}")

    res = json.loads(r.text)
    return res['boardData']['nickname'], res['boardData']['user_id'] if res['responseCode'] == 6 else None


@ray.remote
def fetch_old(user_id):
    payload = {"id": user_id}
    try:
        r = requests.post(f"https://mafia42.com/api/user/user-info", data=payload)

    except OSError:
        print(f"[ERROR][{timestamp()}] OSError: letting server rest")
        time.sleep(10)
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
                    file.write(str(data[1]))
                    file.close()

    cnt += 1
    endtime = datetime.now()
    ups = round((y - x + 1) / (endtime - starttime).seconds, 1) if endtime - starttime != 0 else 0
    estimatedmin = round((total - cnt)/ups/60, 1) if ups != 0 else 0
    ett = str(datetime.now() + timedelta(minutes=estimatedmin))
    print(f"[DEBUG][{timestamp()}] fetch complete ({ups} users/sec, {estimatedmin} mins remaining)")
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
        f"[DEBUG][{timestamp()}] fetch complete ({ups} users/sec, {estimatedmin} mins remaining)")
    print(f"[INFO][{timestamp()}] estimated endtime: {ett[:len(ett) - 7]}")
    ray.shutdown()


class Sql:
    def __init__(self):
        self.user_db = pymysql.connect(
            user=username,
            password=password,
            host="127.0.0.1",
            db="userdata",
            charset="utf8"
        )
        print(f"[{timestamp()}] Connected to SQL Server")
        self.date = str(datetime.now().date()).replace("-", "")[2:]
        self.cursor = self.user_db.cursor(pymysql.cursors.DictCursor)
        self.table_name = ""

    def create_table(self):
        try:
            self.cursor.execute(f"""
                CREATE TABLE `userdata_{self.date}` (
                nickname TEXT NULL,
                id INT NULL DEFAULT NULL
                )
                COLLATE = 'utf8mb3_general_ci';
            """)
            print(f"[{timestamp()}] Created Table")
            self.table_name = f"userdata_{self.date}"

        except pymysql.err.OperationalError:
            print(f"[{timestamp()}] Table Already Exists!")
            self.table_name = f"userdata_{self.date}_temp"
            self.cursor.execute(f"""
                CREATE TABLE `{self.table_name}` (
                nickname TEXT NULL,
                id INT NULL DEFAULT NULL
                )
                COLLATE = 'utf8mb3_general_ci';
            """)

    def insert(self, data_):
        statement = f"""
                        INSERT INTO `{self.table_name}`(nickname, id)
                        VALUES (%s, %s);
                        """
        self.cursor.executemany(statement, data_)
        self.user_db.commit()
        self.update()

    @staticmethod
    def update():
        count = 0
        file = open("settings.txt", 'w')
        for line in settings:
            count += 1
            if count != 9:
                file.write(line)
            else:
                file.write(f"last_fetch={end}")
        file.close()


cnt = 1
sql = Sql()
sql.create_table()
for (s, e) in split1:
    if __name__ == "__main__":
        main_old(s, e)
sql.insert(old_users)

for (s, e) in split2:
    if __name__ == "__main__":
        main(s, e)
sql.insert(new_users)
