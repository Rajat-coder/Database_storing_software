import datetime
import os
import tkinter

from tkinter import *

from fpdf import FPDF
import pymysql
from tkinter import messagebox, ttk
class entrytime:
    def __init__(self,my_frame):
        mywindow=Toplevel(my_frame)
        mywindow.wm_minsize(800,600)
        mywindow.title("Find Entry Time")

        time1 = Label(mywindow, text="TIME ENTRY")
        time1.place(x=500, y=700)
        self.time11 = Entry(mywindow, width=40)
        self.time11.place(x=630, y=700)

        btn6 = Button(mywindow, text="Find EntryTime", padx=10,command=self.searchdata4, bg="yellow")
        btn6.place(x=760, y=760)

        self.mytablearea = Frame(mywindow)
        scrollbarx = Scrollbar(self.mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(self.mytablearea, columns=(
        'SERIAL NO.', 'APPLICATION', 'APPLICATION DATE', 'NAME', 'TRADEMARK', 'DETAILS', 'CLASS', 'STATUS', 'CONTACT',
        'EMAIL', 'TMJ', 'RENEWAL', 'ADDRESS', 'TIME'),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set, height=32)

        scrollbarx.config(command=self.mytable.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.config(command=self.mytable.yview)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading('SERIAL NO.', text="SERIAL NO.")
        self.mytable.heading('APPLICATION', text="APPLICATION NO.")
        self.mytable.heading('APPLICATION DATE', text="APPLICATION DATE")
        self.mytable.heading('NAME', text="NAME")
        self.mytable.heading('TRADEMARK', text="TRADEMARK NAME")
        self.mytable.heading('DETAILS', text="USER DETAILS")
        self.mytable.heading('CLASS', text="CLASS")
        self.mytable.heading('STATUS', text="STATUS")
        self.mytable.heading('CONTACT', text="CONTACT NUMBER")

        self.mytable.heading('EMAIL', text="EMAIL")
        self.mytable.heading('TMJ', text="TMJ NO. & DATE")
        self.mytable.heading('RENEWAL', text="RENEWAL DATE")
        self.mytable.heading('ADDRESS', text="ADDRESS")
        self.mytable.heading('TIME', text="TIME")

        self.mytable['show'] = 'headings'
        self.mytable.column('#0', stretch=NO, anchor=tkinter.N, minwidth=0, width=100)
        self.mytable.column('#1', stretch=NO, anchor=tkinter.N, minwidth=0, width=100)
        self.mytable.column('#2', stretch=NO, anchor=tkinter.N, minwidth=0, width=110)
        self.mytable.column('#3', stretch=NO, anchor=tkinter.N, minwidth=0, width=140)
        self.mytable.column('#4', stretch=NO, anchor=tkinter.N, minwidth=0, width=230)
        self.mytable.column('#5', stretch=NO, anchor=tkinter.N, minwidth=0, width=120)
        self.mytable.column('#6', stretch=NO, anchor=tkinter.N, minwidth=0, width=140)
        self.mytable.column('#7', stretch=NO, anchor=tkinter.N, minwidth=0, width=60)
        self.mytable.column('#8', stretch=NO, anchor=tkinter.N, minwidth=0, width=180)
        self.mytable.column('#9', stretch=NO, anchor=tkinter.N, minwidth=0, width=130)
        self.mytable.column('#10', stretch=NO, anchor=tkinter.N, minwidth=0, width=200)
        self.mytable.column('#11', stretch=NO, anchor=tkinter.N, minwidth=0, width=150)
        self.mytable.column('#12', stretch=NO, anchor=tkinter.N, minwidth=0, width=100)
        self.mytable.column('#13', stretch=NO, anchor=tkinter.N, minwidth=0, width=450)
        self.mytable.column('#14', stretch=NO, anchor=tkinter.N, minwidth=0, width=200)
        self.mytable.pack()
        self.mytablearea.pack()

    def searchdata4(self):
            a = self.time11.get()
            try:
                myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
                with myobj.cursor() as myconn:
                    sql_query = "select serial,Application,ApplicationDate,Name,Trademark,userdetail,Class,Status,Contact,Email,TMJ,Renewal,Address,Time from mytable where Time like %s"

                    try:
                        myconn.execute(sql_query, a + "%")
                        result = myconn.fetchall()
                        self.mytable.delete(*self.mytable.get_children())

                        for myrow in result:
                            self.mytable.insert('', END, values=(myrow))

                        myobj.commit()
                        myobj.close()
                    except Exception as ex:
                        messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured due to " + str(ex))