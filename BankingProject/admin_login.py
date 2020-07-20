from tkinter import *
import pymysql
import pymysql.cursors
import os
from tkinter import messagebox
win=Tk()
win.geometry("550x420")
win.config(bg="lightpink")
win.title('Admin Login')

def adlo():
    an=yn.get()
    ap=pn.get()
    conn = pymysql.connect(host='localhost', user='root', password='', db="atm")
    a = conn.cursor()
    a.execute("select * from adm where id='"+an+"' and password='"+ap+"'")
    result=a.fetchall()
    count=a.rowcount
    print(result)
    print(count)
    if(count>0):
        os.system("adm_hpage.py")
    else:
        messagebox.showinfo('message','not login')
        conn.rollback()
        print('not save')
        conn.close()

frame2=Frame(win,width=500,height=300,highlightbackground="green")
frame2.place(x=20,y=20)
lb=Label(frame2,text="ADMIN LOGIN",font=('arial',20,'bold'))
lb.place(x=170,y=30)

lb=Label(frame2,text='ADMIN ID',font=('arial',15,'bold'),bd=10)
lb.place(x=15,y=100)
yn=StringVar()
tb=Entry(frame2,textvariable=yn)
tb.place(x=300,y=115)

lb1=Label(frame2,text="ADMIN PASSWORD",font=('arial',15,'bold'),bd=10)
lb1.place(x=15,y=150)
pn=StringVar()
tb1=Entry(frame2,show="*",textvariable=pn)
tb1.place(x=300,y=160)


btn1=Button(win,text=" LOGIN  ",command=adlo,bg='orchid',activebackground="purple",activeforeground="white",width=20,height=2,relief="ridge",bd=10)
btn1.place(x=200,y=350)

win.mainloop()
