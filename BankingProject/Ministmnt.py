from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox

win=Tk()
win.geometry("650x310")
win.config(bg="lightpink")
win.resizable(FALSE,FALSE)
def showmini():

            ac=acc.get()
            conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
            var = conn.cursor()
            var.execute("select * from mini where account_number='"+ac+"'")
            v = var.fetchall()
            counts=var.rowcount
            if(counts>0):
                    show = Tk()
                    show.geometry("850x500")
                    show.resizable(False,True)
                    show.title("Details")
                    vary=80
                    headlb=Label(show,text="customer details",font="Times 25 bold").grid(row=0,column=1,padx=200)
                    #-------------------------------Label of the Table---------------------------------#
                    lb1 = Label(show,text="Account_Number ",width=20,bg="white",bd=5).place(x=2,y=50)
                    lb2 = Label(show,text="Date_And_Time",width=20,bg="white",bd=5).place(x=175,y=50)
                    lb3 = Label(show,text="Deposit",width=20,bg="white",bd=5).place(x=348,y=50)
                    lb4 = Label(show,text="Withdraw",width=20,bg="white",bd=5).place(x=521,y=50)
                    for i in range(0,var.rowcount):
                            lb1 = Label(show,text=v[i][0],width=20,bg="white",bd=5).place(x=2,y=vary)
                            lb2 = Label(show,text=v[i][1],width=20,bg="white",bd=5).place(x=175,y=vary)
                            lb3 = Label(show,text=v[i][2],width=20,bg="white",bd=5).place(x=348,y=vary)
                            lb4 = Label(show,text=v[i][3],width=20,bg="white",bd=5).place(x=521,y=vary)
                            vary+=30
                    print(vary)
                    conn.commit()
            else:
                    conn.rollback()
                    messagebox.showinfo('message','Invalid')
                    print("!!!!!!!!!!!!!!!!!!!!!!Exception!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

frame2=Frame(win,width=610,height=200,highlightbackground="green")
frame2.place(x=20,y=20)
lb1=Label(frame2,text="MINISTATEMENT",font=('arial',20,'bold'))
lb1.place(x=190,y=30)

lb3=Label(frame2,text="ENTER ACCOUNT NUMBER",font=('arial',15,'bold'),bd=10)
lb3.place(x=15,y=100)
acc=StringVar()
tb3=Entry(frame2,textvariable=acc,width=30)
tb3.place(x=400,y=115)

btn=Button(win,text="SHOW",command=showmini,bg="orchid",width=15,height=2,activeforeground="white",activebackground="purple",relief='ridge',bd=10)
btn.place(x=260,y=240)

win.mainloop()
