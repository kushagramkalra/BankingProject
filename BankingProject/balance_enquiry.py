from tkinter import *
from tkinter import messagebox
import pymysql
import pymysql.cursors

win=Tk()
win.geometry("540x300")
win.config(bg="lightpink")
win.resizable(FALSE,FALSE)

def balenq():
    acn=an.get()
    conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("select total_amount from bal where account_number='"+acn+"'")
    results=a.fetchall()
    count=a.rowcount
    print(results)
    print(count)
    if(count>0):
        messagebox.showinfo("Account Balance",results)
    else:
        messagebox.showinfo("hello","record not found")

frame2=Frame(win,width=500,height=200,highlightbackground="green")
frame2.place(x=20,y=20)
lb1=Label(frame2,text="BALANCE ENQUIRY",font=('arial',20,'bold'))
lb1.place(x=110,y=20)

lb=Label(win,text='ACCOUNT NUMBER',font=('arial',15,'bold'),bd=10)
lb.place(x=50,y=115)
an=StringVar()
tb=Entry(win,textvariable=an)
tb.place(x=340,y=127)

btn1=Button(win,text=" SEARCH ",bg='orchid',command=balenq,font=('arial',10,'bold'),width=40,height=2,relief="ridge",activebackground="purple",activeforeground="white",bd=10)
btn1.place(x=100,y=230)

win.mainloop()
