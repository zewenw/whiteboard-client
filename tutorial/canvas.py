from tkinter import *

canvas_width = 500
canvas_height = 500

root = Tk()

button_line = Button(root, text="line", bd=1)
button_circle = Button(root, text="circle", bd=1)
button_rectangle = Button(root, text="rectangle", bd=1)

button_line.grid(row=0, column=0)
button_circle.grid(row=0, column=1)
button_rectangle.grid(row=0, column=2)


canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.grid(row=1, columnspan=4, sticky=N)

root.mainloop()
