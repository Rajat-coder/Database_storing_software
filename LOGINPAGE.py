from tkinter import *
from tkinter import messagebox, ttk

import pymysql

from MAINFRAME import main_page
from Mainframeemp import main_pageemp


class Loginclass:
    def __init__(self):
        self.mywindow=Tk()
        self.mywindow.wm_minsize(600,400)
        self.mywindow.title("Login Page")

        l1 = Label(self.mywindow, text="USERNAME")
        l2 = Label(self.mywindow, text="PASSWORD")

        self.t1 = Entry(self.mywindow, width=50)
        self.t2 = Entry(self.mywindow, show='*')

        btn = Button(self.mywindow, text="LOGIN", command=self.datasave)

        l1.place(x=50, y=50)
        self.t1.place(x=150, y=50)
        l2.place(x=50, y=100)
        self.t2.place(x=150, y=100)

        btn.place(x=200, y=150)
        self.mywindow.mainloop()

    def datasave(self):
        try:
            mydb = pymysql.connect(host='localhost', db='officedb', user="root", password="")
            with mydb.cursor() as dc:
                dc.execute("select Usertype from signup where Username = %s and Password =%s",
                           (self.t1.get(), self.t2.get()))
                result = dc.fetchone()
                if result is not None:
                    print(result[0])
                    if (result[0] == 'Admin'):

                        main_page(self.mywindow)

                    elif (result[0] == 'Employee'):
                        # self.mywindow.destroy
                        main_pageemp(self.mywindow)

                    # messagebox.showinfo("Success", "login")
                    # traceback.print_exe()


                else:

                    messagebox.showerror("failure", "wrong username or password")

                dc.close()


        except Exception as e:
            messagebox.showerror("error", "error :  " + str(e))
