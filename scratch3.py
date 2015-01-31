import sys
from tkinter import *

#import tkinter


def mHello():
    mLabel3["text"] = ment.get()
 
    # optional code to bring window to top and change focus
    mGuiButton.lift()
    mGuiButton.focus_force()

def mInfo():
    messagebox.showinfo(title="info", message="Mules have no reproductive organs.")
    return


mGuiMain = Tk()

# menubars for GuiMain
menubar = Menu(mGuiMain)

filemenu = Menu(menubar, tearoff = 0)
fileMenu2 = Menu(menubar)
subMenu2 = Menu(fileMenu2)

subMenu2.add_command(label="restart stub")
subMenu2.add_command(label="reformat drive stub")
fileMenu2.add_cascade(label="extreme options", menu = subMenu2)

filemenu.add_command(label="info", command = mInfo)
filemenu.add_command(label="search", command = lambda: messagebox.showinfo(title="search stub", message="hi"))
menubar.add_cascade(label="file", menu=filemenu)

fileMenu2.add_command(label="quit", command = quit)
menubar.add_cascade(label="main", menu=fileMenu2)

mGuiMain.config(menu=menubar)



mGuiButton = Tk()

mGuiGrid2 = Tk()

mGuiMain.geometry('450x450+200+200')
mGuiButton.geometry('200x100+100+100')

# note: no default size means grid dimensions determine window size
mGuiGrid2.geometry('+1000+100')

mGuiMain.title("Main")

mGuiGrid2.title("Grid")
mGuiButton.title("Button")

ment = StringVar(value="hi")




mLabel = Label(text="my text", fg="red", bg="black")
mLabel.pack()
mLabel2 = Label(text="text again", fg="gold", bg="white")
mLabel2.place(x=225,y=100)
mLabel3 = Label(mGuiButton, text=ment.get())
mLabel3.pack()


mButton = Button(mGuiButton, text="click here", command = lambda: Label(mGuiButton, text="greetings").pack())
mButton.pack()

mButton2 = Button(mGuiMain, text="click here", command = mHello)
mButton2.pack()


# note: empty rows and columns take up zero space
mLabelGrid2_1 = Label(mGuiGrid2, text="one-three", bg='pink', font=("courier", 16)).grid(row=0, column=3)
mLabelGrid2_2 = Label(mGuiGrid2, text="seven-two", bg='white').grid(row=7, column=2)
mLabelGrid3_3 = Label(mGuiGrid2, text="one-one", bg='gold').grid(row=1, column=1)
mLabelGrid4_4 = Label(mGuiGrid2, text="zero-zero").grid(row=0, column=0)
mLabelGrid5_5 = Label(mGuiGrid2, text="three-five").grid(row=3, column=5)

# note : 'sticky' options are N, S, E, W
mLabelGrid5_6 = Label(mGuiGrid2, text="3-2", bg='olive').grid(row=3, column=2, sticky=W)
mLabelGrid5_7 = Label(mGuiGrid2, text="2-1", bg='light slate grey').grid(row=2, column=1, sticky=E)

# textbox entry
entry = Entry(mGuiMain, textvariable=ment)
entry.pack()

Button(mGuiMain, text="quit", command = quit).place(x=400, y=20)

mGuiMain.mainloop()

       

