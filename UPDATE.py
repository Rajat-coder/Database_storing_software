import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import pymysql
from tkcalendar import DateEntry


class updatetrademark:
    def __init__(self,my_frame):
        mywindow=Toplevel(my_frame)
        mywindow.title("Update Trademark")
        mywindow.minsize(1550,900)

        a1 = Label(mywindow, text="APPLICATION NO.")
        a1.place(x=20, y=510)
        self.a11 = Entry(mywindow)
        self.a11.place(x=150, y=510)

        v1 = Label(mywindow, text="APPLICATION DATE")
        v1.place(x=20, y=540)
        self.cal = Entry(mywindow)
        self.cal.place(x=150, y=540)

        b1 = Label(mywindow, text="NAME OF PARTY")
        b1.place(x=20, y=570)
        self.b11 = Entry(mywindow, width=40)
        self.b11.place(x=150, y=570)

        c1 = Label(mywindow, text="TRADEMARK NAME")
        c1.place(x=20, y=600)
        self.c11 = Entry(mywindow, width=40)
        self.c11.place(x=150, y=600)

        x1 = Label(mywindow, text="USER DETAILS")
        x1.place(x=20, y=630)
        self.x11 = Entry(mywindow, width=40)
        self.x11.place(x=150, y=630)

        self.Class = StringVar()
        classbox = ttk.Combobox(mywindow, textvariable=self.Class, state='readonly')
        self.fetch_data()
        classbox.config(values=self.coursesname)
        classbox.set("Choose Class")
        classbox.place(x=150, y=660)

        self.Status = StringVar()
        statusbox = ttk.Combobox(mywindow, textvariable=self.Status, state='readonly')
        self.fetch_data2()
        statusbox.config(values=self.statusname)
        statusbox.set("Choose Status")
        statusbox.place(x=150, y=690)

        f1 = Label(mywindow, text="CONTACT NUMBER")
        f1.place(x=20, y=720)
        self.f11 = Entry(mywindow)
        self.f11.place(x=150, y=720)

        g1 = Label(mywindow, text="EMAIL")
        g1.place(x=500, y=510)
        self.g11 = Entry(mywindow, width=30)
        self.g11.place(x=630, y=510)


        h1 = Label(mywindow, text="TMJ DATE")
        h1.place(x=500, y=540)
        self.h11 = Entry(mywindow, width=30)
        self.h11.place(x=630, y=540)

        i1 = Label(mywindow, text="RENEWAL DATE")
        i1.place(x=500, y=570)
        self.cal2 = Entry(mywindow)
        self.cal2.place(x=630, y=570)

        e1 = Label(mywindow, text="ADDRESS")
        e1.place(x=500, y=620)
        self.e11 = Text(mywindow, height=3, width=40)
        self.e11.place(x=630, y=620)

        time1 = Label(mywindow, text="TIME ENTRY")
        time1.place(x=500, y=700)
        self.time11 = Entry(mywindow,width=40)
        self.time11.place(x=630, y=700)

        btn1 = Button(mywindow, text="Search By Name", padx=10,command=self.searchdata2, bg="yellow")
        btn2 = Button(mywindow, text="fetch", padx=10,command=self.fetchbutton, bg="yellow")
        btn3 = Button(mywindow, text="Search By Application", padx=10,command=self.searchdata, bg="yellow")
        btn4 = Button(mywindow, text="Update", padx=10,command=self.updatebutton, bg="yellow")
        btn5 = Button(mywindow, text="Delete", padx=10,command=self.deletebutton, bg="yellow")
        btn6 = Button(mywindow, text="Find EntryTime", padx=10,command=self.searchdata3, bg="yellow")

        btn2.place(x=400,y=760)
        btn4.place(x=520,y=760)
        btn5.place(x=640,y=760)
        btn6.place(x=760, y=760)
        btn3.place(x=20,y=760)
        btn1.place(x=220,y=760)

        self.mytablearea = Frame(mywindow)
        scrollbarx = Scrollbar(self.mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(self.mytablearea, columns=(
        'APPLICATION', 'APPLICATION DATE', 'NAME', 'TRADEMARK', 'DETAILS', 'CLASS', 'STATUS', 'CONTACT', 'EMAIL', 'TMJ',
        'RENEWAL', 'ADDRESS','TIME'),
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
        self.mytable.heading('TIME', text="TIME")

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
        self.mytable.column('#12', stretch=NO, anchor=tkinter.N, minwidth=0, width=450)
        self.mytable.column('#13', stretch=NO, anchor=tkinter.N, minwidth=0, width=200)
        self.mytable.pack()
        self.mytable.bind("<Double-Button-1>", self.getdata)
        self.mytablearea.pack()


        mywindow.mainloop()

    def getdata(self,e):
        id = self.mytable.focus()
        content = self.mytable.item(id)
        row = content['values']
        Application=row[0]
        self.setdata(Application)

    def setdata(self,Application):
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query = "select Application,ApplicationDate,Name,Trademark,userdetail,Class,Status,Contact,Email,TMJ,Renewal,Address,Time from mytable where Application=%s"
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                try:
                    myconn.execute(sql_query,Application)
                    result = myconn.fetchall()

                    for myrow in result:
                        self.a11.delete(0, END)
                        self.a11.insert(0, str(myrow[0]))

                        self.cal.delete(0, END)
                        self.cal.insert(0, str(myrow[1]))

                        self.b11.delete(0, END)
                        self.b11.insert(0, str(myrow[2]))

                        self.c11.delete(0, END)
                        self.c11.insert(0, str(myrow[3]))

                        self.x11.delete(0, END)
                        self.x11.insert(0, str(myrow[4]))

                        self.Class.set(myrow[5])

                        self.Status.set(myrow[6])



                        self.f11.delete(0, END)
                        self.f11.insert(0, str(myrow[7]))

                        self.g11.delete(0, END)
                        self.g11.insert(0, str(myrow[8]))

                        self.h11.delete(0, END)
                        self.h11.insert(0, str(myrow[9]))

                        self.cal2.delete(0, END)
                        self.cal2.insert(0, str(myrow[10]))

                        self.e11.delete('1.0', END)
                        self.e11.insert(END, str(myrow[11]))

                    myobj.commit()
                    myobj.close()
                except Exception as ex:

                    messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex))

    def fetchbutton(self):
        Application=self.a11.get()
        self.setdata(Application)

    def updatebutton(self):
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query = "update mytable set ApplicationDate=%s, Name=%s,Trademark=%s,userdetail=%s,Class=%s,Status=%s,Contact=%s,Email=%s,TMJ=%s,Renewal=%s,Address=%s where Application=%s "
                try:
                    myconn.execute(sql_query, (
                    self.cal.get(),self.b11.get(), self.c11.get(), self.x11.get(), self.Class.get(), self.Status.get(),
                    self.f11.get(), self.g11.get(), self.h11.get(), self.cal2.get(), self.e11.get('1.0', END), self.a11.get()))

                    messagebox.showinfo("success", "successfuly updated")
                    myobj.commit()
                    myobj.close()
                except Exception as ex:
                    messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex))

    def searchdata(self):
        a= self.a11.get()
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query = "select Application,ApplicationDate,Name,Trademark,userdetail,Class,Status,Contact,Email,TMJ,Renewal,Address,Time from mytable where Application like %s"

                try:
                    myconn.execute(sql_query, a+"%")
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

    def searchdata2(self):
        a= self.b11.get()
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query = "select Application,ApplicationDate,Name,Trademark,userdetail,Class,Status,Contact,Email,TMJ,Renewal,Address,Time from mytable where Name like %s"

                try:
                    myconn.execute(sql_query, a+"%")
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


    def searchdata3(self):
        a= self.time11.get()
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query = "select Application,ApplicationDate,Name,Trademark,userdetail,Class,Status,Contact,Email,TMJ,Renewal,Address,Time from mytable where Time like %s"

                try:
                    myconn.execute(sql_query, a+"%")
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
                    s = self.coursesname.append(row[0])
                    # or
                    # s = str(row[0]) + " " + str(row[1]) + "  " + str(row[2])
                    self.coursesname.append(s)
                dc.close()
        except Exception as e:
            messagebox.showerror("error", "error :  " + str(e))


    def fetch_data2(self):
        try:
            mydb = pymysql.connect(host='localhost', db='Officedb', user="root", password="")
            with mydb.cursor() as dc:
                dc.execute("select * from status")
                result=dc.fetchall()
                self.statusname = []
                if (len(result) == 0):
                    messagebox.showerror("error", "no Status  ")
                for row in result:
                    # s=self.coursesname.append(row[0])
                    #or
                    s = str(row[0])
                    self.statusname.append(s)
                dc.close()
        except Exception as e:
            messagebox.showerror("error","error :  "+str(e))

    def deletebutton(self):
        Application=self.a11.get()
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query = "delete from mytable where Application=%s"
                messagebox.showinfo("Complete", "Successfully deleted")

                try:
                    myconn.execute(sql_query, Application)
                    myobj.commit()

                    self.a11.delete(0, END)
                    self.cal.delete(0, END)
                    self.b11.delete(0, END)
                    self.c11.delete(0, END)
                    self.x11.delete(0, END)
                    self.Class.set("Choose your class")
                    self.Status.set("Choose your Status")

                    self.f11.delete(0, END)
                    self.g11.delete(0, END)
                    self.h11.delete(0, END)
                    self.cal2.delete(0, END)
                    self.e11.delete('1.0', END)


                    myobj.close()
                except Exception as ex:

                    messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex))
