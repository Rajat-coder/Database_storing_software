from tkinter import *
from tkinter import messagebox, ttk

import pymysql
class updatetusername:
    def __init__(self,my_frame):
        mywindow=Toplevel(my_frame)
        mywindow.title("Change username")
        mywindow.minsize(900,600)

        a1 = Label(mywindow, text="USERNAME")
        a1.place(x=20, y=20)
        self.a11 = Entry(mywindow)
        self.a11.place(x=150, y=20)

        b1 = Label(mywindow, text="PASSWORD")
        b1.place(x=20, y=60)
        self.b11 = Entry(mywindow, width=30)
        self.b11.place(x=150, y=60)

        c1 = Label(mywindow, text="USERTYPE")
        c1.place(x=20, y=100)
        self.c11 = Entry(mywindow, width=30)
        self.c11.place(x=150, y=100)

        btn1 = Button(mywindow, text="Search By Name", padx=10, command=self.searchdata)
        btn4 = Button(mywindow, text="Update by Name", padx=10, command=self.updatebutton)
        btn2 = Button(mywindow, text="Update by Password", padx=10, command=self.updatebutton2)
        # btn5 = Button(mywindow, text="Delete", padx=10, command=self.deletebutton)

        btn4.place(x=360, y=17)
        btn2.place(x=360, y=58)
        # btn5.place(x=360, y=150)
        btn1.place(x=150, y=150)

        self.mytablearea = Frame(mywindow)
        scrollbarx = Scrollbar(self.mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(self.mytablearea, columns=(
            'Username','Password','Usertype'),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        scrollbarx.config(command=self.mytable.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.config(command=self.mytable.yview)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading('Username', text="USERNAME")
        self.mytable.heading('Password', text="PASSWORD")
        self.mytable.heading('Usertype', text="USERTYPE")


        self.mytable['show'] = 'headings'
        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=100)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=150)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=120)
        self.mytable.pack()
        self.mytable.bind("<Double-Button-1>", self.getdata)
        self.mytablearea.place(x=20, y=250)

        mywindow.mainloop()

    def getdata(self, e):
        id = self.mytable.focus()
        content = self.mytable.item(id)
        row = content['values']
        Username = row[0]
        self.setdata(Username)

    def setdata(self, Username):
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query = "select Username,Password,Usertype from signup where Username=%s"
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                try:
                    myconn.execute(sql_query, Username)
                    result = myconn.fetchall()

                    for myrow in result:
                        self.a11.delete(0, END)
                        self.a11.insert(0, str(myrow[0]))

                        self.b11.delete(0, END)
                        self.b11.insert(0, str(myrow[1]))

                        self.c11.delete(0, END)
                        self.c11.insert(0, str(myrow[2]))

                    myobj.commit()
                    myobj.close()
                except Exception as ex:

                    messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex))

    def updatebutton(self):
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query="update signup set Username=%s,Usertype=%s where Password=%s"
                try:
                    myconn.execute(sql_query,(self.a11.get(),self.c11.get(),self.b11.get()))

                    messagebox.showinfo("success", "successfuly updated")
                    myobj.commit()
                    myobj.close()
                except Exception as ex:
                    messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex))


    def updatebutton2(self):
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query="update signup set Password=%s ,Usertype=%swhere Username=%s"
                try:
                    myconn.execute(sql_query,(self.b11.get(),self.c11.get(),self.a11.get()))

                    messagebox.showinfo("success", "successfuly updated")
                    myobj.commit()
                    myobj.close()
                except Exception as ex:
                    messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex))


    def searchdata(self):
        a = self.a11.get()
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query = "select Username,Password,Usertype from signup where Username like %s"

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