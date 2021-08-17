from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *
from datetime import date
from tkcalendar import *
from datetime import datetime

class add:



    def __init__(self,email):
        self.email = email

        self.top = Toplevel()
        self.top.title("ADD Budget")
        self.top.geometry('500x600')
        self.top.label_3 = Label(self.top, text="Budget", font=("Constantia", "25", "italic", 'bold')).pack(
            side=TOP, pady=20)
        Label(self.top, text="Enter Amount : ").pack(side=TOP, pady=10)
        self.amount = Entry(self.top)
        self.amount.pack(side=TOP, pady=10)

        Label(self.top, text="Select Date : ").pack(side=TOP, pady=10)
        self.cal = DateEntry(self.top, width=12,
                        background='darkblue', foreground='white', borderwidth=2)
        self.cal.pack(padx=10, pady=10)



        self.Button1 = Button(self.top, text='ADD Budget', command=self.addbudget)
        self.Button1.pack(side=TOP, pady=10)

    def addbudget(self):

        today = date.today()
        new5 = datetime.strftime(today, '%m/%d/%y')
        self.date = self.cal.get()

        conn = Connect(host='127.0.0.1', user='root', password='', database='expensemanager')
        cr = conn.cursor()

        if self.amount.get() == ""  :
            showinfo("ADD CATEGORY", 'Please input correct details')


        else:
            checkbudget = f'select * from budget where emailId = "{self.email}" between "{new5}" and "{self.date}"'
            cr.execute(checkbudget)
            result=cr.fetchall()

            if result == None or result == ():
                q = f'insert into budget value(null,"{self.amount.get()}","{self.date}","{self.email}")'
                cr.execute(q)
                print(q)
                conn.commit()
                showinfo('Budget','Budget Added')
                self.top.destroy()

            else:
                showinfo('Budget',"You cannot add new budget for same month")




