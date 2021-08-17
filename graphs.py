from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pymysql import *
import numpy as np

class graphs:



    def __init__(self,email):

        self.top = Toplevel()
        self.top.configure(bg='#03f4fc')
        Label(self.top,text='Category Wise Expenses',font=("Constantia", "25", "italic", 'bold')).place(x=150,y=50)
        Label(self.top,text='Month Wise Expenses',font=("Constantia", "25", "italic", 'bold')).place(x=850,y=50)
        self.top.geometry('1366x680+0+0')
        self.top.resizable(0, 0)
        self.email = email
        conn = connect(host='127.0.0.1', user='root', password='', database='expensemanager')
        cr = conn.cursor()

        name = []
        values = []
        m = ("Automobile", "Entertainment", "Family", "Insurance", "Loan", "Personal", "Travel", 'Others')
        for i in m:
            q = 'select sum(amount) from expences where category="{}" and emailid="{}"'.format(i,self.email)
            cr.execute(q)
            resultFinal = cr.fetchone()
            if resultFinal[0] != None:
                name.append(i)
                values.append(resultFinal[0])


        y = np.array(values)
        mylabels = name

        fig = plt.figure(figsize=(6, 6), dpi=100)
        fig.set_size_inches(6, 4)

        plt.pie(y, labels=mylabels)
        plt.axis('equal')
        canvasbar = FigureCanvasTkAgg(fig,self.top)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(relx=0.25,rely=0.5, anchor=CENTER)
        plt.legend()


        q = 'select date,amount from expences'
        cr.execute(q)
        result1 = cr.fetchall()
        d = {'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'June': 0, 'July': 0, 'Aug': 0, 'Sept': 0, 'Oct': 0,
             'Nov': 0, 'Dec': 0}
        for i in range(0, len(result1)):
            d1 = str(result1[i][0]).split('/')
            if d1[1] == '01':
                d['Jan'] += result1[i][1]
            elif d1[1] == '02':
                d['Feb'] += result1[i][1]
            elif d1[1] == '03':
                d['Mar'] += result1[i][1]
            elif d1[1] == '04':
                d['Apr'] += result1[i][1]
            elif d1[1] == '05':
                d['May'] += result1[i][1]
            elif d1[1] == '06':
                d['June'] += result1[i][1]
            elif d1[1] == '07':
                d['July'] += result1[i][1]
            elif d1[1] == '08':
                d['Aug'] += result1[i][1]
            elif d1[1] == '09':
                d['Sept'] += result1[i][1]
            elif d1[1] == '10':
                d['Oct'] += result1[i][1]
            elif d1[1] == '11':
                d['Nov'] += result1[i][1]
            elif d1[1] == '12':
                d['Dec'] += result1[i][1]

        name1 = []
        value1 = []
        for i in d.keys():
            name1.append(i)
            value1.append(d[i])
        x = np.array(name1)
        y = np.array(value1)


        fig = plt.figure(figsize=(6, 6), dpi=100)
        fig.set_size_inches(6, 4)

        plt.bar(x, y, color="#4CAF50")
        canvasbar = FigureCanvasTkAgg(fig, self.top)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(relx=0.75, rely=0.5, anchor=CENTER)

        plt.show()

