import sqlite3
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from Addtional_features import MyCombobox
from PIL import Image, ImageTk
import datetime

# USER MENU
BACKGROUND_COLOR = "#57a1f8"
FORM_BG_COLOR = "#FFFFFF"
BG = "#ffffff"
FG = "#000000"
# NAV_COLOR = '#ffffff'
# NAV_TEXT_COLOR = '#000000'
NAV_COLOR = '#57a1f8'
NAV_TEXT_COLOR = '#ffffff'


class User:
    def __init__(self, main_win):
        self.main_window = main_win

    def user_mainmenu(self):
        self.mframe = Canvas(self.main_window, bg=NAV_COLOR, highlightthickness=1)
        self.mframe.grid(column=0, row=1, columnspan=1, rowspan=15)

        image1 = Image.open("images/items.png")
        resize_image4 = image1.resize((50, 50))
        self.mi1 = ImageTk.PhotoImage(resize_image4)
        self.accounts = Button(self.mframe, image=self.mi1, border=0, bg=NAV_COLOR, command=self.builditemtable)
        self.accounts.grid(column=0, row=1, padx=16, pady=(20, 0))
        self.label1 = Label(self.mframe, text="Items", bg=NAV_COLOR, fg=NAV_TEXT_COLOR)
        self.label1.grid(column=0, row=2, pady=(5, 10))

        image2 = Image.open("images/invoice.png")
        resize_image2 = image2.resize((50, 50))
        self.mi2 = ImageTk.PhotoImage(resize_image2)
        self.sales = Button(self.mframe, image=self.mi2, border=0, bg=NAV_COLOR,
                            command=self.make_invoice)
        self.sales.grid(column=0, row=3, pady=(10, 0))
        self.label2 = Label(self.mframe, text="Invoice", bg=NAV_COLOR, fg=NAV_TEXT_COLOR)
        self.label2.grid(column=0, row=4, pady=(5, 10))

        image3 = Image.open("images/change user.png")
        resize_image3 = image3.resize((50, 50))
        self.mi3 = ImageTk.PhotoImage(resize_image3)
        self.changeuser = Button(self.mframe, image=self.mi3, border=0, bg=NAV_COLOR)
        self.changeuser.grid(column=0, row=5, pady=(10, 0))
        self.label3 = Label(self.mframe, text="Sign Out", bg=NAV_COLOR, fg=NAV_TEXT_COLOR)
        self.label3.grid(column=0, row=6, pady=(5, 15))

        image4 = Image.open("images/quit.png")
        resize_image4 = image4.resize((50, 50))
        self.mi4 = ImageTk.PhotoImage(resize_image4)
        self.logout = Button(self.mframe, image=self.mi4, border=0, bg=NAV_COLOR)
        self.logout.grid(column=0, row=7, pady=(10, 0))
        self.label4 = Label(self.mframe, text="Quit", bg=NAV_COLOR, fg=NAV_TEXT_COLOR)
        self.label4.grid(column=0, row=8, pady=(5, 218))

        self.tableframe1 = Frame(self.main_window, width=150, height=600, bg="#ffffff")
        self.tableframe1.place(x=1230, y=180, anchor=NE)
        self.tableframe1info = self.tableframe1.place_info()
        self.tableframe = Frame(self.main_window, width=350, height=700, bg="#ffffff")
        self.tableframe.place(x=1070, y=230, anchor=NE)
        self.tableframeinfo = self.tableframe.place_info()
        self.entryframe = Frame(self.main_window, width=800, height=350, bg="#ffffff")
        self.entryframe.place(x=810, y=410)
        self.entryframeinfo = self.entryframe.place_info()
        self.entryframe1 = Frame(self.main_window, width=500, height=350, bg="#ffffff")
        self.entryframe1.place(x=230, y=410)
        self.entryframe1info = self.entryframe1.place_info()
        self.make_invoice()

    def active(self, label):
        self.label1.config(fg='#ffffff')
        self.label2.config(fg="#ffffff")
        self.label3.config(fg="#ffffff")
        self.label4.config(fg="#ffffff")
        label.config(fg='#00ffff')

    def builditemtable(self):
        self.entryframe.place_forget()
        self.entryframe1.place_forget()
        self.tableframe.place(self.tableframeinfo)
        self.tableframe1.place_forget()
        self.active(self.label1)
        scrollbarx = Scrollbar(self.tableframe, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe, columns=("Product ID", "Product Name", "Description", "Category",
                                                           'Price', 'Stocks'), selectmode="extended", height=18,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100)
        self.tree.column('#6', stretch=NO, minwidth=0, width=100)
        self.tree.heading('Product ID', text="Product ID", anchor=W)
        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Description', text="Description", anchor=W)
        self.tree.heading('Category', text="Category", anchor=W)
        self.tree.heading('Price', text="Price", anchor=W)
        self.tree.heading('Stocks', text="Stocks", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.getproducts()

    def getproducts(self):
        self.cur.execute("SELECT * from products WHERE stocks < 7")
        productlist = self.cur.fetchall()
        for i in productlist:
            self.tree.insert('', 'end', values=i)

    def make_invoice(self):
        self.tableframe.place_forget()
        self.entryframe.place(self.entryframeinfo)
        self.entryframe1.place(self.entryframe1info)
        self.tableframe1.place(self.tableframe1info)
        self.active(self.label2)
        scrollbarx = Scrollbar(self.tableframe1, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.tableframe1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.tableframe1, columns=("Transaction ID", "Product ID", "Product Name",
                                                            'Quantity', 'Price', 'Date', 'Time'), selectmode="browse",
                                 height=6,
                                 yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=140)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150)
        self.tree.column('#3', stretch=NO, minwidth=0, width=170)
        self.tree.column('#4', stretch=NO, minwidth=0, width=130)
        self.tree.column('#5', stretch=NO, minwidth=0, width=130)
        self.tree.column('#6', stretch=NO, minwidth=0, width=130)
        self.tree.column('#7', stretch=NO, minwidth=0, width=130)
        self.tree.heading('Transaction ID', text="Transaction ID", anchor=W)
        self.tree.heading('Product ID', text="Product ID", anchor=W)
        self.tree.heading('Product Name', text="Product Name", anchor=W)
        self.tree.heading('Quantity', text="Quantity", anchor=W)
        self.tree.heading('Price', text="Price", anchor=W)
        self.tree.heading('Date', text="Date", anchor=W)
        self.tree.heading('Time', text="Time", anchor=W)
        self.tree.grid(row=1, column=0, sticky="W")
        scrollbary.config(command=self.tree.yview)
        scrollbarx.grid(row=2, column=0, sticky="we")
        scrollbarx.config(command=self.tree.xview)
        scrollbary.grid(row=1, column=1, sticky="ns", pady=30)
        self.tree.bind("<<TreeviewSelect>>", self.clicktranstable)
        self.user_input()

    def user_input(self):
        self.cur.execute('select max(trans_id) from sales')
        li = self.cur.fetchall()
        if li[0][0] != None:
            self.transid = li[0][0] + 1
        else:
            self.transid = 100
        self.qty = StringVar(value=1)
        self.additem = StringVar()
        self.total = IntVar(value=0)
        Button(self.entryframe, text="Proceed", command=self.transtableadd, width=8, height=7, border=0, fg="white", bg="#57a1f8",
               font="roboto 10").place(x=0, y=30)
        Button(self.entryframe, text="Add to cart", command=self.addtotrans, width=10, height=3, border=0, fg="white", bg="#57a1f8",
               font="roboto 10").place(x=100, y=80)
        Button(self.entryframe, text="Remove", command=self.removecart, width=10, height=3, border=0, fg="white", bg="#57a1f8",
               font="roboto 10").place(x=210, y=80)
        entercart = MyCombobox(self.entryframe, width=20, textvariable=self.additem, font="roboto 12")
        entercart.place(x=100, y=30, height=30)
        cartqty = Entry(self.entryframe, textvariable=self.qty, width=9, bg="#ffffff", font="roboto 12")
        cartqty.place(x=320, y=30, height=30)
        carttotal = Entry(self.entryframe, textvariable=self.total, width=20, state='readonly', bg="#ffffff",
                          font="roboto 12")
        carttotal.place(x=130, y=185, height=60)
        Label(self.entryframe, text="Quantity", font="roboto 12 bold", bg="#ffffff").place(x=318, y=0)
        Label(self.entryframe, text="Search", font="roboto 12 bold", bg="#ffffff").place(x=100, y=0)
        Label(self.entryframe, text="Amount Due", font="roboto 14 bold", bg="#ffffff").place(x=0, y=205)
        self.cur.execute("select max(invoice) from sales")
        self.invoice = self.cur.fetchall()
        self.invoice = self.invoice[0][0] + 1
        Label(self.tableframe1, text="Invoice No. " + str(self.invoice), font="roboto 14 bold", bg="#ffffff").grid(
            row=0, column=0)
        self.cur.execute("select product_desc,product_price from products")
        li = self.cur.fetchall()
        self.inventory = []
        self.desc_price = dict()
        for i in range(0, len(li)):
            if self.inventory.count(li[i][0]) == 0:
                self.inventory.append(li[i][0])
            self.desc_price[li[i][0]] = li[i][1]
        entercart.set_completion_list(self.inventory)
        li = ['Product Id', 'Product Name', 'Price', 'Left Stock']
        va = 0
        for i in range(0, 4):
            Label(self.entryframe1, text=li[i], font="roboto 14 bold", bg="#FFFFFF").place(x=0, y=va)
            va += 65
        self.cartitemid = StringVar()
        self.cartitem = StringVar()
        self.cartitemprice = StringVar()
        self.cartitemstock = StringVar()
        Entry(self.entryframe1, textvariable=self.cartitemid, font="roboto 14", bg="#FFFFFF", width=25,
              state='readonly').place(x=162, y=0, height=40)
        Entry(self.entryframe1, textvariable=self.cartitem, font="roboto 14", bg="#FFFFFF", width=25,
              state='readonly').place(x=162, y=65, height=40)
        Entry(self.entryframe1, textvariable=self.cartitemprice, font="roboto 14", bg="#FFFFFF", width=25,
              state='readonly').place(x=162, y=65 * 2, height=40)
        Entry(self.entryframe1, textvariable=self.cartitemstock, font="roboto 14", bg="#FFFFFF", width=25,
              state='readonly').place(x=162, y=65 * 3, height=40)
        self.id_qty = dict()
        self.cur.execute("select product_id from products")
        list_ = self.cur.fetchall()
        for i in range(0, len(list_)):
            self.id_qty[list_[i][0]] = 0

    def addtotrans(self):
        if len(self.additem.get()) == 0 or self.inventory.count(self.additem.get()) == 0:
            messagebox.showerror("Error", "Product Not Found!")
            return
        else:
            if not self.qty.get().isdigit():
                messagebox.showerror('Error', 'Invalid quantity!')
                return
            if int(self.qty.get()) <= 0:
                messagebox.showerror('Error', 'Invalid quantity!')
                return
            self.cur.execute("select product_id,product_desc from products where product_desc = ? ",
                             (self.additem.get(),))
            row = self.cur.fetchall()
            row = [list(row[0])]
            row[0].insert(0, self.transid)
            self.transid += 1
            row[0].append(int(self.qty.get()))
            row[0].append((int(self.qty.get()) * self.desc_price[self.additem.get()]))
            x = str(datetime.datetime.now().strftime("%d-%m-%y"))
            row[0].append(x)
            x = datetime.datetime.now()
            x = str(x.hour) + ' : ' + str(x.minute) + ' : ' + str(x.second)
            row[0].append(x)
            row = [tuple(row[0])]
            self.cartitemid.set(row[0][1])
            self.cartitemprice.set(self.desc_price[self.additem.get()])
            self.cartitem.set(row[0][2])
            self.cur.execute("select stocks from products where product_id=?", (row[0][1],))
            li = self.cur.fetchall()
            if (li[0][0] - self.id_qty[row[0][1]]) - int(self.qty.get()) < 0:
                if li[0][0] != 0:
                    messagebox.showerror('Error', 'Product with this quantity not available!')
                else:
                    messagebox.showerror('Error', 'Product out of stock!')
                return
            self.id_qty[row[0][1]] += int(self.qty.get())
            self.cartitemstock.set(li[0][0] - self.id_qty[row[0][1]])
            for data in row:
                self.tree.insert('', 'end', values=data)
            self.total.set(self.total.get() + (int(self.qty.get()) * self.desc_price[self.additem.get()]))
            self.qty.set('1')
            self.additem.set('')

    def transtableadd(self):
        x = self.tree.get_children()
        if len(x) == 0:
            messagebox.showerror('Error', 'Empty cart!')
            return
        if not messagebox.askyesno('Alert!', 'Do you want to proceed?'):
            return
        a = []
        self.cur.execute("select max(invoice) from sales")
        self.invoice = self.cur.fetchall()
        self.invoice = self.invoice[0][0] + 1
        for i in x:
            list_ = self.tree.item(i)
            a.append(list_['values'])
        for i in a:
            s = (str(i[5])).split('-')
            i[5] = s[2] + "-" + s[1] + "-" + s[0]
            self.cur.execute("insert into sales values (?,?,?,?,?,?)",
                             (int(i[0]), int(self.invoice), int(i[1]), int(i[3]), i[5], i[6]))
            self.cur.execute("select stocks from products where product_id=?", (int(i[1]),))
            list_ = self.cur.fetchall()
            self.cur.execute("update products set stocks=? where product_id=?",
                             (list_[0][0] - self.id_qty[str(i[1])], int(i[1])))
            self.base.commit()
        messagebox.showinfo('Success', 'Transaction Successful!')
        self.makeprint()
        self.tree.delete(*self.tree.get_children())
        self.cartitemstock.set('')
        self.cartitem.set('')
        self.cartitemid.set('')
        self.cartitemprice.set('')
        self.total.set(0)
        self.additem.set('')
        self.qty.set('1')
        self.cur.execute("select product_id from products")
        list_ = self.cur.fetchall()
        for i in range(0, len(list_)):
            self.id_qty[list_[i][0]] = 0
        self.make_invoice()

    def removecart(self):
        remove = self.tree.selection()
        if len(remove) == 0:
            messagebox.showerror('Error', 'No cart selected')
            return
        if messagebox.askyesno('Alert!', 'Remove cart?'):
            x = self.tree.get_children()
            remove = remove[0]
            list_ = []
            fi = []
            for i in x:
                if i != remove:
                    list_.append(tuple((self.tree.item(i))['values']))
                else:
                    fi = ((self.tree.item(i))['values'])
            self.tree.delete(*self.tree.get_children())
            for i in list_:
                self.tree.insert('', 'end', values=i)
            self.cartitemstock.set('')
            self.cartitem.set('')
            self.cartitemid.set('')
            self.cartitemprice.set('')
            self.additem.set('')
            self.qty.set('1')
            self.id_qty[str(fi[1])] -= fi[3]
            self.total.set(self.total.get() - fi[4])
            return

    def makeprint(self):
        if messagebox.askyesno("Alert!", "Print this transaction?"):
            pass

    def clicktranstable(self, event):
        cur = self.tree.selection()
        cur = self.tree.item(cur)
        li = cur['values']
        if len(li) == 7:
            self.cartitemid.set((li[1]))
            self.cartitem.set((li[2]))
            self.cur.execute("select product_price,stocks from products where product_id=?", (li[1],))
            li = self.cur.fetchall()
            self.cartitemprice.set(li[0][0])
            self.cartitemstock.set(li[0][1] - self.id_qty[self.cartitemid.get()])
