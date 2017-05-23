import Tkinter as tk
from Tkinter import *

root = tk.Tk()
choices = ('network one', 'network two', 'network three')
var = tk.StringVar(root)




def ok():
    username = "%s" % (e1.get())
    password = "%s" % (e2.get())
    print "manage snmp users create "+username+" -cf 0.0 -ap MD5 -akc " \
          "9579279544ecd9324d5a0ad17e55ec4d -pp DES -pkc " \
          "9579279544ecd9324d5a0ad17e55ec4d"

e1 = Entry(root)
e1.grid()
e2 = Entry(root)
e2.grid()
# I made this quick refresh button to demonstrate
tk.Button(root, text='ok', command=ok).grid()

root.mainloop()