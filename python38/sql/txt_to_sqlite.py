import imp
import pandas as pd
import sqlite3

def txt_to_dataframe():
    f = open("python38/Mafia42/fetchuser/userlist.txt", 'r')
    lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.strip())
    f.close()
    
    return pd.DataFrame(data)


if __name__ == "__main__":
    df = txt_to_dataframe()
    con = sqlite3.connect("python38/Mafia42/fetchuser/userlist.db")
    df.to_sql("userlist", con)
