import sys
from tkinter import *

print("hi")

x = []

for i in range(4):
    print(i)
    x.append(Tk().geometry('100x100+{}+{}'.format(101 * i, 101 * i)))


mGui = Tk()

mGui.geometry('450x450+200+200')

mGui.mainloop()
