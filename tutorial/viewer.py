from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('image')
# root.iconbitmap('H:/Pictures/Saved Pictures/icon.ico')

my_img1 = ImageTk.PhotoImage(Image.open("../resource/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("../resource/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("../resource/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("../resource/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("../resource/5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1, width=960, height=360)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num - 1], width=960, height=360)
    button_forward = Button(root, text=">>", command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_num - 1))
    if image_num == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


def backward(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num - 1], width=960, height=360)
    button_forward = Button(root, text=">>", command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_num-1))
    if image_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


button_back = Button(root, text="<<", command=backward, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
