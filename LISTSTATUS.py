from tkinter import *
import pymysql
from tkinter import messagebox, ttk
class Statusdetails:
    def __init__(self,my_frame):
        mywindow=Toplevel(my_frame)
        mywindow.wm_minsize(400,400)
        mywindow.title("Status Details")
        self.mytablearea = Frame(mywindow)
        scrollbarx = Scrollbar(self.mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(self.mytablearea, columns=("Status"),
                               xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        scrollbarx.config(command=self.mytable.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.config(command=self.mytable.yview)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading('Status', text="Status")



        self.mytable['show'] = 'headings'
        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)

        self.mytable.pack()
        self.mytablearea.pack()
        try:
                myobj=pymysql.connect(host="localhost", user="root",password="", db="officedb")
                with myobj.cursor() as myconn:
                    sql_query="select status from status "
                    try:
                        myconn.execute(sql_query)
                        result = myconn.fetchall()
                        for myrow in result:
                            self.mytable.insert('',END,values=(myrow))
                        myobj.commit()
                        myobj.close()
                    except Exception as ex:
                        messagebox.showerror("Error Occured in query", "Error occured due to " + str(ex))
        except Exception as ex:
                messagebox.showerror("Error Occured", "Error occured due to " + str(ex))