from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *


class expence:

    def __init__(self,email):
        self.email = email
        self.top=Toplevel()
        self.top.title("View Expence")
        self.top.label_3 = Label(self.top, text="Expences",font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,pady=20)
        self.top.waraper = LabelFrame(self.top,text="Income View")
        self.top.waraper.pack(fill="both", expand="yes", padx=50, pady=50)
        self.trv = Treeview(self.top.waraper, columns=(1,2,3,4,5,6), show="headings", height="5")
        self.trv.pack(padx=10, pady=50)
        self.trv.heading(1, text="ID")
        self.trv.heading(2, text="Amount")
        self.trv.heading(3, text="Payee")
        self.trv.heading(4, text="Description")
        self.trv.heading(5, text="Category")
        self.trv.heading(6, text="Transection Type")
        self.trv.bind("<Double-1>", self.delcat)
        conn = Connect(host='127.0.0.1', user='root', password='', database='expensemanager')
        cr = conn.cursor()
        q = f'select  id,amount,payee,remarks,category,TransectionType from expences where emailId ="{self.email}"'
        cr.execute(q)
        self.result = cr.fetchall()

        for i in self.trv.get_children():
            self.trv.delete(i)

        for i in self.result:
            self.trv.insert("", END, value=i)


    def delcat(self, event):
        self.temp_data = self.trv.item(self.trv.focus())['values']

        self.new = messagebox.askquestion("Delete", "Are you sure?")
        if self.new == "yes":
            conn = Connect(host='127.0.0.1', user='root', password='', database='expensemanager')
            cr = conn.cursor()
            q = 'delete from expences where id = "{}"'.format(self.temp_data[0])
            print(q)
            cr.execute(q)
            conn.commit()
            self.result = cr.fetchone()
        else:
            pass
