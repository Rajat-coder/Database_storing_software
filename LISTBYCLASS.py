import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox, ttk
class trademarklistbyclass:
    def __init__(self,my_frame):
        mywindow = Toplevel(my_frame)
        mywindow.minsize(1300,600)
        mywindow.title("Trademark By List class")

        self.mytablearea = Frame(mywindow)
        scrollbarx = Scrollbar(self.mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(self.mytablearea, columns=(
        'APPLICATION', 'APPLICATION DATE', 'NAME', 'TRADEMARK', 'DETAILS', 'CLASS', 'STATUS', 'CONTACT', 'EMAIL', 'TMJ',
        'RENEWAL', 'ADDRESS'),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set, height=23)
        scrollbarx.config(command=self.mytable.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.config(command=self.mytable.yview)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading('APPLICATION', text="APPLICATION NO.")
        self.mytable.heading('APPLICATION DATE', text="APPLICATION DATE")
        self.mytable.heading('NAME', text="NAME")
        self.mytable.heading('TRADEMARK', text="TRADEMARK NAME")
        self.mytable.heading('DETAILS', text="USER DETAILS")
        self.mytable.heading('CLASS', text="CLASS")
        self.mytable.heading('STATUS', text="STATUS")
        self.mytable.heading('CONTACT', text="CONTACT NUMBER")

        self.mytable.heading('EMAIL', text="EMAIL")
        self.mytable.heading('TMJ', text="TMJ DATE")
        self.mytable.heading('RENEWAL', text="RENEWAL DATE")
        self.mytable.heading('ADDRESS', text="ADDRESS")

        self.mytable['show'] = 'headings'
        self.mytable.column('#0', stretch=NO, anchor=tkinter.N, minwidth=0, width=100)
        self.mytable.column('#1', stretch=NO, anchor=tkinter.N, minwidth=0, width=110)
        self.mytable.column('#2', stretch=NO, anchor=tkinter.N, minwidth=0, width=140)
        self.mytable.column('#3', stretch=NO, anchor=tkinter.N, minwidth=0, width=230)
        self.mytable.column('#4', stretch=NO, anchor=tkinter.N, minwidth=0, width=120)
        self.mytable.column('#5', stretch=NO, anchor=tkinter.N, minwidth=0, width=140)
        self.mytable.column('#6', stretch=NO, anchor=tkinter.N, minwidth=0, width=60)
        self.mytable.column('#7', stretch=NO, anchor=tkinter.N, minwidth=0, width=180)
        self.mytable.column('#8', stretch=NO, anchor=tkinter.N, minwidth=0, width=130)
        self.mytable.column('#9', stretch=NO, anchor=tkinter.N, minwidth=0, width=200)
        self.mytable.column('#10', stretch=NO, anchor=tkinter.N, minwidth=0, width=100)
        self.mytable.column('#11', stretch=NO, anchor=tkinter.N, minwidth=0, width=100)
        self.mytable.column('#12', stretch=NO, anchor=tkinter.N, minwidth=0, width=300)
        self.mytable.pack()
        self.mytablearea.pack()



        self.Class = StringVar()
        classbox = ttk.Combobox(mywindow, textvariable=self.Class, state='readonly')
        self.fetch_data()
        classbox.config(values=self.coursesname)
        classbox.set("Choose Class")
        classbox.bind("<<ComboboxSelected>>", self.fetch_table)

        self.Status = StringVar()
        statusbox = ttk.Combobox(mywindow, textvariable=self.Status, state='readonly')
        self.fetch_data2()
        statusbox.config(values=self.statusname)
        statusbox.set("Choose Status")
        statusbox.bind("<<ComboboxSelected>>", self.fetch_table2)

        classbox.place(x=10, y=510)
        statusbox.place(x=200,y=510)


        mywindow.mainloop()

    def fetch_table(self,e):
        try:
                myobj=pymysql.connect(host="localhost", user="root",password="", db="officedb")
                with myobj.cursor() as myconn:
                    sql_query="select Application,ApplicationDate,Name,Trademark,userdetail,Class,Status,Contact,Email,TMJ,Renewal,Address from mytable where Class=%s"

                    try:
                        myconn.execute(sql_query,self.Class.get())
                        result = myconn.fetchall()
                        self.mytable.delete(*self.mytable.get_children())

                        for myrow in result:
                            self.mytable.insert('',END,values=(myrow))

                        myobj.commit()
                        myobj.close()
                    except Exception as ex:
                        messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
        except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured due to " + str(ex))

    def fetch_data(self):
        try:
            mydb = pymysql.connect(host='localhost', db='Officedb', user="root", password="")
            with mydb.cursor() as dc:
                dc.execute("select * from classes")
                result = dc.fetchall()
                self.coursesname = []
                if (len(result) == 0):
                    messagebox.showerror("error", "no class  ")
                for row in result:
                    # s = self.coursesname.append(row[0])
                    # or
                    s = str(row[0])
                    self.coursesname.append(s)
                dc.close()
        except Exception as e:
            messagebox.showerror("error", "error :  " + str(e))

    def fetch_table2(self,e):
        try:
                myobj=pymysql.connect(host="localhost", user="root",password="", db="officedb")
                with myobj.cursor() as myconn:
                    sql_query="select Application,ApplicationDate,Name,Trademark,userdetail,Class,Status,Contact,Email,TMJ,Renewal,Address from mytable where Status=%s"

                    try:
                        myconn.execute(sql_query,self.Status.get())
                        result = myconn.fetchall()
                        self.mytable.delete(*self.mytable.get_children())

                        for myrow in result:
                            self.mytable.insert('',END,values=(myrow))

                        myobj.commit()
                        myobj.close()
                    except Exception as ex:
                        messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
        except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured due to " + str(ex))

    def fetch_data2(self):
        try:
            mydb = pymysql.connect(host='localhost', db='Officedb', user="root", password="")
            with mydb.cursor() as dc:
                dc.execute("select * from status")
                result = dc.fetchall()
                self.statusname = []
                if (len(result) == 0):
                    messagebox.showerror("error", "no Status  ")
                for row in result:
                    # s=self.coursesname.append(row[0])
                    # or
                    s = str(row[0])
                    self.statusname.append(s)
                dc.close()
        except Exception as e:
            messagebox.showerror("error", "error :  " + str(e))