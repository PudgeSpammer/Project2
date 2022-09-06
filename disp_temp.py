import sqlite3
import re
from datetime import datetime

def seeTable():
    conn = sqlite3.connect("callmeout22.db")
    cursor = conn.cursor()
    query= "select * from member"
    cursor.execute (query)
    rows=cursor.fetchall()
    for row in rows:
        for col in row:
            print (col, end=' ')
        print()

    cursor.close()
    conn.close()

seeTable()
