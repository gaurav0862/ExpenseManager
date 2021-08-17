
from tkinter import *
from tkinter.messagebox import *
from pymysql import *
from PIL import Image,ImageTk
import datetime



import Home


class login:

    def __init__(self):

        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Login")
        self.img = (Image.open("Image_Resources/3.png"))
        self.resized_image = self.img.resize((500, 600), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas1 = Canvas(self.root, width=500, height=500)
        self.canvas1.place(x=0, y=0)
        self.root.resizable(0, 0)

        self.canvas1.create_image(0, 0, image=self.new_image, anchor="nw")
        self.canvas1.create_text(250, 50, text="Login", font=('Ink Free', 50, "bold",))
        self.canvas1.create_text(200, 135, text="ENTER EMAIL ID : ")

        self.emailID = Entry(self.root)
        self.emailID.place(x=250, y=125)
        self.canvas1.create_text(192, 180, text="ENTER PASSWORD : ")
        self.password = Entry(self.root, show='*')
        self.password.place(x=250, y=170)
        self.btn = Button(self.root, text="LOGIN", command=self.login1,width=10)
        self.btn.place(x=230, y=225)
        self.btn1 = Button(self.root, text="New User?", command=self.SignUp,width=10)
        self.btn1.place(x=229, y=260)

        self.root.mainloop()


    def SignUp(self):

        self.top = Toplevel
        self.root.geometry('500x500')
        self.root.title("New User")
        self.img = (Image.open("Image_Resources/3.png"))
        self.resized_image = self.img.resize((500, 500), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(self.resized_image)
        self.canvas1 = Canvas(self.root, width=500, height=500)
        self.canvas1.place(x=0, y=0)
        self.root.resizable(0, 0)

        self.canvas1.create_image(0, 0, image=self.new_image, anchor="nw")
        self.canvas1.create_text(250, 50, text="Register", font=('Ink Free', 50, "bold",))

        self.canvas1.create_text(200, 135, text="Name : ",font=("arial",10,"bold") )
        self.Name = Entry(self.root)
        self.Name.place(x=250, y=125)

        self.canvas1.create_text(200, 170, text="Email : ",font=("arial",10,"bold"))
        self.Email1 = Entry(self.root)
        self.Email1.place(x=250, y=160)


        self.canvas1.create_text(200, 205, text="Mobile : ",font=("arial",10,"bold"))
        self.Mobile = Entry(self.root)
        self.Mobile.place(x=250, y=195)

        self.canvas1.create_text(200, 240, text="Password : ",font=("arial",10,"bold") )
        self.password1 = Entry(self.root)
        self.password1.place(x=250, y=230)

        self.btn1 = Button(self.root, text="Register?", command=self.register, width=10)
        self.btn1.place(x=229, y=275)

    def register(self):



        conn = connect(host="127.0.0.1",user='root',password="",database="expensemanager")
        cr = conn.cursor()


        if self.Name.get()=="" and self.Email1.get()=="" and self.Mobile.get()=="" and self.password.get() == "":
            showerror('Error', "Provide all information" )

        else:
            Mobile = self.Mobile.get()
            password = self.password1.get()
            conn = connect(host="127.0.0.1", user='root', password="", database="expensemanager")
            cr = conn.cursor()

            q = f'insert into userdata values("{self.Email1.get()}","{self.Name.get()}","{Mobile}","{password}",NULL,NULL,NULL,NULL,NULL)'
            cr.execute(q)
            conn.commit()

            showinfo("",'User Added Successfully')


    def login1(self):

        conn = connect(host="127.0.0.1",user="root",password="",database="expensemanager")
        cr = conn.cursor()

        self.lgv = self.emailID.get()
        self.lgv_1 = self.password.get()

        if self.lgv == "" and self.lgv_1 == "" :
            showinfo("Login", "Please provide id password")

        else:
            q = 'select * from userData where email="{}" and Password="{}" '.format(self.lgv, self.lgv_1)
            cr.execute(q)
            self.result = cr.fetchall()

            for i in self.result:
                self.username = i[1]

            if self.result == None or self.result == ():
                showinfo('Login', "Invalid Input")
            else:

                self.time_1 = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
                print(self.time_1)

                q = 'update userData set lastLogin="{}" where email="{}"'.format(self.time_1, self.lgv)
                self.result = cr.execute(q)
                conn.commit()
                showinfo('Login', "Login Sucessfull")
                self.root.destroy()
                Home.demo(self.username,self.lgv)







obj=login()