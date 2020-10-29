from tkinter import *
from tkinter import messagebox, ttk

import pymysql

from MAINFRAME import main_page


class Createadmin:
    def __init__(self):
        self.mywindow=Tk()
        self.mywindow.wm_minsize(600,400)
        self.mywindow.title("Create Admin/User")

        l1 = Label(self.mywindow, text="USERNAME")
        l2 = Label(self.mywindow, text="PASSWORD")

        self.t1 = Entry(self.mywindow, width=50)
        self.t2 = Entry(self.mywindow, show='*')

        self.typevar = StringVar()
        type = ttk.Combobox(self.mywindow, textvariable=self.typevar, width=40)
        type.config(values=("Admin", "Employee"))
        type.set("Choose Type")
        # type.set("user type")

        btn = Button(self.mywindow, text="Create", command=self.datasave)

        l1.place(x=50, y=50)
        self.t1.place(x=150, y=50)
        l2.place(x=50, y=100)
        self.t2.place(x=150, y=100)
        type.place(x=100, y=150)

        btn.place(x=150, y=200)
        self.mywindow.mainloop()

    def datasave(self):
        try:
            mydb = pymysql.connect(host='localhost', db='officedb', user="root", password="")
            with mydb.cursor() as dc:
                dc.execute("insert into signup(Username,Password,Usertype) values(%s,%s,%s)",
                           (self.t1.get(), self.t2.get(), self.typevar.get()))
                print(self.t1.get(), self.t2.get(), self.typevar.get())
                mydb.commit()
                dc.close()
                messagebox.showinfo("Success", "admin created")
                main_page(self.mywindow)

        except Exception as e:
            messagebox.showerror("error", "error :  " + str(e))