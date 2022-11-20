from tkinter import *

root = Tk()


def my_click():
    my_lable = Label(root, text="clicked button!", bg="red", fg="green")
    my_lable.pack()


button = Button(root, text="line", padx=10, pady=5, bg="blue", command=my_click)
button.pack()

root.mainloop()
