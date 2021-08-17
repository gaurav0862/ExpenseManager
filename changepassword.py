from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

class change:

    def __init__(self,email):
        self.email =email

        self.top = Toplevel()
        self.top.state("zoomed")
        self.top.title("Add Admin")

        self.top.geometry('500x500')
        self.labl = Label(self.top, text="ADD ADMIN", font=("Gabriola", "25", "italic", 'bold')).pack(side=TOP, pady=5)
        self.label_1 = Label(self.top, text="EMAIL ID : ").pack(side=TOP, pady=10)

        self.EmailID = Entry(self.top)
        self.EmailID.insert(0,email)

        self.EmailID.pack(side=TOP, pady=10)

        self.lable_2 = Label(self.top, text="Password : ").pack(side=TOP, pady=10)
        self.password = Entry(self.top)
        self.password.pack(side=TOP, pady=10)

        Button(self.top, text='Update', command=self.unewcat).pack(side=TOP, pady=10)

    def unewcat(self):

        self.password1 =self.password.get()
        print(self.password1)

        conn = Connect(host='127.0.0.1', user='root', password='', database='expensemanager')
        cr = conn.cursor()

        q = f'select Password from userdata where email = "{self.email}"'
        cr.execute(q)
        result = cr.fetchone()
        for i in result:

            self.password2 =i


        if self.password2 == self.password1:
            showerror('change password',"Paaword should not be same as last password")

        elif self.password1 == "":

            showerror("password","Please enter valid input")

        else:
            q1 = f'update userdata set Password = "{self.password1}" where email="{self.email}"'
            print(q1)
            cr.execute(q1)
            conn.commit()
            self.top.destroy()
            showinfo('Change Password',"Password changed successfully")

