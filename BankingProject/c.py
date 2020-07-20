from tkinter import *
import pymysql
import pymysql.cursors
import os
from tkinter import messagebox
win=Tk()
win.geometry("820x590")
win.config(bg="lightpink")
win.title('Admin Login')
def nu():
    ma=m.get()
    na=n.get()
    add=ad.get()
    con=c.get()
    nom=no.get()
    try:
        conn = pymysql.connect(host='localhost', user='root', password='', db="atm")
        a = conn.cursor()
        a.execute("insert into newacc(mail,name,address,contact,nominee)values('"+ma+"','"+na+"','"+add+"','"+con+"','"+nom+"')")
        conn.commit()
        print('save')
        os.system("pack_buttons.py")
    except:
        conn.rollback()
        print('not save')

flash_delay = 500  # msec between colour change
flash_colours = ('black', 'red') # Two colours to swap between

def flashColour(object, colour_index):
    object.config(foreground = flash_colours[colour_index])
    win.after(flash_delay, flashColour, object, 1 - colour_index)

lb7=Label(win, text = 'NOTE :- You have to visit the bank for account number, pin and IFSC code (and for further formalities if any..)',
                      foreground = flash_colours[0],background='lightpink')
lb7.place(x=10,y=570)

flashColour(lb7, 0)

lb6=Label(win,text='WELCOME TO ROYAL BANK ATM SERVICE',font=('arial',20,'bold'),background='lightpink')
lb6.place(x=110,y=20)

lb=Label(win,text='ENTER E-MAIL ID',background='lightpink')
lb.place(x=190,y=100)
m=StringVar()
tb=Entry(win,textvariable=m)
tb.place(x=460,y=100)

lb1=Label(win,text='ENTER NAME',background='lightpink')
lb1.place(x=190,y=150)
n=StringVar()
tb1=Entry(win,textvariable=n)
tb1.place(x=460,y=150)

lb2=Label(win,text='ENTER ADDRESS',background='lightpink')
lb2.place(x=190,y=200)
ad=StringVar()
tb2=Entry(win,textvariable=ad)
tb2.place(x=460,y=200)

lb3=Label(win,text='ENTER CONTACT',background='lightpink')
lb3.place(x=190,y=250)
c=StringVar()
tb3=Entry(win,textvariable=c)
tb3.place(x=460,y=250)

lb4=Label(win,text='ENTER NOMINEE',background='lightpink')
lb4.place(x=190,y=300)
no=StringVar()
tb4=Entry(win,textvariable=no)
tb4.place(x=460,y=300)

btn1=Button(win,text=" NEXT ",command=nu,font=('arial',10,'bold'),width=30,height=2,relief="ridge")
btn1.place(x=270,y=425)

win.mainloop()
