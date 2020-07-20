from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox

win=Tk()
win.geometry("700x500")
win.config(bg="LIGHTPINK")
win.resizable(FALSE,FALSE)
def con():
    acn=ac.get()
    oldc=oc.get()
    newc=nc.get()
    conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("select * from bal where account_number='"+acn+"' and contact='"+oldc+"' ")
    row=a.rowcount
    if(row>0):
        a.execute("update bal set contact='"+newc+"' where account_number='"+acn+"' and contact='"+oldc+"' ")
        conn.commit()
        messagebox.showinfo("message","change")
    else:
        messagebox.showinfo("message","not match found")
        messagebox.showinfo("message","not change")
        conn.close()

frame2=Frame(win,width=660,height=350,highlightbackground="green")
frame2.place(x=20,y=20)
lb1=Label(frame2,text="UPDATE CONTACT",font=('arial',20,'bold'))
lb1.place(x=200,y=30)

lb3=Label(frame2,text="ENTER ACCOUNT NUMBER",font=('arial',15,'bold'),bd=10)
lb3.place(x=15,y=100)
ac=StringVar()
tb3=Entry(frame2,textvariable=ac,width=30)
tb3.place(x=450,y=115)


lb4=Label(frame2,text="ENTER OLD CONTACT NUMBER",font=('arial',15,'bold'),bd=10)
lb4.place(x=15,y=175)
oc=StringVar()
tb4=Entry(frame2,textvariable=oc,width=30)
tb4.place(x=450,y=190)

lb5=Label(frame2,text="ENTER NEW CONTACT NUMBER",font=('arial',15,'bold'),bd=10)
lb5.place(x=15,y=245)
nc=StringVar()
tb5=Entry(frame2,textvariable=nc,width=30)
tb5.place(x=450,y=260)


btn=Button(win,text="UPDATE",command=con,bg="orchid",width=15,height=2,bd=10)
btn.place(x=280,y=420)

win.mainloop()
