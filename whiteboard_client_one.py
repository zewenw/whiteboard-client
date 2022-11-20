from tkinter import *
from websocket import create_connection
import threading
import asyncio

circle_flag = False
line_flag = True
rectangle_flag = False


class WebSocketThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.socket = None

    def run(self):
        # asyncio.set_event_loop(asyncio.new_event_loop())
        websocket = create_connection("ws://localhost:8765")
        self.socket = websocket
        # asyncio.get_event_loop().run_until_complete(websocket)
        # asyncio.get_event_loop().run_forever()

    def listen(self):
        while True:
            try:
                msg = self.socket.recv()
                if msg is None:
                    break
                else:
                    sync_canvas(msg)

            except self.socket.exceptions.ConnectionClosed:
                print("close: ", self.socket)
                break

    def send_msg(self, msg):
        self.socket.send(msg)

    def do_activate(self):
        asyncio.get_event_loop().run_until_complete(self.action())


threadWebSocket = WebSocketThread()
threadWebSocket.start()


def sync_canvas(msg):
    split = str(msg).split("|")
    shape = split[0]
    if shape == "circle":
        canvas.create_oval(int(split[1]), int(split[2]), int(split[3]), int(split[4]))
    elif shape == "rectangle":
        canvas.create_rectangle(int(split[1]), int(split[2]), int(split[3]), int(split[4]))
    elif shape == "line":
        canvas.create_line(int(split[1]), int(split[2]), int(split[3]), int(split[4]))


def click_position(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y


def release_position(event):
    if circle_flag:
        canvas.create_oval(lastx, lasty, event.x, event.y)
        click_position(event)
        msg = "circle|" + str(lastx) + "|" + str(lasty) + "|" + str(event.x) + "|" + str(event.y)
        threadWebSocket.send_msg(msg)
        print("circle_begin_X_coor: " + str(lastx) + " circle_begin_Y_coor: " + str(
            lasty) + " circle_end_X_coor: " + str(
            event.x) + " circle_end_Y_coor: " + str(event.y))
    if rectangle_flag:
        canvas.create_rectangle(lastx, lasty, event.x, event.y)
        click_position(event)
        msg = "rectangle|" + str(lastx) + "|" + str(lasty) + "|" + str(event.x) + "|" + str(event.y)
        threadWebSocket.send_msg(msg)
        print("rec_begin_X_coor: " + str(lastx) + " rec_begin_Y_coor: " + str(
            lasty) + " rec_end_X_coor: " + str(event.x) + " rec_end_Y_coor: " + str(event.x))


def draw(event):
    if line_flag:
        canvas.create_line(lastx, lasty, event.x, event.y)
        click_position(event)
        msg = "line|" + str(lastx) + "|" + str(lasty) + "|" + str(event.x) + "|" + str(event.y)
        threadWebSocket.send_msg(msg)
        print("line_X_coor: " + str(lastx) + " line_Y_coor: " + str(lasty))


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
button_clear = Button(button_frame, text="clear canvas", padx=10, pady=10, command=clear_canvas)
button_rectangle.deselect()


button_circle.grid(row=0, column=0)
button_line.grid(row=0, column=1)
button_rectangle.grid(row=0, column=2)
button_clear.grid(row=0, column=3)

canvas = Canvas(white_board_frame, width=700, height=700)
canvas.bind("<Button-1>", click_position)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", release_position)
canvas.pack()

root.mainloop()
