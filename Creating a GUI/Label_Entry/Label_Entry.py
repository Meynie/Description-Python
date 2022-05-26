"""
Текстовые метки в Python представлены элементом Label. Этот элемент позволяет выводить статический текст без возможности редактирования.
"""

from tkinter import *

# Вывод простейшего текста
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

label1 = Label(text="Hello Python", fg="#eee", bg="#333")
label1.pack()

poetry = "Вот мысль, которой весь я предан,\nИтог всего, что ум скопил.\nЛишь тот, кем бой за жизнь изведан,\nЖизнь и свободу заслужил."
label2 = Label(text=poetry, justify=LEFT)
label2.place(relx=.2, rely=.3)

root.mainloop()

# Поле ввода
from tkinter import *
from tkinter import messagebox


def display_full_name():
    messagebox.showinfo("GUI Python", name.get() + " " + surname.get())


root = Tk()
root.title("GUI на Python")

name = StringVar()
surname = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

message_button = Button(text="Click Me", command=display_full_name)
message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()