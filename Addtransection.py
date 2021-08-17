from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *


class transection:


    def __init__(self, email):
        self.email = email

        self.top = Toplevel()
        self.top.title("ADD Transection")
        self.top.geometry('500x500')
        self.top.label_3 = Label(self.top, text="ADD Transection", font=("Constantia", "25", "italic", 'bold')).pack(
            side=TOP, pady=20)
        Label(self.top, text="Enter Amount : ").pack(side=TOP, pady=10)
        self.amount = Entry(self.top)
        self.amount.pack(side=TOP, pady=10)

        Label(self.top, text="Remarks").pack(side=TOP, pady=10)
        self.remarks = Text(self.top, width=30, height=2)
        self.remarks.pack(side=TOP)

        conn = Connect(host='127.0.0.1', user='root', password='', database='expensemanager')
        cr = conn.cursor()
        q = f'select categoryname from category where emailID = "{self.email}"'
        cr.execute(q)
        result = cr.fetchall()
        x = []
        for i in result:
            x.append(i[0])

        Label(self.top, text="Type : ").pack(side=TOP, pady=10)
        self.type = Combobox(self.top, values=x)
        self.type.pack(side=TOP, pady=10)

        self.Button1 = Button(self.top, text='ADD', command=self.unewcat)
        self.Button1.pack(side=TOP, pady=10)


    def unewcat(self):
        self.cnam = self.amount.get()
        self.catdes = self.remarks.get(1.0, END)
        self.typ = self.type.get()

        conn = Connect(host='127.0.0.1', user='root', password='', database='expensemanager')
        cr = conn.cursor()

        if self.cnam == "" and self.catdes == "" and self.typ == "":
            showinfo("ADD CATEGORY", 'Please input correct details')


        else:

            q1 = f'select ID from category where CategoryName ="{self.typ}"'
            cr.execute(q1)
            result1 = cr.fetchone()

            for i in result1:
                new = i

            q = f'insert into transection value(null,"{self.cnam}","{self.catdes}","{new}")'
            cr.execute(q)
            print(q)
            conn.commit()
            self.top.destroy()
