import datetime
import tkinter
from tkinter import *
import os
import pymysql
from tkinter import messagebox, ttk

from fpdf import FPDF
from tkcalendar import DateEntry


class trademarklistbyDate:
    data = []
    def __init__(self,my_frame):
        mywindow=Toplevel(my_frame)
        mywindow.minsize(1300,600)
        mywindow.title("Trademark By App Date")
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

        l1 = Label(mywindow, text="STARTING DATE")
        l2 = Label(mywindow, text="ENDING DATE")

        self.t1 = DateEntry(mywindow, width=12, background='darkblue',
                            foreground='white', borderwidth=2, year=2010, date_pattern='dd-mm-yyyy')

        self.t2 = DateEntry(mywindow, width=12, background='darkblue',
                            foreground='white', borderwidth=2, year=2010, date_pattern='dd-mm-yyyy')
        btn = Button(mywindow, text="FIND", command=self.fetch_table,bg="yellow")
        l1.place(x=0, y=510)
        self.t1.place(x=100, y=510)
        l2.place(x=250, y=510)
        self.t2.place(x=350, y=510)

        btn.place(x=230, y=540)

        printbtn = Button(mywindow, text="PRINT", padx=20,command=self.simple_table,bg="yellow")
        printbtn.place(x=1000, y=540)

    def fetch_table(self):
        try:
            myobj = pymysql.connect(host="localhost", user="root", password="", db="officedb")
            with myobj.cursor() as myconn:
                sql_query = "select Application,ApplicationDate,Name,Trademark,userdetail,Class,Status,Contact,Email,TMJ,Renewal,Address from mytable where ApplicationDate between %s and %s"

                try:
                    myconn.execute(sql_query, (self.t1.get_date(), self.t2.get_date()))
                    result = myconn.fetchall()
                    self.mytable.delete(*self.mytable.get_children())
                    print("***************startin g*****************")
                    print("all result = ",result)
                    for myrow in result:
                        print("Result=",myrow)
                        d1=str(myrow[1])
                        ob1 = datetime.datetime.strptime(d1, '%Y-%m-%d').strftime('%d/%m/%Y')
                        d2 = str(myrow[10])
                        ob2 = datetime.datetime.strptime(d2, '%Y-%m-%d').strftime('%d/%m/%Y')
                        my_data=list(myrow)
                        my_data[1]=ob1
                        my_data[10]=ob2

                        self.mytable.insert('', END, values=(my_data))
                        self.data.append(list(myrow))  # so we can use it to print(or to make pdf)
                    print("***************ending *************")

                    myobj.commit()
                    myobj.close()
                except Exception as ex:
                    messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error occured due to " + str(ex))

    def simple_table(self):  # for making pdf
        spacing = 3
        pdf = FPDF()
        pdf.set_font("Arial", size=4)
        pdf.add_page()

        col_width = pdf.w / 7
        row_height = pdf.font_size
        # print(self.data)
        headings = ['Application','ApplicationDate(YY-MM-DD)', 'Name', 'Trademark', 'User Details','Class', 'Status', 'Contact', 'Email', 'TMJ',
                    'Renewal', 'Address']
        for i in headings:  # for headings
            pdf.cell(col_width, row_height * spacing, txt=i, border=2)
        pdf.ln(row_height * spacing)
        for row in self.data:  # getting data from table(i.e database)
            print(row)
            for item in row:
                pdf.cell(col_width, row_height * spacing, txt=str(item), border=1)
            pdf.ln(row_height * spacing)

        pdf.output('pdf_file1.pdf')
        os.system('explorer.exe "pdf_file1.pdf"')  # to open default pdf that already have print option
