from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image,ImageTk
from tkinter.messagebox import *
from tkinter.ttk import Combobox, Treeview
from pymysql import *

import Addexpence
import Addtransection
import ViewBudget
import category
import changepassword
import viewcategory
import AddIncome
import viewincome
import Viewexpence
import Budget
import graphs

class demo:

    def __init__(self,name,email):
        self.root = Tk()
        self.root.title("Home Page")
        self.email=email
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry('1366x680+0+0')
        self.root.resizable(0, 0)
        self.homeimg = Image.open("Image_Resources/expencelogin.jpg")
        self.resized_image = self.homeimg.resize((1366,748),Image.ANTIALIAS)
        self.newimg = ImageTk.PhotoImage(self.resized_image)
        self.canvas1 = Canvas(self.root)
        self.canvas1.pack(fill="both", expand=True)

        self.canvas1.create_image(0, 0, image=self.newimg, anchor='nw')


        self.canvas1.create_text(700, 50, text=f"Welcome {name}", font=("Gabriola", "50", "italic", 'bold'),fill="white")



        self.menu_1 = Menu(self.root)
        self.root.config(menu=self.menu_1)

        self.admin = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Profile", menu=self.admin)
        self.admin.add_command(label="Change Password", command=lambda: changepassword.change(self.email))
        # self.admin.add_command(label="", command=lambda: "")
        self.admin.add_command(label="Logout", command= lambda : self.root.destroy())


        self.Income = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Income", menu=self.Income)
        self.Income.add_command(label="Add Income", command=lambda: AddIncome.income(email))
        self.Income.add_command(label="View Income", command=lambda: viewincome.income(email))

        self.Expenses = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Expence", menu=self.Expenses)
        self.Expenses.add_command(label="Add Expence", command=lambda: Addexpence.expence(email))
        self.Expenses.add_command(label="View Expence", command=lambda: Viewexpence.expence(email))

        self.Budget = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_cascade(label="Budget", menu=self.Budget)
        self.Budget.add_command(label="Add Budget", command=lambda: Budget.add(email))
        self.Budget.add_command(label="View Budget", command=lambda: ViewBudget.view(email))

        # self.Graphs = Menu(self.menu_1, tearoff=0)
        self.menu_1.add_command(label="Graphs", command=lambda: graphs.graphs(email))
        # self.Graphs.add_command(label="Show Graphs", )






        self.root.mainloop()

# demo()