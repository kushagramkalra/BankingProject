from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox

def tf():
        ac=an.get()
        conn = pymysql.connect(host="localhost",user="root",password="",db='atm')
        var = conn.cursor()
        var.execute("select * from tf where account_number='"+ac+"'")
        v=var.fetchall()
        row=var.rowcount
        if(row>0):
            show = Tk()
            show.geometry("850x500")
            show.resizable(False,True)
            show.title("Details")
            vary=80
            headlb=Label(show,text="customer details",font="Times 25 bold").grid(row=0,column=1,padx=200)
            #-------------------------------Label of the Table---------------------------------#
            lb1 = Label(show,text="Account_Number ",width=20,bg="white",bd=5).place(x=2,y=50)
            lb2 = Label(show,text="Transfered_To",width=20,bg="white",bd=5).place(x=175,y=50)
            lb3 = Label(show,text="Amount",width=20,bg="white",bd=5).place(x=348,y=50)
            lb4 = Label(show,text="Date_And_Time",width=20,bg="white",bd=5).place(x=521,y=50)
            
        
            for i in range(0,var.rowcount):
                lb1 = Label(show,text=v[i][0],width=20,bg="white",bd=5).place(x=2,y=vary)
                lb2 = Label(show,text=v[i][1],width=20,bg="white",bd=5).place(x=175,y=vary)
                lb3 = Label(show,text=v[i][2],width=20,bg="white",bd=5).place(x=348,y=vary)
                lb4 = Label(show,text=v[i][3],width=20,bg="white",bd=5).place(x=521,y=vary)
        
                vary+=30
            
            
            print(vary)
            conn.commit()
        else:
            messagebox.showinfo("message","match not found")
            conn.close()

win=Tk()
win.geometry("540x300")
win.config(bg="lightpink")
win.title('fund records')

frame2=Frame(win,width=500,height=200,highlightbackground="green")
frame2.place(x=20,y=20)
lb1=Label(frame2,text="FUND RECORDS",font=('arial',20,'bold'))
lb1.place(x=140,y=20)

lb=Label(win,text='ACCOUNT NUMBER',font=('arial',15,'bold'),bd=10)
lb.place(x=60,y=115)
an=StringVar()
tb=Entry(win,textvariable=an)
tb.place(x=340,y=128)

btn1=Button(win,text=" CHECK ",command=tf,bg='orchid',font=('arial',10,'bold'),width=40,height=2,relief="ridge",activebackground="purple",activeforeground="white",bd=10)
btn1.place(x=100,y=230)

win.mainloop()
