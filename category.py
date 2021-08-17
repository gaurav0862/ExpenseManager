from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

class addcat:

    def __init__(self,email):
        self.email = email

        self.top = Toplevel()
        self.top.title("ADD ADMIN")
        self.top.geometry('500x500')
        self.top.label_3 = Label(self.top, text="ADD CATEGORY", font=("Constantia", "25", "italic", 'bold')).pack(side=TOP,

                                                                                                              pady=20)
        Label(self.top, text="Category Name : ").pack(side=TOP, pady=10)
        self.categoryName = Entry(self.top)
        self.categoryName.pack(side=TOP, pady=10)


        Label(self.top, text="Category Description").pack(side=TOP, pady=10)
        self.enp = Text(self.top, width=50, height=5)
        self.enp.pack(side=TOP)


        Label(self.top, text="Type : ").pack(side=TOP, pady=10)
        self.type = Combobox(self.top,values=("Bank","Cash","Expence","investment","assets","Income"))
        self.type.pack(side=TOP, pady=10)


        self.Button1 = Button(self.top, text='ADD', command=self.unewcat)
        self.Button1.pack(side=TOP, pady=10)


    def unewcat(self):
        self.cnam = self.categoryName.get()
        self.catdes = self.enp.get(1.0, END)
        self.typ =self.type.get()
        self.eml = self.email
        conn = Connect(host='127.0.0.1', user='root', password='', database='expensemanager')
        cr = conn.cursor()
        if self.cnam=="" and self.catdes=="":
            showinfo("ADD CATEGORY",'Please input correct details')
        else:
            q = F'insert into category values(NULL,"{self.cnam}","{self.catdes}","{self.typ}","{self.eml}")'
            cr.execute(q)
            print(q)
            conn.commit()
            self.top.destroy()