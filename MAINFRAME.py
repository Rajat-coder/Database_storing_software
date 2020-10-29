import time
from tkinter import *
import sys

from ADDCLASS import addclass
from ADDSTATUS import addstatus
from ADDTRADEMARK import addtrademark
from CHANGEUSER import updatetusername
from ENTRYTIME import entrytime
from LISTBYCLASS import trademarklistbyclass
from LISTBYTMJ import trademarklistbyDate
from LISTCLASS import Classdetails
from LISTSTATUS import Statusdetails
from TRADEMARKLIST import trademarkdetails
from UPDATE import updatetrademark


class main_page:
    def __init__(self,mywindow):
        self.mywindow=mywindow
        self.mywindow.wm_title("Advocate Management")
        menubar = Menu(self.mywindow)
        self.mywindow.option_add("*tearOff", False)
        self.mywindow.config(menu=menubar)
        # w = mywindow.winfo_screenwidth()
        # h = mywindow.winfo_screenheight()
        # mywindow.geometry("%dx%d+%d+%d" % (w, h, 0, -9))
        self.mywindow.wm_minsize(1350,800)

        self.img = PhotoImage(file="C:\\Users\\HP\\PycharmProjects\\OFFICE\\Images\\hello.png")
        self.img2 = Label(self.mywindow,height=420,width=1350)
        self.img2.place(x=0, y=98)
        self.img2.config(image=self.img)



        ABC1 = Frame(self.mywindow, bd=6, width=1350, height=100, padx=5, bg="grey", relief=RAISED)
        ABC1.grid(row=0, column=0, columnspan=4, sticky=W)



        Date1 = StringVar()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%y"))

        Time1.set(time.strftime("%H:%M:%S"))

        self.Ib1Title = Label(ABC1, textvariable=Date1, font=("Lucida Handwriting", 20, "bold"), pady=9, bd=5, bg="grey",
                              fg="cornsilk").place(x=10,y=15)
        self.Ib1Title = Label(ABC1, text="\tS HANDA & CO.\t\t", font=("Lucida Handwriting", 33, "bold"), pady=9, bd=5,
                              bg="grey", fg="cornsilk", justify=CENTER).place(x=300,y=5)
        self.Ib1Title = Label(ABC1, textvariable=Time1, font=("Lucida Handwriting", 20, "bold"), pady=9, bd=5, bg="grey",
                              fg="cornsilk").place(x=1180,y=15)



        lb1 =Label(mywindow,font=("Lucida Handwriting", 12, "bold"), text= '''   About us :
                                CONSULTANT FOR REGISATION 
                                OF TRADEMARK,COPYRIGHTS,
                                PATENT,DESIGN,FIRM REGISTRATION,
                                PARTNERSHIP,SOCITIES,CLUB,
                                ASSOCIATION,ISO''' )
        lb1.place(x=0, y=550)

        lb2 = Label(mywindow,font=("Lucida Handwriting", 12, "bold"), text='''   Contact Details :
                                        127(FIRST FLOOR),SHIV NAGAR,
                                        SODAL MANDIR,JALANDHAR
                                        144004(PUNJAB)
                                        AJAY KUMAR HANDA-9417193348
                                        RISHABH HANDA-8968842231'''  )
        lb2.place(x=800, y=550)



        File = Menu(menubar)
        Class = Menu(menubar)
        Status = Menu(menubar)
        Details = Menu(menubar)
        Logout = Menu(menubar)
        Quit = Menu(menubar)

        menubar.add_cascade(menu=File, label="FILE")
        menubar.add_cascade(menu=Class, label="CLASS")
        menubar.add_cascade(menu=Status, label="STATUS")
        menubar.add_cascade(menu=Details, label="DETAILS")
        menubar.add_cascade(menu=Logout, label="LOGOUT")
        menubar.add_cascade(menu=Quit, label="QUIT")

        File.add_command(label="Add Trademark", accelerator="Ctrl+n", command=self.addtrademarkform)
        self.mywindow.bind("<Control-n>", lambda e: addtrademark(mywindow))
        File.add_command(label="Search / Update / Delete Trademark", accelerator="Ctrl+f", command=self.updateframe)
        self.mywindow.bind("<Control-f>", lambda e: updatetrademark(mywindow))
        File.add_command(label="Find EntryTime", accelerator="Ctrl+f", command=self.timeframe)

        Class.add_command(label="Add Class", command=self.addclassform)
        Class.add_command(label="List Class",command=self.listclassframe)

        Status.add_command(label="Add Status",command=self.addstatusform)
        Status.add_command(label="List Status", command=self.liststatusframe)

        Details.add_command(label="Trademark List", command=self.trademarklistform)
        Details.add_command(label="Trademark List By CLASS AND NAME ", command=self.trademarkbyclass)
        Details.add_command(label="Trademark List By APP. DATE ", command=self.trademarkbydate)

        Logout.add_command(label="Change Username and password",command=self.chngeuserform)
        Logout.add_command(label="Logout",command=self.loginframe)
        Logout.add_command(label="New User",command=self.newuser)

        Quit.add_command(label="Quit", accelerator="Ctrl+q")
        mywindow.bind("<Control-q>", self.quitwindow)


    def quitwindow(self, e):
        sys.exit()

    def addtrademarkform(self):
        addtrademark(self.mywindow)

    def addclassform(self):
        addclass(self.mywindow)

    def loginframe(self):
        self.mywindow.destroy()
        from LOGINPAGE import Loginclass
        Loginclass()

    def newuser(self):
        self.mywindow.destroy()
        from CREATEADMIN import Createadmin
        Createadmin()


    def trademarklistform(self):
        trademarkdetails(self.mywindow)

    def timeframe(self):
        entrytime(self.mywindow)


    def chngeuserform(self):
        updatetusername(self.mywindow)

    def trademarkbyclass(self):
        trademarklistbyclass(self.mywindow)

    def updateframe(self):
        updatetrademark(self.mywindow)



    def liststatusframe(self):
        Statusdetails(self.mywindow)

    def trademarkbydate(self):
        trademarklistbyDate(self.mywindow)

    def addstatusform(self):
        addstatus(self.mywindow)

    def listclassframe(self):
        Classdetails(self.mywindow)
# my_frame = Tk()
# obj = main_page(my_frame)
# my_frame.mainloop()
