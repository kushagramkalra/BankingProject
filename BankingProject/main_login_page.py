from tkinter import *
from tkinter import Message,Text
from tkinter import messagebox
#import cv2
import os
import shutil
import csv
import numpy as np
#from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import os
import pymysql
import pymysql.cursors
win=Tk()
win.geometry("800x400+300+200")
win.config(bg="lightpink")

def log():
    na=n.get()
    acn=ac.get()
    pin=p.get()
    conn = pymysql.connect(host='localhost', user='root', password='', db="atm")
    a = conn.cursor()
    a.execute("select * from bal where name='"+na+"' and account_number='"+acn+"' and pin='"+pin+"'")
    result=a.fetchall()
    count=a.rowcount
    print(result)
    print(count)
    if(count>0):
        os.system("Home_page.py")
    else:
        messagebox.showinfo('message','not login')
        conn.rollback()
        print('not save')
        conn.close()    
    i=0
    if(i==0):
        cam=cv2.VideoCapture(0)
        face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        ff=open('atmimage/all.txt','r')
        sampleNum=int(ff.read())
        while(True):
            ret,gray=cam.read()
            faces=face_classifier.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
                sampleNum=sampleNum+1
                cv2.imwrite('atmimage\ ' +str(sampleNum)+".jpeg",gray[y:y+h,x:x+w])
                print(int(sampleNum))
                cv2.imshow('frame',gray)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                cam.release()
                cv2.destroyAllWindows()
                f=open('atmimage/all.txt','w')
                f.write(str(sampleNum))
                f.close()
                print('hello')
    else:
        print("no")

def adlog():
    os.system("admin_login.py")
    
def uslog():
    os.system("c.py")
    i=0
    if(i==0):
        cam=cv2.VideoCapture(0)
        face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        ff=open('newaccimage/new.txt','r')
        sampleNum=int(ff.read())
        while(True):
            ret,gray=cam.read()
            faces=face_classifier.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in faces:
                cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
                sampleNum=sampleNum+1
                cv2.imwrite('newaccimage\ ' +str(sampleNum)+".jpeg",gray[y:y+h,x:x+w])
                print(int(sampleNum))
                cv2.imshow('frame',gray)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                cam.release()
                cv2.destroyAllWindows()
                f=open('newaccimage/new.txt','w')
                f.write(str(sampleNum))
                f.close()
                print('hello')
    else:
        print("no")
    
lb3=Label(win,text='WELCOME TO ROYAL BANK ATM SERVICE',font=('arial',20,'bold'),background='lightpink')
lb3.place(x=110,y=20)

lb=Label(win,text='NAME',background='lightpink')
lb.place(x=190,y=100)
n=StringVar()
tb=Entry(win,textvariable=n)
tb.place(x=460,y=100)

lb1=Label(win,text='ACCOUNT NUMBER',background='lightpink')
lb1.place(x=190,y=150)
ac=StringVar()
tb1=Entry(win,textvariable=ac)
tb1.place(x=460,y=150)

lb2=Label(win,text='PIN',background='lightpink')
lb2.place(x=190,y=200)
p=StringVar()
tb2=Entry(win,show="*",textvariable=p)
tb2.place(x=460,y=200)

btn1=Button(win,text=" LOGIN ",command=log,font=('arial',10,'bold'),width=30,height=2,relief="ridge")
btn1.place(x=30,y=250)

btn2=Button(win,text=" ADMIN LOGIN ",command=adlog,font=('arial',10,'bold'),width=30,height=2,relief="ridge")
btn2.place(x=525,y=250)

btn3=Button(win,text=" NEW USER ",command=uslog,font=('arial',10,'bold'),width=30,height=2,relief="ridge")
btn3.place(x=280,y=325)

win.mainloop()
