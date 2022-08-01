import pandas as pd
import mariadb
import sqlite3

def mariadb_to_dataframe(user, password, database, query) -> pd.DataFrame:
    dbconn = mariadb.connect(
        user=user,
        password=password,
        host="localhost",
        port=3306,
        database=database,
    )
    query_result = pd.read_sql(query, dbconn)
    dbconn.close()

    return query_result


if __name__ == "__main__":
    sql = "SELECT * FROM userdata_220709"
    df = mariadb_to_dataframe("root", "1234", "mafia42", sql)
    con = sqlite3.connect("userdata_220709.db")
    df.to_sql("userdata", con)
    