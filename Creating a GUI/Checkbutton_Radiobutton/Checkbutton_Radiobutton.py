"""
Элемент Checkbutton представляет собой флажок,
который может находиться в двух состояниях: отмеченном и неотмеченном.
"""
from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

python_lang = IntVar()
python_checkbutton = Checkbutton(text="Python", variable=python_lang,
                                 onvalue=1, offvalue=0, padx=15, pady=10)
python_checkbutton.grid(row=0, column=0, sticky=W)

javascript_lang = IntVar()
javascript_checkbutton = Checkbutton(text="JavaScript", variable=javascript_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10)
javascript_checkbutton.grid(row=1, column=0, sticky=W)

root.mainloop()

"""
 Radiobutton представляет переключатель, 
 который может находиться в двух состояниях: отмеченном или неотмеченном. 
 Но в отличие от Checkbutton переключатели могут создавать группу, 
 из которой одномоментно можно выбрать только один переключатель.
"""

from tkinter import *

languages = [("Python", 1), ("JavaScript", 2), ("C#", 3), ("Java", 4)]


def select():
    l = language.get()
    if l == 1:
        sel.config(text="Выбран Python")
    elif l == 2:
        sel.config(text="Выбран JavaScript")
    elif l == 3:
        sel.config(text="Выбран C#")
    elif l == 4:
        sel.config(text="Выбран Java")


root = Tk()
root.title("GUI на Python")
root.geometry("300x280")

header = Label(text="Выберите курс", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

language = IntVar()

row = 1
for txt, val in languages:
    Radiobutton(text=txt, value=val, variable=language, padx=15, pady=10, command=select) \
        .grid(row=row, sticky=W)
    row += 1

sel = Label(padx=15, pady=10)
sel.grid(row=row, sticky=W)

root.mainloop()