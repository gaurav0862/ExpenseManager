from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *
from datetime import date, datetime


class income:


    def __init__(self, email):
        self.email = email

        self.top = Toplevel()
        self.top.title("ADD Transection")
        self.top.geometry('500x600')
        self.top.label_3 = Label(self.top, text="ADD Income", font=("Constantia", "25", "italic", 'bold')).pack(
            side=TOP, pady=20)
        Label(self.top, text="Enter Amount : ").pack(side=TOP, pady=10)
        self.amount = Entry(self.top)
        self.amount.pack(side=TOP, pady=10)

        Label(self.top, text="Payer : ").pack(side=TOP, pady=10)
        self.Payer = Entry(self.top)
        self.Payer.pack(side=TOP, pady=10)

        Label(self.top, text="Remarks").pack(side=TOP, pady=10)
        self.remarks = Text(self.top, width=30, height=2)
        self.remarks.pack(side=TOP)


        Label(self.top, text="Category ").pack(side=TOP, pady=10)
        self.category = Combobox(self.top, values=("Salary","Personal Savings","Rents and Royalties","Pension","Account Transfer"),state='readonly')
        self.category.pack(side=TOP, pady=10)


        Label(self.top, text="Transection Type : ").pack(side=TOP, pady=10)
        self.type = Combobox(self.top, values=("Bank","Cash"),state='readonly')
        self.type.pack(side=TOP, pady=10)

        self.Button1 = Button(self.top, text='ADD', command=self.unewcat)
        self.Button1.pack(side=TOP, pady=10)


    def unewcat(self):
        self.cnam = self.amount.get()
        self.catdes = self.remarks.get(1.0, END)
        self.typ = self.type.get()

        date1 = date.today()
        new5 = datetime.strftime(date1, '%d/%m/%y')

        conn = Connect(host='127.0.0.1', user='root', password='', database='expensemanager')
        cr = conn.cursor()

        if self.cnam == "" and self.catdes == "" and self.typ == "":
            showinfo("ADD CATEGORY", 'Please input correct details')


        else:


            q = f'insert into income value(null,"{self.cnam}","{self.Payer.get()}","{self.catdes}","{self.category.get()}","{self.typ}","{self.email}","{new5}")'
            cr.execute(q)
            print(q)
            conn.commit()
            self.top.destroy()
