import sys
from tkinter import *


# function definitions START

# functions supplied as callbacks for traces are passed arguments and must take them
def set_checkmate_text(*args):
    if checkmate.get():
        checkmate_text.set("Checkmate ON")
    else:
        checkmate_text.set("Checkmate OFF")

    
# label update for "Button" window
def mHello():
    mLabel3["text"] = ment.get()
 
    # optional code to bring window to top and change focus
    mGuiButton.lift()
    mGuiButton.focus_force()

# called by "Main" menu option "file" -> "info"
def mInfo():
    messagebox.showinfo(title="info", message="Mules have no reproductive organs.")
    return

def checkmate_flip():
    if checkmate.get():
        checkmate.set(False)
    else:
        checkmate.set(True)

def update_from_radio():

    orderString.set("you ordered {} with {}.".format(radioValMeat.get(), radioValSauce.get()))
    messagebox.showinfo(message="hi")
    

def noop():
    pass
        

# function definitions END


# make this first, or add: root = Tk()

mGuiMain = Tk()


#values for "checkmate" flag demo

checkmate_text = StringVar()
checkmate_text.initialize("")
checkmate = BooleanVar(mGuiMain)
checkmate.initialize(True)
checkmate.trace("w", set_checkmate_text)
set_checkmate_text()



# menubars for "Main" window
menubar = Menu(mGuiMain)

filemenu = Menu(menubar, tearoff = 0)

fileMenu2 = Menu(menubar)
fileMenu2.add_command(label="quit", command = mGuiMain.destroy)

fileMenu2.add_checkbutton(label="Checkmate!", onvalue = True, offvalue = False, variable = checkmate)


subMenu2 = Menu(fileMenu2)

subMenu2.add_command(label="restart stub")
subMenu2.add_command(label="reformat drive stub")
fileMenu2.add_cascade(label="extreme options", menu = subMenu2)

filemenu.add_command(label="info", command = mInfo)
filemenu.add_command(label="search", command = lambda: messagebox.showinfo(title="search stub", message="hi"))
menubar.add_cascade(label="file", menu=filemenu)


menubar.add_cascade(label="main", menu=fileMenu2)

mGuiMain.config(menu=menubar)


# "Main" window config
mGuiMain.geometry('450x450+200+200')
mGuiMain.title("Main")

mLabel = Label(text="my text", fg="red", bg="black")
mLabel.pack()
mLabel2 = Label(text="text again", fg="gold", bg="white")
mLabel2.place(x=225,y=100)
mButton2 = Button(mGuiMain, text="click here", command = mHello)
mButton2.pack()

# "Checkmate" checkbox and button system
mLabelCheckmate = Label(textvariable = checkmate_text)
mLabelCheckmate.place(x=200, y=400)
mButtonCheckmate = Button(mGuiMain, text = "flip Checkmate status", command = checkmate_flip)
mButtonCheckmate.place(x=200, y=415)


# "Main" window textbox entry
ment = StringVar(value="hi")
entry = Entry(mGuiMain, textvariable=ment)
entry.pack()
Button(mGuiMain, text="quit", command = quit).place(x=400, y=20)


# "Button" window

mGuiButton = Tk()
mGuiButton.geometry('200x100+100+100')
mGuiButton.title("Button")
mLabel3 = Label(mGuiButton, text=ment.get())
mLabel3.pack()
mButton = Button(mGuiButton, text="click here", command = lambda: Label(mGuiButton, text="greetings").pack())
mButton.pack()


# "Grid" window
mGuiGrid2 = Tk()
# note: no default size means grid dimensions determine window size
mGuiGrid2.geometry('+1000+100')
mGuiGrid2.title("Grid")

# note: empty rows and columns take up zero space
mLabelGrid2_1 = Label(mGuiGrid2, text="one-three", bg='pink', font=("courier", 16)).grid(row=0, column=3)
mLabelGrid2_2 = Label(mGuiGrid2, text="seven-two", bg='white').grid(row=7, column=2)
mLabelGrid3_3 = Label(mGuiGrid2, text="one-one", bg='gold').grid(row=1, column=1)
mLabelGrid4_4 = Label(mGuiGrid2, text="zero-zero").grid(row=0, column=0)
mLabelGrid5_5 = Label(mGuiGrid2, text="three-five").grid(row=3, column=5)

# note : 'sticky' options are N, S, E, W
mLabelGrid5_6 = Label(mGuiGrid2, text="3-2", bg='olive').grid(row=3, column=2, sticky=W)
mLabelGrid5_7 = Label(mGuiGrid2, text="2-1", bg='light slate grey').grid(row=2, column=1, sticky=E)



# "Radio" window (radio buttons)

radioVal = IntVar()
radioValMeat = StringVar()
radioValSauce = StringVar()
radioVal.initialize(1)
mGuiRadio = Tk()
mGuiRadio.title("Radio Buttons")
mGuiRadio.geometry('100x200+700+100')

radioLabelMeat = Label(mGuiRadio, text="meat choices")
radioLabelMeat.pack()

rbMeat1 = Radiobutton(mGuiRadio, text="chicken", variable=radioValMeat, command = update_from_radio, value="chicken")
rbMeat1.pack()
rbMeat2 = Radiobutton(mGuiRadio, text="beef", variable=radioValMeat,command = update_from_radio, value="beef")
rbMeat2.pack()
rbMeat3 = Radiobutton(mGuiRadio, text="pork", variable=radioValMeat, command = update_from_radio, value="pork")
rbMeat3.pack()

radioLabelSauce = Label(mGuiRadio, text="sauce choices")
radioLabelSauce.pack()

rbSauce1 = Radiobutton(mGuiRadio, text="red sauce", variable=radioValSauce, command = update_from_radio, value="red sauce")
rbSauce1.pack()
rbSauce2 = Radiobutton(mGuiRadio, text="two", variable=radioValSauce, command = update_from_radio, value="green sauce")
rbSauce2.pack()
rbSauce3 = Radiobutton(mGuiRadio, text="three", variable=radioValSauce, command = update_from_radio, value="enchilada sauce")
rbSauce3.pack()

orderString = StringVar()
orderString.set("your order...")
update_from_radio()
radioLabelOrder = Label(mGuiRadio, textvariable=orderString.get())
radioLabelOrder.pack()
update_from_radio()



mGuiMain.mainloop()

       

