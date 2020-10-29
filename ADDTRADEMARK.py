import datetime
from tkinter import *
from tkinter import ttk, messagebox

import pymysql
from tkcalendar import DateEntry


class addtrademark:
    def __init__(self,my_frame):
        mywindow=Toplevel(my_frame)
        mywindow.wm_title("TRADEMARK FORM")
        mywindow.wm_minsize(800,600)

        a1=Label(mywindow,text="APPLICATION NO.")
        a1.place(x=20,y=20)
        self.a11=Entry(mywindow)
        self.a11.place(x=150,y=20)

        v1 = Label(mywindow, text="APPLICATION DATE")
        v1.place(x=20, y=60)
        self.cal = DateEntry(mywindow, width=12, background='darkblue',
                             foreground='white', borderwidth=2, year=2010, date_pattern='dd-mm-yyyy')
        self.cal.place(x=150, y=60)



        b1=Label(mywindow,text="NAME OF PARTY")
        b1.place(x=20,y=100)
        self.b11=Entry(mywindow, width=40)
        self.b11.place(x=150,y=100)

        c1=Label(mywindow,text="TRADEMARK NAME")
        c1.place(x=20,y=140)
        self.c11=Entry(mywindow, width=40)
        self.c11.place(x=150,y=140)

        x1 = Label(mywindow, text="USER DETAILS")
        x1.place(x=20, y=180)
        self.x11 = Entry(mywindow, width=40)
        self.x11.place(x=150, y=180)

        self.Class = StringVar()
        classbox = ttk.Combobox(mywindow, textvariable=self.Class, state='readonly')
        self.fetch_data()
        classbox.config(values=self.coursesname)
        classbox.set("Choose Class")
        classbox.place(x=150, y=220)

        self.Status = StringVar()
        statusbox = ttk.Combobox(mywindow, textvariable=self.Status, state='readonly')
        self.fetch_data2()
        statusbox.config(values=self.statusname)
        statusbox.set("Choose Status")
        statusbox.place(x=150, y=260)


        f1=Label(mywindow,text="CONTACT NUMBER")
        f1.place(x=20,y=300)
        self.f11=Entry(mywindow)
        self.f11.place(x=150,y=300)

        g1 = Label(mywindow, text="EMAIL")
        g1.place(x=20, y=340)
        self.g11 = Entry(mywindow, width=30)
        self.g11.place(x=150, y=340)

        h1 = Label(mywindow, text="TMJ DATE")
        h1.place(x=20, y=380)
        self.h11 = Entry(mywindow, width=30)
        self.h11.place(x=150, y=380)

        i1 = Label(mywindow, text="RENEWAL DATE")
        i1.place(x=20, y=420)
        self.cal2 = DateEntry(mywindow, width=12, background='darkblue',
                             foreground='white', borderwidth=2, year=2020,date_pattern='dd-mm-yyyy')
        self.cal2.place(x=150, y=420)

        e1 = Label(mywindow, text="ADDRESS")
        e1.place(x=20, y=460)
        self.e11 = Text(mywindow, height=3, width=40)
        self.e11.place(x=150, y=460)




        savebtn=Button(mywindow, text="Save",command=self.saveinfo, padx=20,bg="yellow")
        savebtn.place(x=180, y=540)

        mywindow.mainloop()

    def saveinfo(self):
        # datetime_str = self.cal.get()
        # datetime_str1 = str(self.cal.get_date())
        # datetime_object1=datetime.datetime.strptime(datetime_str1, '%Y-%m-%d').strftime('%d/%m/%Y')
        # datetime_str2 = str(self.cal2.get_date())
        # datetime_object2=datetime.datetime.strptime(datetime_str2, '%Y-%m-%d').strftime('%d/%m/%Y')

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="officedb")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("insert into mytable(Application,ApplicationDate,Name,Trademark,Class,Status,Contact,Email,TMJ,Renewal,Address,userdetail) "
                                   "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                   self.a11.get(),self.cal.get_date(),self.b11.get() , self.c11.get(),self.Class.get(),
                                   self.Status.get(),self.f11.get(),self.g11.get(),self.h11.get(),self.cal2.get_date(),self.e11.get('1.0', END),self.x11.get()))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully")
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def fetch_data(self):
        try:
            mydb = pymysql.connect(host='localhost', db='Officedb', user="root", password="")
            with mydb.cursor() as dc:
                dc.execute("select * from classes")
                result=dc.fetchall()
                self.coursesname = []
                if (len(result) == 0):
                    messagebox.showerror("error", "no class  ")
                for row in result:
                    # s=self.coursesname.append(row[0])
                    #or
                    s = str(row[0])
                    self.coursesname.append(s)
                dc.close()
        except Exception as e:
            messagebox.showerror("error","error :  "+str(e))

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


def main():
    w=Tk()
    addtrademark(w)
    w.mainloop()

if __name__ == '__main__':
    main()