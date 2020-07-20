from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os

def delete():
    acn=an.get()
    pn=pin.get()
    
    conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("delete from bal where account_number='"+acn+"' and pin='"+pn+"'")
    conn.commit()
    result=a.fetchall()
    count=a.rowcount
    if(count>0):
        messagebox.showinfo("message","deleted")
    else:
        conn.rollback()
        print('not delete')
        messagebox.showinfo("message","not deleted")
    conn.close()

win=Tk()
win.title("block account")
win.geometry("690x350")
win.config(bg="lightpink")
win.resizable(FALSE,FALSE)

frame2=Frame(win,width=650,height=220,highlightbackground="green")
frame2.place(x=20,y=20)
lb1=Label(frame2,text="BLOCK YOUR ACCOUNT",font=('arial',20,'bold'))
lb1.place(x=160,y=30)

lb2=Label(frame2,text="ENTER ACCOUNT NUMBER",font=('arial',15,'bold'),bd=10)
lb2.place(x=40,y=100)
an=StringVar()
tb2=Entry(frame2,textvariable=an,width=30)
tb2.place(x=400,y=115)

lb3=Label(frame2,text="ENTER PIN",font=('arial',15,'bold'),bd=10)
lb3.place(x=40,y=150)
pin=StringVar()
tb3=Entry(frame2,show="*",textvariable=pin,width=30)
tb3.place(x=400,y=165)

btn=Button(win,text="BLOCK",bg="orchid",command=delete,width=15,height=2,activebackground="purple",activeforeground="white",relief='ridge',bd=10)
btn.place(x=280,y=270)

win.mainloop()
