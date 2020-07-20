from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
from datetime import *
def tfun():
    acn=an.get()
    pin=p.get()
    racn=ran.get()
    am=amt.get()
    
    conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("select * from bal where account_number='"+acn+"' and pin='"+pin+"' ")
    
    row=a.rowcount
    if(row>0):
        a.execute("update bal set total_amount=total_amount-'"+am+"' where account_number='"+acn+"' and pin='"+pin+"' ")
        a.execute("insert into tf (account_number,transfered_to,amount,date_and_time) values('"+acn+"','"+racn+"','"+am+"','"+str(datetime.now())+"')")
        conn.commit()
        messagebox.showinfo("Information","withdrawl successfully")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Information","Data Transfer Failed")
    

win=Tk()
win.geometry("640x530")
win.config(bg="lightpink")
win.title('transfer fund')

frame2=Frame(win,width=600,height=400,highlightbackground="green")
frame2.place(x=20,y=20)
lb3=Label(frame2,text="FUND TRANSFER",font=('arial',20,'bold'))
lb3.place(x=180,y=20)

lb=Label(frame2,text="YOUR ACCOUNT NUMBER",font=('arial',15,'bold'),bd=10)
lb.place(x=30,y=90)
an=StringVar()
tb=Entry(frame2,textvariable=an)
tb.place(x=420,y=105)

lb1=Label(frame2,text="PIN",font=('arial',15,'bold'),bd=10)
lb1.place(x=30,y=150)
p=StringVar()
tb1=Entry(frame2,show="*",textvariable=p)
tb1.place(x=420,y=160)

lb2=Label(frame2,text="RECIVER'S ACCOUNT NUMBER",font=('arial',15,'bold'),bd=10)
lb2.place(x=30,y=210)
ran=StringVar()
tb2=Entry(frame2,textvariable=ran)
tb2.place(x=420,y=225)

lb2=Label(frame2,text="AMOUNT",font=('arial',15,'bold'),bd=10)
lb2.place(x=30,y=270)
amt=StringVar()
tb2=Entry(frame2,textvariable=amt)
tb2.place(x=420,y=280)

btn1=Button(win,text=" TRANSFER ",command=tfun,bg='orchid',font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn1.place(x=140,y=450)

win.mainloop()
