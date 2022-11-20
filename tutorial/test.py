from tkinter import *


def show():
    print(var.get())


root = Tk()
white_board_frame = LabelFrame(root, text="WhiteBoard Here", bd=1, relief=SUNKEN, padx=10, pady=10)
white_board_frame.pack(padx=10, pady=10)
var = StringVar()
checkbutton = Checkbutton(root, text="circle", variable=var, onvalue="circle", offvalue="line")
checkbutton.deselect()
checkbutton.pack()
button_check = Button(root, text="show select", command=show).pack()


def key(event):
    print("pressed", repr(event.char))


def callback(event):
    print("clicked at", event.x, event.y)


canvas = Canvas(white_board_frame, width=200, height=200, bd=1)
canvas.bind("<Return>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()

root.mainloop()
