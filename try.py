import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pymysql import *
import numpy as np

conn = connect(host='127.0.0.1', user='root', password='', database='expensemanager')
cr = conn.cursor()

name = []
values = []
m = ("Automobile", "Entertainment", "Family", "Insurance", "Loan", "Personal", "Travel", 'Others')
for i in m:
    q = 'select sum(amount) from expences where category="{}"'.format(i)
    cr.execute(q)
    resultFinal = cr.fetchone()
    if resultFinal[0] != None:
        name.append(i)
        values.append(resultFinal[0])
print(name, values)
# data1 = {'Country': ['US', 'CA', 'GER', 'UK', 'FR'],
#          'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]
#          }
# df1 = DataFrame(data1, columns=['Country', 'GDP_Per_Capita'])
#
#

root = tk.Tk()
y = np.array(values)
mylabels = name

fig = plt.figure(figsize=(6, 6), dpi=100)
fig.set_size_inches(6, 4)

plt.pie(y, labels=mylabels)
plt.axis('equal')
canvasbar = FigureCanvasTkAgg(fig,root)
canvasbar.draw()
canvasbar.get_tk_widget().place(relx=0.3,rely=0.3, anchor=tk.CENTER)
# canvas1 = FigureCanvasTkAgg(figure1,root)
# canvas1.draw()
# canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
plt.legend()
# plt.show()
# figure1 = plt.Figure(figsize=(6, 5), dpi=100)
# ax1 = figure1.add_subplot(111)
# bar1 = FigureCanvasTkAgg(figure1, root)
# bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()
# df1.plot(kind='bar', legend=True, ax=ax1)
# ax1.set_title('Country Vs. GDP Per Capita')


root.mainloop()


def barChart():
    q = 'select date,amount from expences'
    cr.execute(q)
    result1 = cr.fetchall()
    d = {'January':0,'Febuary':0,'March':0,'April':0,'May':0,'June':0,'July':0,'August':0,'September':0,'October':0,'November':0,'December':0}
    for i in range(0,len(result1)):
        d1 = str(result1[i][0]).split('/')
        if d1[1] == '01':
            d['January'] += result1[i][1]
        elif d1[1] == '02':
            d['Febuary'] += result1[i][1]
        elif d1[1] == '03':
            d['March'] += result1[i][1]
        elif d1[1] == '04':
            d['April'] += result1[i][1]
        elif d1[1] == '05':
            d['May'] += result1[i][1]
        elif d1[1] == '06':
            d['June'] += result1[i][1]
        elif d1[1] == '07':
            d['July'] += result1[i][1]
        elif d1[1] == '08':
            d['August'] += result1[i][1]
        elif d1[1] == '09':
            d['September'] += result1[i][1]
        elif d1[1] == '10':
            d['October'] += result1[i][1]
        elif d1[1] == '11':
            d['November'] += result1[i][1]
        elif d1[1] == '12':
            d['December'] += result1[i][1]
    print(d)
    name1 = []
    value1 = []
    for i in d.keys():
        name1.append(i)
        value1.append(d[i])
    x = np.array(name1)
    y = np.array(value1)
    print(x,y)
    plt.bar(x, y, color = "#4CAF50")
    plt.show()

barChart()