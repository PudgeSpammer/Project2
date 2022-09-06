import sqlite3

def deleteTest():
    conn = sqlite3.connect("callmeout22.db")
    cursor = conn.cursor()
    query= "delete from member"
    cursor.execute (query)
    conn.commit()
    cursor.close()
    conn.close()

deleteTest()