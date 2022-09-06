from lib2to3.pgen2.token import NUMBER
from time import time
from tkinter import *
import sqlite3
from datetime import datetime

root = Tk()
root.title("LOSER")
width = 400
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#==============================VARIABLES======================================
USERNAME = StringVar()
PHNUMBER = StringVar()
TIME= StringVar()
DATE=StringVar()     
#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)
     
#==============================LABELS=========================================
lbl_title = Label(Top, text = "LOSER", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_phnumber = Label(Form, text = "Phone Number:", font=('arial', 14), bd=15)
lbl_phnumber.grid(row=1, sticky="e")
lbl_time1 = Label(Form, text = "Time:", font=('arial', 14), bd=15)
lbl_time1.grid(row=2, sticky="e")
lbl_date1 = Label(Form, text = "Date (mm/dd):", font=('arial', 14), bd=15)
lbl_date1.grid(row=3, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=4, columnspan=2)
     
#==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
phnumber = Entry(Form, textvariable=PHNUMBER, font=(14))
phnumber.grid(row=1, column=1)
time1 = Entry(Form, textvariable=TIME, font=(14))
time1.grid(row=2, column=1)    
date1 = Entry(Form, textvariable=DATE, font=(14))
date1.grid(row=3, column=1)  


#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("callmeout22.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, phnumber TEXT, time1 TEXT, date1 TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `phnumber` = 'admin' AND time1 = 'admin' AND date1 = 'admin'")
    print("created entry 1")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, phnumber, time1, date1) VALUES('admin', 'admin', 'admin', 'admin')")
        conn.commit()

def Login(event=None):
    Database()
    
    if USERNAME.get() == "" or PHNUMBER.get() == "" or TIME.get() == "" or DATE.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")

    #accept input and commit to table        
    else:
        print (PHNUMBER.get())
        #cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `phnumber` = ? AND `time1` = ?", (USERNAME.get(), PHNUMBER.get(), TIME.get()))
        Name= str(USERNAME.get())
        PHNO= str(PHNUMBER.get())
        CALLTIME= TIME.get()
        CALLDATE= DATE.get()
        cursor.execute("INSERT INTO `member` (username, phnumber, time1, date1) VALUES( ? , ? , ? , ?)", (Name,PHNO,CALLTIME,CALLDATE))
        conn.commit()
        
    cursor.close()
    conn.close()
    
     
def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("LOSER")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successful Login!", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)
     


#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Enter", width=45, command=Login)
btn_login.grid(pady=25, row=4, columnspan=2)
#btn_login.bind('<Return>', Login)    

def Back():
    Home.destroy()
    root.deiconify()

#==============================INITIALIATION==================================
if __name__ == '__main__':
    root.mainloop()