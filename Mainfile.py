from tkinter import messagebox

import pymysql

from CREATEADMIN import Createadmin
from LOGINPAGE import Loginclass


try:
    mydb = pymysql.connect(host='localhost', db='officedb', user="root", password="")
    with mydb.cursor() as dc:
        dc.execute("select * from  signup")
        result = dc.fetchone()
        if result is not None:
            Loginclass()

        else:

            Createadmin()

        dc.close()



except Exception as e:
    messagebox.showerror("error", "error :  " + str(e))