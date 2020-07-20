from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
win=Tk()
win.geometry("673x420")
win.config(bg="lightpink")
win.title('Change Nominee')

def chnom():
    yname=yn.get()
    prevnom=pn.get()
    newnom=nn.get()
    conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("select * from bal where name='"+yname+"' and nominee='"+prevnom+"'")
    row=a.rowcount
    if(row>0):
        a.execute("update bal set nominee='"+newnom+"' where name='"+yname+"' and nominee='"+prevnom+"'")
        conn.commit()
        messagebox.showinfo("message","change")
    else:
        messagebox.showinfo("message","match not found")
        conn.rollback()
        messagebox.showinfo("message","not change")
        

frame2=Frame(win,width=630,height=300,highlightbackground="green")
frame2.place(x=20,y=20)
lb=Label(frame2,text="CHANGE NOMINEE",font=('arial',20,'bold'))
lb.place(x=170,y=30)

lb=Label(frame2,text='YOUR NAME',font=('arial',15,'bold'),bd=10)
lb.place(x=15,y=100)
yn=StringVar()
tb=Entry(frame2,textvariable=yn)
tb.place(x=480,y=115)

lb1=Label(frame2,text="NAME OF PREVIOUS NOMINEE",font=('arial',15,'bold'),bd=10)
lb1.place(x=15,y=150)
pn=StringVar()
tb1=Entry(frame2,textvariable=pn)
tb1.place(x=480,y=160)

lb2=Label(frame2,text="NAME OF NEW NOMINEE",font=('arial',15,'bold'),bd=10)
lb2.place(x=15,y=200)
nn=StringVar()
tb2=Entry(frame2,textvariable=nn)
tb2.place(x=480,y=210)

btn1=Button(win,text=" CHANGE  ",command=chnom,bg='orchid',activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn1.place(x=170,y=350)

win.mainloop()
