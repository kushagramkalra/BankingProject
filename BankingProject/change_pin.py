from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox

win=Tk()
win.geometry("640x435")
win.config(bg="lightpink")

def ch():
    acn=ac.get()
    opin=op.get()
    npin=np.get()
    rpin=rnp.get()
    conn=pymysql.connect(host='localhost',user='root',password='',db='atm')
    a=conn.cursor()
    a.execute("select * from bal where account_number='"+acn+"' and pin='"+opin+"' ")
    row=a.rowcount
    if((row>0) & (npin==rpin)):
        a.execute("update bal set pin='"+npin+"' where account_number='"+acn+"' and pin='"+opin+"'")
        conn.commit()
        messagebox.showinfo("message","change")
    else:
        messagebox.showinfo("message","match not found")
        messagebox.showinfo("message","not change")
        conn.close()


frame2=Frame(win,width=600,height=300,highlightbackground="green")
frame2.place(x=20,y=20)
lb1=Label(frame2,text="CHANGE PIN",font=('arial',20,'bold'))
lb1.place(x=200,y=30)

lb3=Label(frame2,text="ENTER ACCOUNT NUMBER",font=('arial',15,'bold'),bd=10)
lb3.place(x=15,y=100)
ac=StringVar()
tb3=Entry(frame2,textvariable=ac,width=30)
tb3.place(x=380,y=110)

lb4=Label(frame2,text="ENTER OLD PIN",font=('arial',15,'bold'),bd=10)
lb4.place(x=15,y=150)
op=StringVar()
tb4=Entry(frame2,textvariable=op,width=30)
tb4.place(x=380,y=160)

lb4=Label(frame2,text="ENTER NEW PIN",font=('arial',15,'bold'),bd=10)
lb4.place(x=15,y=200)
np=StringVar()
tb4=Entry(frame2,textvariable=np,width=30)
tb4.place(x=380,y=210)

lb5=Label(frame2,text="RENTER NEW PIN",font=('arial',15,'bold'),bd=10)
lb5.place(x=15,y=250)
rnp=StringVar()
tb5=Entry(frame2,textvariable=rnp,width=30)
tb5.place(x=380,y=260)

btn=Button(win,text="CHANGE",command=ch,bg="orchid",width=15,height=2,bd=10,activebackground="purple",activeforeground="white")
btn.place(x=260,y=360)

win.mainloop()
