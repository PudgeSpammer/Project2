from flask import Flask, render_template, request, redirect, url_for, session
from flaskext.mysql import MySQL
#from sqlalchemy import MySQL
from tkinter import *
import sqlite3
from lib2to3.pgen2.token import NUMBER
import mysql
#import MySQLdb.cursors
import re



app = Flask(__name__)
  
  
app.secret_key = 'your secret key'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your password'
app.config['MYSQL_DB'] = 'geeklogin'
  
mysql = MySQL(app)

@app.route('/')
@app.route('/register', methods =['GET', 'POST'])
def register():
    Name = ""
    Number = ""
    time = ""
    date = ""

    msg = ''
    if request.method == 'POST' and 'Name' in request.form and 'Number' in request.form and 'Time' in request.form and 'Date' in request.form:
        Name = request.form['Name']
        Number = request.form['Number']
        time = request.form['Time']
        date = request.form['Date'] 
        print(Name)
    
    print("Entered")
    global conn, cursor
    conn = sqlite3.connect("callmeout22.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, phnumber TEXT, time1 TEXT, date1 TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `phnumber` = 'admin' AND time1 = 'admin' AND date1 = 'admin'")
    print("created entry 2")
    
    Name= str(Name)
    Number= str(Number)
    time= str(time)
    date= str(date)
    cursor.execute("INSERT INTO `member` (username, phnumber, time1, date1) VALUES( ? , ? , ? , ?)", (Name,Number,time,date))
    conn.commit()
    cursor.close()
    conn.close()

    return render_template('register.html', msg = msg)

if __name__ == '__main__':
    app.run(debug=True)