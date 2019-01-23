import pymysql

con = pymysql.connect("cs1.ucc.ie", "jw22", "fidaekee", "2020_jw22")

with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    print("Database version: {}".format(version[0]))