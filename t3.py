from Tkinter import *

master = Tk()

snmpVer = ('one', 'two', 'three')

var1 = StringVar(master)
# var1.set("one") # initial value
var2 = StringVar(master)
# var2.set("one") # initial value
var3 = StringVar(master)
# var3.set("one") # initial value

option = OptionMenu(master, var1, *snmpVer)
option.pack()
option = OptionMenu(master, var2, "MD5", "two", "three", "four")
option.pack()
option = OptionMenu(master, var3, "one", "two", "three", "four")
option.pack()



def ok():
    print "value is", var1.get()
    print "value is", var2.get()
    print "value is", var3.get()


    master.quit()

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()