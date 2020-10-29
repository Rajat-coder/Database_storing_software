import time
from tkinter import *
import sys

from ADDCLASS import addclass
from ADDTRADEMARK import addtrademark
from LISTBYCLASS import trademarklistbyclass
from TRADEMARKLIST import trademarkdetails
from UPDATE import updatetrademark


class main_pageemp:
    def __init__(self,mywindow):
        self.mywindow=Tk()
        # self.mywindow=mywindow
        self.mywindow.wm_title("EMPLOYEE PAGE")
        menubar = Menu(self.mywindow)
        self.mywindow.option_add("*tearOff", False)
        self.mywindow.config(menu=menubar)
        # w = mywindow.winfo_screenwidth()
        # h = mywindow.winfo_screenheight()
        # mywindow.geometry("%dx%d+%d+%d" % (w, h, 0, -9))
        self.mywindow.wm_minsize(1350,1200)

        # self.img = PhotoImage(file="C:\\Users\\rajat\\PycharmProjects\\Images\\hello.png")
        # self.img2 = Label(mywindow,height=35,width=80, bg="blue")
        # self.img2.place(x=0, y=98)
        # self.img2.config(image=self.img)






        File = Menu(menubar)
        Class = Menu(menubar)
        Details = Menu(menubar)

        menubar.add_cascade(menu=File, label="FILE")
        menubar.add_cascade(menu=Class, label="CLASS")
        menubar.add_cascade(menu=Details, label="DETAILS")

        File.add_command(label="Add Trademark", accelerator="Ctrl+n", command=self.addtrademarkform)
        self.mywindow.bind("<Control-n>", lambda e: addtrademark(mywindow))
        File.add_command(label="Search / Update / Delete Student", command=self.updateframe)

        Class.add_command(label="Add Class", command=self.addclassform)
        Class.add_command(label="List Class")
        Class.add_command(label="Delete Class")

        Details.add_command(label="List of trademark", command=self.trademarklistform)
        Details.add_command(label="Trademark list by class", command=self.trademarkbyclass)

        mywindow.bind("<Control-q>", self.quitwindow)


    def quitwindow(self, e):
        sys.exit()

    def addtrademarkform(self):
        addtrademark(self.mywindow)

    def addclassform(self):
        addclass(self.mywindow)

    def trademarklistform(self):
        trademarkdetails(self.mywindow)

    def trademarkbyclass(self):
        trademarklistbyclass(self.mywindow)

    def updateframe(self):
        updatetrademark(self.mywindow)

# my_frame = Tk()
# obj = main_pageemp(my_frame)
# my_frame.mainloop()