from tkinter import *
#from lab5_library_Yong import *

def close():
    exit()


window = Tk()
menubar = Menu(window)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Vertical line")#,command=verticalline(float('Enter a x')))
filemenu.add_command(label="Horizontal line")#,command=horizontalline(float('Enter a y')))
filemenu.add_command(label="Staircase")
filemenu.add_command(label="Random pixel")
filemenu.add_command(label="Clear Backlight")
filemenu.add_command(label="Close",command=close)

menubar.add_cascade(label="Test Function",menu=filemenu)

window.config(menu=menubar)
window.mainloop()

