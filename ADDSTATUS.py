from tkinter import *
from tkinter import messagebox

import pymysql


class addstatus:
    def __init__(self,my_frame):
        mywindow=Toplevel(my_frame)
        mywindow.wm_minsize(300,200)
        mywindow.title("Add Status")

        name=Label(mywindow,text="Enter Your Status")
        name.place(x=10,y=50)
        self.name2=Entry(mywindow)
        self.name2.place(x=120,y=50)

        button=Button(mywindow,text="SAVE",command=self.savedata)
        button.place(x=100,y=150)

    def savedata(self):
        try:
            mydb = pymysql.connect(host='localhost', db='Officedb', user="root", password="")
            with mydb.cursor() as dc:
                dc.execute("insert into status(status) values(%s)",
                           (self.name2.get()))
                mydb.commit()
                dc.close()
            messagebox.showinfo("Success", "Status added Successfully")

            self.name2.delete('0', END)

        except Exception as e:
            messagebox.showerror("error", "error :  " + str(e))