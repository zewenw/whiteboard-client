from tkinter import *

root = Tk()

entry = Entry(root, width=50)
entry.pack()


entry.insert(0, "entry your name ")



def my_click():
    hello = "hello:" + entry.get()
    my_lable = Label(root, text=hello, bg="red", fg="green")
    my_lable.pack()


button = Button(root, text="enter your name:", padx=10, pady=5, bg="blue", command=my_click)
button.pack()

root.mainloop()
