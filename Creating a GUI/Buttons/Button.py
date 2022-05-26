from tkinter import *

clicks = 0


# 1
def click_button():
    """
    A simple button that counts the number of clicks.
    """
    global clicks
    clicks += 1
    buttonText.set("Clicks {}".format(clicks))


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

buttonText = StringVar()
buttonText.set("Clicks {}".format(clicks))

btn = Button(textvariable=buttonText, background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()

root.mainloop()


# 2
root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn1 = Button(text="BOTTOM", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn1.pack(side=BOTTOM)

btn2 = Button(text="RIGHT", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn2.pack(side=RIGHT)

btn3 = Button(text="LEFT", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn3.pack(side=LEFT)

btn4 = Button(text="TOP", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn4.pack(side=TOP)

root.mainloop()

# 3
clicks = 0


def click_button():
    global clicks
    clicks += 1
    btn.config(text="Clicks {}".format(clicks))


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn = Button(text="Clicks 0", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)

root.mainloop()

# 4

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

for r in range(3):
    for c in range(3):
        btn = Button(text="{}-{}".format(r, c))
        btn.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10)

root.mainloop()