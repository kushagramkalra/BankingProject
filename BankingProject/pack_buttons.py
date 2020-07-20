from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
import os

win=Tk()
win.geometry("640x380")
win.config(bg="lightpink")

def premium():
    os.system("prem.py")
def basic():
    os.system("basic.py")
def average():
    os.system("average.py")


lb1=Label(text="SELECT THE PACK",font=('arial',20,'bold'),bg="lightpink")
lb1.place(x=180,y=40)

btn1=Button(text="PREMIUM",command=premium,bg="orchid",width=15,height=2)
btn1.place(x=70,y=170)

btn2=Button(text="AVERAGE",command=average,bg="orchid",width=15,height=2)
btn2.place(x=250,y=230)

btn3=Button(text="BASIC",command=basic,bg="orchid",width=15,height=2)
btn3.place(x=420,y=170)

flash_delay = 500  # msec between colour change
flash_colours = ('black', 'red') # Two colours to swap between

def flashColour(object, colour_index):
    object.config(foreground = flash_colours[colour_index])
    win.after(flash_delay, flashColour, object, 1 - colour_index)

lb7=Label(text = "IMPORTANT INFORMATION",font=('ariel',10,'bold'),foreground = flash_colours[0],background='lightpink')
lb7.place(x=10,y=300)
flashColour(lb7, 0)


lb7=Label(win, text = '1) Minimum amount to open an account with basic pack is Rs.20,000',
                      foreground = flash_colours[0],background='lightpink')
lb7.place(x=10,y=320)
flashColour(lb7, 0)

lb8=Label(win, text = '2) Minimum amount to open an account with average pack is Rs.50,000',
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=340)
flashColour(lb8, 0)

lb8=Label(win, text = '3) Minimum amount to open an account with premium pack is Rs.1,00,000',
                      foreground = flash_colours[0],background='lightpink')
lb8.place(x=10,y=360)
flashColour(lb8, 0)

win.mainloop()
