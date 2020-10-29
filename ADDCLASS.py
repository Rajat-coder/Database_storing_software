from tkinter import *
from tkinter import messagebox

import pymysql


class addclass:
    def __init__(self,my_frame):
        mywindow=Toplevel(my_frame)
        mywindow.wm_minsize(300,200)
        mywindow.title("Add Class")



        name=Label(mywindow,text="Class No.")
        name.place(x=40,y=50)
        self.name1=Entry(mywindow)
        self.name1.place(x=100,y=50)

        button=Button(mywindow,text="SAVE",command=self.savedata)
        button.place(x=100,y=150)

    def savedata(self):
        try:
            mydb = pymysql.connect(host='localhost', db='Officedb', user="root", password="")
            with mydb.cursor() as dc:
                dc.execute("insert into classes(class) values(%s)",
                           (self.name1.get()))
                mydb.commit()
                dc.close()
            messagebox.showinfo("Success", "Class added Successfully")

            self.name1.delete('0', END)

        except Exception as e:
            messagebox.showerror("error", "error :  " + str(e))