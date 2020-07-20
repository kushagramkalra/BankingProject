from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
from datetime import *

win=Tk()
win.geometry("600x400")
win.config(bg="lightpink")
win.resizable(FALSE,FALSE)
def depo():
    ac=acc.get()
    pi=pin.get()
    am=amt.get()
    conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from bal where account_number='"+ac+"' and pin='"+pi+"' ")
    row=var.rowcount
    if(row>0):
        var.execute("update bal set total_amount=total_amount+'"+am+"' where account_number='"+ac+"' and pin='"+pi+"' ")
        var.execute("insert into mini (account_number,date_and_time,deposit) values ('"+ac+"','"+str(datetime.now())+"','"+am+"')")
        conn.commit()
        messagebox.showinfo("Information","deposited  successfully")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Information","Data Transfer Failed")

frame2=Frame(win,width=560,height=280,highlightbackground="green")
frame2.place(x=20,y=20)
lb1=Label(frame2,text="DEPOSIT CASH",font=('arial',20,'bold'))
lb1.place(x=180,y=30)

lb3=Label(frame2,text="ENTER ACCOUNT NUMBER",font=('arial',15,'bold'),bd=10)
lb3.place(x=15,y=100)
acc=StringVar()
tb3=Entry(frame2,textvariable=acc,width=30)
tb3.place(x=340,y=115)

lb4=Label(frame2,text="ENTER PIN",font=('arial',15,'bold'),bd=10)
lb4.place(x=15,y=150)
pin=StringVar()
tb4=Entry(frame2,show="*",textvariable=pin,width=30)
tb4.place(x=340,y=160)

lb4=Label(frame2,text="ENTER AMOUNT",font=('arial',15,'bold'),bd=10)
lb4.place(x=15,y=200)
amt=StringVar()
tb4=Entry(frame2,textvariable=amt,width=30)
tb4.place(x=340,y=210)

btn=Button(win,text="DEPOSIT",command=depo,bg="orchid",width=15,height=2,bd=10,activebackground="purple",activeforeground="white",relief='ridge')
btn.place(x=230,y=320)

win.mainloop()
