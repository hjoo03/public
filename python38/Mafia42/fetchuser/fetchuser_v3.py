# -*- coding: utf-8 -*-

import os, sys, datetime, sqlite3, requests, ray, json, time
import pandas as pd

class DataBase:
    def __init__(self) -> None:
        pass
    
    def import_old_db(self):
        for file in os.listdir("source\\"):
            if "userlist" and ".db" in file:
                db = file
        self.conn = sqlite3.connect("source\\" + db)
        self.database = db
        db_name = "userlist"
        d = pd.read_sql(f"SELECT * FROM {db_name}", self.conn).set_index("index")
        df = d if not d.drop_duplicates() else d.drop_duplicates
        self.old_users = df.values.tolist()
        
    def create_new_db(self):
        pass
    

class Worker:
    def __init__(self, user_list, ):
        self.user_list = user_list
        self.userdata = []
        
    def run(self):
        print(f"Start Sub Thread [{self.name}]")
        for user in self.user_list:
            payload = {"id": user}
            try:
                r = requests.post(f"https://mafia42.com/api/user/user-info", data=payload)
            except OSError:
                print(f"SubThread[{self.name}]: OSEror; Letting Server Rest")
                time.sleep(10)
                r = requests.post(f"https://mafia42.com/api/user/user-info", data=payload)
            try:
                res = json.loads(r.text)
                self.userdata.append((res['userData']['NICKNAME'], res['userData']['ID']))
            except json.decoder.JSONDecodeError:
                pass
            
        print(f"Kill Sub Thread [{self.name}]")
        