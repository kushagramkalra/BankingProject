from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os

win=Tk()
win.geometry("640x400")
win.config(bg="lightpink")

def prem():
    na=n.get()
    am='premium'
    at=100000
    conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
    var = conn.cursor()
    var.execute("select * from newacc where name='"+na+"'")
    row=var.rowcount
    if(row>0):
        var.execute("update newacc set amount='"+str(at)+"',pack='"+str(am)+"' where name='"+na+"' ")
        conn.commit()
        messagebox.showinfo("Information","account request sent")
    else:
        messagebox.showinfo("Information","not valid")
        conn.rollback()
        messagebox.showinfo("Information","account request failed")


lb1=Label(text="PREMIUM",font=('arial',20,'bold'),bg="lightpink")
lb1.place(x=252.5,y=20)

lb3=Label(text="ENTER NAME",font=('arial',15,'bold'),bd=10,bg="lightpink")
lb3.place(x=70,y=80)
n=StringVar()
tb3=Entry(textvariable=n,width=30)
tb3.place(x=400,y=92)

btn1=Button(text="OPEN ACCOUNT",command=prem,bg="orchid",width=15,height=2)
btn1.place(x=260,y=160)

flash_delay = 500  # msec between colour change
flash_colours = ('black', 'red') # Two colours to swap between

def flashColour(object, colour_index):
    object.config(foreground = flash_colours[colour_index])
    win.after(flash_delay, flashColour, object, 1 - colour_index)

lb7=Label(text = "IMPORTANT INFORMATION",font=('ariel',10,'bold'),foreground = flash_colours[0],background='lightpink')
lb7.place(x=10,y=250)
flashColour(lb7, 0)


lb7=Label(win, text = '1) 20% rebate on medical facilities.',
                      foreground = flash_colours[0],background='lightpink')
lb7.place(x=10,y=270)
flashColour(lb7, 0)

lb8=Label(win, text = '2) 8% interest on all fixed deposits (one can claim the principle amount not before 1 year.)',
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=290)
flashColour(lb8, 0)

lb8=Label(win, text = '3) 15% off on all movie tickets.',
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=310)
flashColour(lb8, 0)

lb8=Label(win, text = '4) 20% off on all alternate food transections(groceris,restaurants.)',
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=330)
flashColour(lb8, 0)

lb8=Label(win, text = '5) Airport lounge access in all domestic as well as international airlines.',
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=350)
flashColour(lb8, 0)

lb8=Label(win, text = '6) Saperate counters are available for premium account holders.',font=('ariel',10,'bold'),
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=380)
flashColour(lb8, 0)


lb8=Label(win, text = 'For more information contact 8826479826 or visit nearest branch...',font=('ariel',10,'bold'),
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=380)
flashColour(lb8, 0)

win.mainloop()
