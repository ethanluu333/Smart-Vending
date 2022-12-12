import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os




class Login:

    def __init__(self):
        self.loginw = Tk()
        self.loginw.title("Login")
        width = 675
        height = 900
        screen_width = self.loginw.winfo_screenwidth()
        screen_height = self.loginw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.loginw.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.loginw.resizable(0, 0)
        self.loginw.protocol('WM_DELETE_WINDOW', self.__login_del__)
        self.loginw.config(bg="white")
        image = Image.open("images/T7startlogo.png")
        resize_image = image.resize((675, 200))
        self.img = ImageTk.PhotoImage(resize_image)

        self.bgimage = Label(
            self.loginw,
            image=self.img,
            border=0
        )
        self.bgimage.pack()

        spacer1 = Label(height=10, bg="white")
        spacer1.pack()

        self.logintable()
        self.username = StringVar(value="Username")
        self.password = StringVar(value="Password")

        self.obj()

        vmbuttonspacer1 = Label(height=15, bg="white")
        vmbuttonspacer1.pack()

        self.vm_buttons()
    
    def vm_buttons(self):
        self.vmframe = Frame(self.loginw, bg="white", height=675, width=900, border="0")
        self.vmframe.pack()

        def openv1():
            os.system('python main2.py')
            


        vm1 = Image.open("images/vm1.png")
        resize_vm1 = vm1.resize((100, 50))
        self.vm1image = ImageTk.PhotoImage(resize_vm1)
        self.vm1imagebutton = Button(
            self.vmframe,
            image=self.vm1image,
            border=0,
            bg="white",
            command=openv1
        )
        self.vm1imagebutton.pack(side="left")

        vm2 = Image.open("images/vm2.png")
        resize_vm2 = vm2.resize((100, 50))
        self.vm2image = ImageTk.PhotoImage(resize_vm2)
        self.vm2imagebutton = Button(
            self.vmframe,
            image=self.vm2image,
            border=0,
            bg="white"
        )
        self.vm2imagebutton.pack(side="left")

        vm3 = Image.open("images/vm3.png")
        resize_vm3 = vm3.resize((100, 50))
        self.vm3image = ImageTk.PhotoImage(resize_vm3)
        self.vm3imagebutton = Button(
            self.vmframe,
            image=self.vm3image,
            border=0,
            bg="white"
        )
        self.vm3imagebutton.pack(side="left")


    def __login_del__(self):
        if messagebox.askyesno("Quit", " Leave application?"):
            self.loginw.destroy()
            exit(0)

    def logintable(self):
        self.base = sqlite3.connect("login.db")
        self.cur = self.base.cursor()
        self.cur.execute(
            "CREATE TABLE if not exists users (name varchar (20), phone_no number, gender varchar(10), username varchar (20),password varchar (20) NOT NULL,account_type varchar ( 10 ) NOT NULL,PRIMARY KEY(username));")

    def obj(self):
        self.loginframe = Frame(self.loginw, bg="white", height=675, width=900, border="0")
        self.loginw.bind('<Return>', self.checkuser)
        self.loginframe.pack()

        self.toplabel = Label(self.loginframe, fg="#57a1f8", bg="white", anchor="center", text="Login",
                              font=("Arial, 20"))
        self.toplabel.pack()

        self.spacer2 = Label(self.loginframe, height=2, bg="white")
        self.spacer2.pack()

        self.us = Entry(self.loginframe, width=30, bg="#ffffff", textvariable=self.username, border=0, justify="left",
                        font=("Arial, 16"))
        self.us.pack()
        self.usborder = Frame(self.loginframe, height=2, bg="black")
        self.usborder.pack(fill="x")

        self.spacerbetweenentry = Label(self.loginframe, height=2, bg="white")
        self.spacerbetweenentry.pack()

        self.pa = Entry(self.loginframe, width=30, bg="#ffffff", textvariable=self.password, border=0, justify="left",
                        font=("Arial, 16"))
        self.pa.pack()
        self.paborder = Frame(self.loginframe, height=2, bg="black")
        self.paborder.pack(fill="x")

        self.us.bind('<Button-1>', self.onclick)
        self.pa.bind('<Button-1>', self.onclick1)

        self.spacerabovebutton = Label(self.loginframe, height=1, bg="white")
        self.spacerabovebutton.pack()

        self.signin = Button(self.loginframe, width=20, pady=10, text="Sign in", bg="#57a1f8", fg="white", border=0,
                             command=self.checkuser)
        self.signin.pack(fill="x")

    def checkuser(self, event=0):
        s = self.username.get()
        s1 = self.password.get()
        s = s.upper()
        s1 = s1.upper()
        self.cur.execute("select * from users where username=? and password=? ", (s, s1))
        list_ = self.cur.fetchall()
        if len(list_) > 0:
            self.success()
        else:
            self.fail()

    def success(self):
        self.loginw.quit()

    def fail(self):
        messagebox.showerror("Error", "The username or password is incorrect")

    def reguser(self):
        self.toplabel.config(text="Register", fg="white")
        self.toplabel.place(x=40, y=25)
        self.username.set("Choose your username")
        self.password.set("Create a password")
        self.signin.config(text="Ok", command=self.insert)
        self.register = Button(self.loginframe, width=20, text="Back", bg="#9933ff", fg="white",
                               command=self.revert, font="Arial")
        self.register.place(x=35, y=320)
        self.signin.config()
        self.signin.place(x=35, y=260)
        self.pa.config(show='')
        self.loginw.focus()
        self.loginw.bind('<Return>', self.insert)
        self.loginw.title('Register')

    def insert(self, event=0):
        s = self.username.get()
        s1 = self.password.get()
        s = s.upper()
        s1 = s1.upper()
        self.cur.execute("select username from users where username = ?", (s,))
        list_ = self.cur.fetchall()
        if len(list_) > 0:
            messagebox.showerror("Error", "Username already exist")
            self.username.set('Choose your username')
            self.loginw.focus()
            return
        if (len(s) == 0 or len(s1) == 0 or len(s) > 20 or len(
                s1) > 20 or s1 == "CREATE A PASSWORD" or s == 'CHOOSE YOUR USERNAME'):
            messagebox.showerror("Error", "Invalid username or password")
            self.username.set('Choose your username')
            self.password.set('Create a password')
            self.pa.config(show='')
            self.loginw.focus()
            return
        else:
            self.cur.execute("insert into users values(?,?,?)", (s, s1, 'USER'))
            messagebox.showinfo("Success", "User registered")
            self.base.commit()
            self.revert()
            self.loginw.state('withdraw')
            self.tree.delete(*self.tree.get_children())
            self.getusers()

    def revert(self):
        self.toplabel.config(text="Login")
        self.toplabel.place(x=75, y=25)
        self.signin.config(text="Sign in", command=self.checkuser)
        self.register.config(text="Register", command=self.reguser)
        self.username.set('Username')
        self.password.set('Password')
        self.pa.config(show='')
        self.signin.config(state=NORMAL)
        self.loginw.focus()
        self.loginw.bind('<Return>', self.checkuser)
        self.signin.place(x=35, y=290)
        self.loginw.title('Login')
        self.loginw.state('withdraw')

    def onclick(self, event):
        if self.username.get() == "Username" or self.username.get() == "Choose your username":
            self.us.delete(0, "end")

    def onclick1(self, event):
        if self.password.get() == "Password" or self.password.get() == "Create a password":
            self.pa.delete(0, "end")
            self.pa.config(show="*")


'''           
#TEST LOGIN
w=login()
w.base.commit()
w.loginw.mainloop()
'''
