from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *
from datetime import *
from datetime import date



class expence:


    def __init__(self, email):
        self.email = email

        self.top = Toplevel()
        self.top.title("ADD Transection")
        self.top.geometry('500x500')
        self.top.label_3 = Label(self.top, text="ADD Expense", font=("Constantia", "25", "italic", 'bold')).pack(
            side=TOP, pady=20)

        conn = Connect(host='127.0.0.1', user='root', password='', database='expensemanager')
        cr = conn.cursor()

        q1 = f'select sum(amount) from expences where emailID = "{self.email}"'
        cr.execute(q1)
        result = cr.fetchone()
        self.expencetotal = result[0]


        q = f'select amount from income where emailID = "{"admin@gmail.com"}"'
        cr.execute(q)

        result = cr.fetchall()
        self.total = 0
        for i in result:
            self.total = self.total + int(i[0])

        self.incometotal = self.total - self.expencetotal

        Label(self.top, text="Income : ").pack(side=TOP, pady=10)
        self.income = Entry(self.top)
        self.income.insert(0,self.incometotal)
        self.income.pack(side=TOP, pady=10)

        Label(self.top, text="Enter Amount : ").pack(side=TOP, pady=10)
        self.amount = Entry(self.top)
        self.amount.pack(side=TOP, pady=10)

        Label(self.top, text="Payee : ").pack(side=TOP, pady=10)
        self.payee = Entry(self.top)
        self.payee.pack(side=TOP, pady=10)

        Label(self.top, text="Description : ").pack(side=TOP, pady=10)
        self.remarks = Text(self.top, width=30, height=2)
        self.remarks.pack(side=TOP)

        Label(self.top, text="Category : ").pack(side=TOP, pady=10)
        self.category = Combobox(self.top, values=("Automobile","Entertainment","Family","Insurance","Loan","Personal","Travel"))
        self.category.pack(side=TOP, pady=10)

        Label(self.top, text="Transection Type : ").pack(side=TOP, pady=10)
        self.transection = Combobox(self.top, values=("Cash","Check","Credit Card"))
        self.transection.pack(side=TOP, pady=10)

        self.Button1 = Button(self.top, text='ADD', command=self.unewcat)
        self.Button1.pack(side=TOP, pady=10)


    def unewcat(self):

        print(f'expence{self.expencetotal}')
        date123 =date.today()
        new5 = datetime.strftime(date123, '%d/%m/%y')
        conn = Connect(host='127.0.0.1', user='root', password='', database='expensemanager')
        cr = conn.cursor()

        budget = f'select * from budget where emailId = "{self.email}"'
        cr.execute(budget)
        result = cr.fetchall()
        for i in result:
            self.budgetdate =i[2]
            self.amount5 = i[1]

        self.limit = int(self.amount5)-int(self.expencetotal)


        if result == None or result== ():


            if self.amount.get() == "" and self.payee.get() == "" and self.category.get()=="" :
                showinfo("ADD CATEGORY", 'Please input correct details')


            else:

                q = f'insert into expences values(null,"{self.amount.get()}","{self.payee.get()}","{self.remarks.get(1.0, END)}","{self.category.get()}","{self.transection.get()}","{self.email}","{new5}")'
                cr.execute(q)
                print(q)
                conn.commit()
                total = self.incometotal - int(self.amount.get())
                showinfo('Expence',f'Your Remaining amount is "{total}" ')
                self.top.destroy()

        else:

            if self.amount.get() == "" and self.payee.get() == "" and self.category.get()=="" :
                showinfo("ADD CATEGORY", 'Please input correct details')


            elif new5 <= self.budgetdate:
                if self.limit > self.expencetotal:



                    q = f'insert into expences values(null,"{self.amount.get()}","{self.payee.get()}","{self.remarks.get(1.0, END)}","{self.category.get()}","{self.transection.get()}","{self.email}","{new5}")'
                    cr.execute(q)
                    print(q)
                    conn.commit()
                    total = self.incometotal - int(self.amount.get())
                    showinfo('Expence', f'Your Remaining amount is "{total}" ')
                    self.top.destroy()

                else:
                    question = askquestion('Budget','Budget Exceded! Do you want to add more expences?')

                    if question == 'yes' :
                        q = f'insert into expences values(null,"{self.amount.get()}","{self.payee.get()}","{self.remarks.get(1.0, END)}","{self.category.get()}","{self.transection.get()}","{self.email}","{new5}")'
                        cr.execute(q)
                        print(q)
                        conn.commit()
                        total = self.incometotal - int(self.amount.get())
                        showinfo('Expence', f'Your Remaining amount is "{total}" ')
                        self.top.destroy()

                    else:
                        pass



            elif new5 > self.budgetdate:


                    q = f'insert into expences values(null,"{self.amount.get()}","{self.payee.get()}","{self.remarks.get(1.0, END)}","{self.category.get()}","{self.transection.get()}","{self.email}","{new5}")'
                    cr.execute(q)
                    print(q)
                    conn.commit()
                    total = self.incometotal - int(self.amount.get())
                    showinfo('Expence', f'Your Remaining amount is "{total}" ')
                    self.top.destroy()




