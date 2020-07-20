from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
from datetime import *

win=Tk()
win.geometry("640x380")
win.config(bg="lightpink")

def two():
    ac=acc.get()
    pi=pin.get()
    am=200
    conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from bal where account_number='"+ac+"' and pin='"+pi+"' ")
    row=var.rowcount
    if(row>0):
        var.execute("update bal set total_amount=total_amount-'"+str(am)+"' where account_number='"+ac+"' and pin='"+pi+"' ")
        var.execute("insert into mini (account_number,date_and_time,withdraw) values('"+ac+"','"+str(datetime.now())+"','"+str(am)+"')")
        conn.commit()
        messagebox.showinfo("Information","withdrawl successfully")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Information","Data Transfer Failed")

def five():
    ac=acc.get()
    pi=pin.get()
    am=500
    conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from bal where account_number='"+ac+"' and pin='"+pi+"' ")
    row=var.rowcount
    if(row>0):
        var.execute("update bal set total_amount=total_amount-'"+str(am)+"' where account_number='"+ac+"' and pin='"+pi+"' ")
        var.execute("insert into mini (account_number,date_and_time,withdraw) values('"+ac+"','"+str(datetime.now())+"','"+str(am)+"')")
        conn.commit()
        messagebox.showinfo("Information","withdrawl successfully")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Information","Data Transfer Failed")

def thousand():
    ac=acc.get()
    pi=pin.get()
    am=1000
    conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from bal where account_number='"+ac+"' and pin='"+pi+"' ")
    row=var.rowcount
    if(row>0):
        var.execute("update bal set total_amount=total_amount-'"+str(am)+"' where account_number='"+ac+"' and pin='"+pi+"' ")
        var.execute("insert into mini (account_number,date_and_time,withdraw) values('"+ac+"','"+str(datetime.now())+"','"+str(am)+"')")
        conn.commit()
        messagebox.showinfo("Information","withdrawl successfully")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Information","Data Transfer Failed")

def fiveth():
    ac=acc.get()
    pi=pin.get()
    am=2000
    conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from bal where account_number='"+ac+"' and pin='"+pi+"' ")
    row=var.rowcount
    if(row>0):
        var.execute("update bal set total_amount=total_amount-'"+str(am)+"' where account_number='"+ac+"' and pin='"+pi+"' ")
        var.execute("insert into mini (account_number,date_and_time,withdraw) values('"+ac+"','"+str(datetime.now())+"','"+str(am)+"')")
        conn.commit()
        messagebox.showinfo("Information","withdrawl successfully")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Information","Data Transfer Failed")

frame2=Frame(win,width=600,height=340,highlightbackground="green")
frame2.place(x=20,y=20)
lb1=Label(frame2,text="FAST CASH",font=('arial',20,'bold'))
lb1.place(x=220,y=30)

lb3=Label(frame2,text="ENTER ACCOUNT NUMBER",font=('arial',15,'bold'),bd=10)
lb3.place(x=15,y=100)
acc=StringVar()
tb3=Entry(frame2,textvariable=acc,width=30)
tb3.place(x=380,y=115)

lb4=Label(frame2,text="ENTER PIN",font=('arial',15,'bold'),bd=10)
lb4.place(x=15,y=150)
pin=StringVar()
tb4=Entry(frame2,show="*",textvariable=pin,width=30)
tb4.place(x=380,y=160)

btn1=Button(frame2,text="200",command=two,bg="orchid",width=15,height=2)
btn1.place(x=70,y=220)

btn2=Button(frame2,text="500",command=five,bg="orchid",width=15,height=2)
btn2.place(x=70,y=280)

btn3=Button(frame2,text="1000",command=thousand,bg="orchid",width=15,height=2)
btn3.place(x=420,y=220)

btn4=Button(frame2,text="2000",command=fiveth,bg="orchid",width=15,height=2)
btn4.place(x=420,y=280)



win.mainloop()
