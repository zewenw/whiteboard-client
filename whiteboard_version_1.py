from tkinter import *

circle_flag = False
line_flag = True
rectangle_flag = False


def click_position(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y


def release_position(event):
    if circle_flag:
        canvas.create_oval(lastx, lasty, event.x, event.y)
        click_position(event)
        print(
            "圆形起始点X坐标：" + str(lastx) + "     圆形起始点Y坐标： " + str(lasty) + "圆形结束点X坐标：  " + str(
                event.x) + "圆形结束点Y坐标： " + str(event.y))
    if rectangle_flag:
        canvas.create_rectangle(lastx, lasty, event.x, event.y)
        click_position(event)
        print(
            "正方形起始点X坐标：" + str(lastx) + "     正方形起始点Y坐标： " + str(
                lasty) + "   正方形结束点X坐标：  " + str(event.x) + "    正方形结束点Y坐标： " + str(event.x))


def draw(event):
    if line_flag:
        canvas.create_line(lastx, lasty, event.x, event.y)
        print("直线路过点X坐标：" + str(lastx) + "    直线路过点Y坐标： " + str(lasty))
        click_position(event)


def circle():
    button_line.deselect()
    button_rectangle.deselect()
    print(circle_var.get())
    global circle_flag
    global line_flag
    global rectangle_flag
    circle_flag = True
    line_flag = False
    rectangle_flag = False


def line():
    button_circle.deselect()
    button_rectangle.deselect()
    global circle_flag
    global line_flag
    global rectangle_flag
    circle_flag = False
    line_flag = True
    rectangle_flag = False


def rectangle():
    button_line.deselect()
    button_circle.deselect()
    print(rectangle_var.get())
    global circle_flag
    global line_flag
    global rectangle_flag
    circle_flag = False
    line_flag = False
    rectangle_flag = True


def clear_canvas():
    canvas.delete('all')


root = Tk()
root.title("WhiteBoard（Owen, Zahraa, Zhichao）")
root.geometry("500x660")

button_frame = LabelFrame(root, text="Choose Function", bd=1, padx=10, pady=10)
button_frame.pack(padx=10, pady=10)
white_board_frame = LabelFrame(root, text="WhiteBoard Here", bd=1, relief=SUNKEN, padx=10, pady=10)
white_board_frame.pack(padx=10, pady=10)

circle_var = StringVar()
button_circle = Checkbutton(button_frame, text="circle", onvalue="circle", offvalue="line", variable=circle_var,
                            padx=10, pady=10, command=circle)
button_circle.deselect()

button_line = Checkbutton(button_frame, text="line", padx=10, pady=10, command=line)
button_line.select()

rectangle_var = StringVar()
button_rectangle = Checkbutton(button_frame, text="rectangle", onvalue="rectangle", offvalue="line",
                               variable=rectangle_var, padx=10, pady=10, command=rectangle)
button_text = Button(button_frame, text="clear canvas", padx=10, pady=10, command=clear_canvas)
button_rectangle.deselect()

button_circle.grid(row=0, column=0)
button_line.grid(row=0, column=1)
button_rectangle.grid(row=0, column=2)
button_text.grid(row=0, column=3)

canvas = Canvas(white_board_frame, width=700, height=700)
canvas.bind("<Button-1>", click_position)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", release_position)
canvas.pack()

root.mainloop()
