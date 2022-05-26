"""
Элемент Listbox в tkinter представляет список объектов.
"""

from tkinter import *

languages = ["Python", "JavaScript", "C#", "Java"]

root = Tk()
root.title("GUI на Python")
root.geometry("300x280")

languages_listbox = Listbox()

for language in languages:
    languages_listbox.insert(END, language)

languages_listbox.pack()

root.mainloop()

# Создание прокрутки
from tkinter import *

languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
             "T-SQL", "PL-SQL", "Typescript"]

root = Tk()
root.title("GUI на Python")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

languages_listbox = Listbox(yscrollcommand=scrollbar.set, width=40)

for language in languages:
    languages_listbox.insert(END, language)

languages_listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=languages_listbox.yview)

root.mainloop()


# Управление данными
from tkinter import *


# удаление выделенного элемента
def delete():
    selection = languages_listbox.curselection()
    # мы можем получить удаляемый элемент по индексу
    # selected_language = languages_listbox.get(selection[0])
    languages_listbox.delete(selection[0])


# добавление нового элемента
def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)


root = Tk()
root.title("GUI на Python")


"""
Для создания иерархического меню в tkinter и Python применяется виджет Menu.
"""

# Простое меню с подменю
from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")

root.config(menu=main_menu)

root.mainloop()

# Взаимодействие с меню
# Для этого у каждого элемента меню можно задать параметр command
from tkinter import *
from tkinter import messagebox


def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

main_menu = Menu()

main_menu.add_cascade(label="File")
main_menu.add_cascade(label="Edit", command=edit_click)
main_menu.add_cascade(label="View")

root.config(menu=main_menu)

root.mainloop()