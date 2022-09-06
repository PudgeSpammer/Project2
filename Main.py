#name_generator

import string
import re
import random
import sqlite3
from twilio.rest import Client
from datetime import datetime

account_sid = "ACa66d60174718a32f8118c03ad728ce92"
auth_token = "df276795e7c27a7d18c314156a90ff2e"
client = Client(account_sid, auth_token)

#NameGenerator
def Name_Generator():
    First = ['A', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'S' , 'W', 'Y']
    Second = ['A', 'D', 'E', 'H', 'I', 'J', 'K', 'M', 'N', 'P', 'R' , 'S', 'W']
    Surname= ['Smith','Johnson','Williams','Brown','Jones','Garcia','Miller','Davis','Rodriguez','Lopez','Thomas','Moore','Wilson','Lee','White','Young']
    while True:
        First_Alphabet= random.choice (First)
        Second_Alphabet= random.choice (Second)
        if(First_Alphabet == Second_Alphabet ):
            continue
        else:
            break
    Surname_Final= random.choice(Surname)
    name= First_Alphabet + " " + Second_Alphabet + " " + Surname_Final
    print (name)

#Enter Name Choice User

#create contact

#delete number
def deleteNumber(phno):
    print("phno")
    print(phno)
    conn = sqlite3.connect("callmeout22.db")
    cursor = conn.cursor()
    query2= "delete from member where phnumber = " + str(phno)
    cursor.execute (query2)
    print("DELETED")
    conn.commit()
    cursor.close()
    conn.close()

#makecall
def MakeCall(number):
    number=str(number)
    number=number[2:12]
    print(number)
    print("this is number")
    print(number)
    deleteNumber(number)
    number="+1"+number
    call= client.calls.create (twiml='<Response><Say> Daddy </Say></Response>', to=number, from_='+19206478318')
    

#messages
def SendMessage(number):
    message= client.messages.create(body='test daddy', to=number, from_='+19206478318')


def getNumber(i1):
    conn = sqlite3.connect("callmeout22.db")
    cursor = conn.cursor()
    query= "select phnumber from member"
    cursor.execute (query)
    rows=cursor.fetchall()
    c=0
    for row in rows:
        c=c+1
        if(c==i1):
            return(row)
            c=0
    conn.close()

#Alarm System For Call and message
def checkTime():
    now = str(datetime.now())
    date= now[5:10]
    date= re.sub('[:,/,-]', '', date)
    

    time= now[11:16]
    time= re.sub('[:,/,-]', '', time)

    conn = sqlite3.connect("callmeout22.db")
    cursor = conn.cursor()
    query= "select time1 from member"
    cursor.execute (query)
    rows=cursor.fetchall()
    cursor.close()
    conn.close()

    conn1 = sqlite3.connect("callmeout22.db")
    cursor1 = conn1.cursor()
    query2= "select date1 from member"
    cursor1.execute (query2)
    rows2=cursor1.fetchall()
    cursor1.close()
    conn1.close()
    print(time)

    #date & time column
    i=0

    for row in rows:
        row=str(row)
        row2=str(rows2[i])
        row= row[2:6]
        row2=row2[2:6]
        i=i+1
        if(row2==date):
            if(time>=row):
                print (row)
                print('call happened')
                MakeCall(getNumber(i))
                i=0

        
    
checkTime()

#Delete Contact on Phone