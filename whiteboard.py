from tkinter import *
from tkinter import ttk

circle_flag = False
Line_flag = False
rectangle_flag = False



def savePosn(event):
    print("保存起始点", repr(event.char))
    global lastx, lasty
    lastx, lasty = event.x, event.y


def addLine(event):
    print("画线", repr(event.char))
    canvas.create_line(lastx, lasty, event.x, event.y)
    savePosn(event)


def circle():
    return


def line():
    return


def rectangle():
    return


def text():
    return


root = Tk()
root.title("WhiteBoard")
root.geometry("500x660")

button_frame = LabelFrame(root, text="Choose Function", bd=1, padx=10, pady=10)
button_frame.pack(padx=10, pady=10)
white_board_frame = LabelFrame(root, text="WhiteBoard Here", bd=1, relief=SUNKEN, padx=10, pady=10)
white_board_frame.pack(padx=10, pady=10)

button_circle = Button(button_frame, text="circle", padx=10, pady=10, command=circle)
button_line = Button(button_frame, text="line", padx=10, pady=10, command=line)
button_rectangle = Button(button_frame, text="rectangle", padx=10, pady=10, command=rectangle)
button_text = Button(button_frame, text="text", padx=10, pady=10, command=text)

button_circle.grid(row=0, column=0)
button_line.grid(row=0, column=1)
button_rectangle.grid(row=0, column=2)
button_text.grid(row=0, column=3)

canvas = Canvas(white_board_frame, width=700, height=700)
# canvas.grid(row=1, columnspan=4)
canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)
canvas.pack()

root.mainloop()
