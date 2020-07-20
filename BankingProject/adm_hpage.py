from tkinter import *
import os
win=Tk()
win.geometry("970x600")
win.config(bg="lightpink")

def withdraw_cash():
    os.system("Withdraw_tk.py")

def Deposit():
    os.system("Deposit.py")

def fast_cash():
    os.system("fast_cash.py")

def change_pin():
    os.system("change_pin.py")

def mini_statement():
    os.system("Ministmnt.py")

def update_contact():
    os.system("Update_contact.py")

def transfer_fund():
    os.system("transfer_fund.py")

def change_nominee():
    os.system("change_nominee.py")

def block_account():
    os.system("block_account.py")

def balance_enquiry():
    os.system("balance_enquiry.py")

def fund_records():
    os.system("fund_records.py")

lb=Label(win,text='ROYAL BANK ATM',font=('arial',40,'bold'),background='lightpink')
lb.place(x=250,y=20)

btn1=Button(win,text="DEPOSIT CASH ",command=Deposit,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn1.place(x=20,y=110)

btn2=Button(win,text="WITHDRAW CASH ",command=withdraw_cash,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn2.place(x=310,y=180)

btn3=Button(win,text="BALANCE ENQUIRY ",command=balance_enquiry,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn3.place(x=20,y=250)

btn4=Button(win,text="TRANSFER FUND ",command=transfer_fund,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn4.place(x=20,y=390)

btn5=Button(win,text="MINISTATEMENT ",command=mini_statement,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn5.place(x=600,y=110)

btn6=Button(win,text="FAST CASH ",command=fast_cash,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn6.place(x=600,y=250)

btn7=Button(win,text="CHANGE PIN ",command=change_pin,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn7.place(x=600,y=390)

btn8=Button(win,text="UPDATE CONTACT ",command=update_contact,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn8.place(x=310,y=320)

btn9=Button(win,text="CHANGE NOMINEE ",command=change_nominee,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn9.place(x=20,y=530)

btn10=Button(win,text="BLOCK ACCOUNT ",command=block_account,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn10.place(x=600,y=530)

btn11=Button(win,text=" FUND RECORDS ",command=fund_records,font=('arial',10,'bold'),activebackground="purple",activeforeground="white",width=40,height=2,relief="ridge",bd=10)
btn11.place(x=310,y=460)

win.mainloop()
