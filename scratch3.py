import sys
from tkinter import *
#import tkinter


def mHello():
    mLabel3 = Label(mGui2, text="hi").pack()
    mGui2.lift()
    mGui.focus_force()

print("hi")

mGui = Tk()
mGui2 = Tk()
mGuiGrid = Tk()
mGuiGrid2 = Tk()

mGui.geometry('450x450+200+200')
mGui2.geometry('200x100+100+100')
mGuiGrid.geometry('200x100+700+100')

# note: no defaullt size means grid dimensions determine window size
mGuiGrid2.geometry('+1000+100')

mGui.title("Global Thermonuclear War Simulator")



mLabel = Label(text="my text", fg="red", bg="black").pack()
mLabel2 = Label(text="text again", fg="gold", bg="white")
mLabel2.place(x=225,y=100)
mButton = Button(mGui2, text="click here", command = lambda: Label(mGui2, text="greetings").pack()).pack()

# note: empty rows and columns take up zero space
mLabelGrid1 = Label(mGuiGrid, text="0-3", bg='pink').grid(row=0, column=3)
mLabelGrid2 = Label(mGuiGrid, text="7-2", bg='white').grid(row=7, column=2)
mLabelGrid3 = Label(mGuiGrid, text="1-1", bg='gold').grid(row=1, column=1)
mLabelGrid4 = Label(mGuiGrid, text="0-0").grid(row=0, column=0)
mLabelGrid5 = Label(mGuiGrid, text="3-5").grid(row=3, column=5)

mLabelGrid2_1 = Label(mGuiGrid2, text="one-three", bg='pink').grid(row=0, column=3)
mLabelGrid2_2 = Label(mGuiGrid2, text="seven-two", bg='white').grid(row=7, column=2)
mLabelGrid3_3 = Label(mGuiGrid2, text="one-one", bg='gold').grid(row=1, column=1)
mLabelGrid4_4 = Label(mGuiGrid2, text="zero-zero").grid(row=0, column=0)
mLabelGrid5_5 = Label(mGuiGrid2, text="three-five").grid(row=3, column=5)

# note : 'sticky' options are N, S, E, W
mLabelGrid5_6 = Label(mGuiGrid2, text="3-2", bg='olive').grid(row=3, column=2, sticky=W)
mLabelGrid5_7 = Label(mGuiGrid2, text="2-1", bg='light slate grey').grid(row=2, column=1, sticky=E)

mGui.mainloop()

