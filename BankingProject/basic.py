from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os

win=Tk()
win.geometry("700x380")
win.config(bg="lightpink")

def basic():
    na=n.get()
    am='basic'
    at=20000
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




lb1=Label(text="BASIC",font=('arial',20,'bold'),bg="lightpink")
lb1.place(x=277,y=20)

lb3=Label(text="ENTER NAME",font=('arial',15,'bold'),bd=10,bg="lightpink")
lb3.place(x=70,y=80)
n=StringVar()
tb3=Entry(textvariable=n,width=30)
tb3.place(x=400,y=92)

btn1=Button(text="SELECT",command=basic,bg="orchid",width=15,height=2)
btn1.place(x=260,y=160)

flash_delay = 500  # msec between colour change
flash_colours = ('black', 'red') # Two colours to swap between

def flashColour(object, colour_index):
    object.config(foreground = flash_colours[colour_index])
    win.after(flash_delay, flashColour, object, 1 - colour_index)

lb7=Label(text = "IMPORTANT INFORMATION",font=('ariel',10,'bold'),foreground = flash_colours[0],background='lightpink')
lb7.place(x=10,y=250)
flashColour(lb7, 0)


lb7=Label(win, text = '1) 10% rebate on medical facilities.',
                      foreground = flash_colours[0],background='lightpink')
lb7.place(x=10,y=270)
flashColour(lb7, 0)

lb8=Label(win, text = '2) 5% interest on all fixed deposits (one can claim the principle amount not before 1 year.)',
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=290)
flashColour(lb8, 0)

lb8=Label(win, text = '3) 5% off on all movie tickets.',
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=310)
flashColour(lb8, 0)

lb8=Label(win, text = '4) 10% off on all alternate food transections(groceris,restaurants.)',
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=330)
flashColour(lb8, 0)

lb8=Label(win, text = 'For more information contact 8826479826 or visit nearest branch...',font=('ariel',10,'bold'),
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=360)
flashColour(lb8, 0)

win.mainloop()
