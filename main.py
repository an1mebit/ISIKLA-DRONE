from tkinter import *
from emulation import emulation
from constants import *
root = Tk()

entry1 = Entry()
entry1.pack(anchor=NW, padx=8, pady=8)
entry2 = Entry()
entry2.pack(anchor=NW, padx=8, pady=8)
entry3 = Entry()
entry3.pack(anchor=NW, padx=8, pady=8)
entry4 = Entry()
entry4.pack(anchor=NW, padx=8, pady=8)
entry5 = Entry()
entry5.pack(anchor=NW, padx=8, pady=8)
entry6 = Entry()
entry6.pack(anchor=NW, padx=8, pady=8)
entry7 = Entry()
entry7.pack(anchor=NW, padx=8, pady=8)

def start_emulation():
    NIJ = int(entry1.get())
    KW = int(entry2.get())
    IJK = int(entry3.get())
    JO1 = int(entry4.get())
    NIT1 = int(entry5.get())
    IPR = int(entry6.get())
    Ruav = int(entry7.get())
    emulation(NIJ, KW, IJK, JO1, NIT1, IPR, Ruav)

Button(text = 'start', command=start_emulation).pack(side = 'left')

root.mainloop()