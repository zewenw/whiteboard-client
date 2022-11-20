from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("tkinter")

frame = LabelFrame(root, text="this is my fram...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

button1 = Button(frame, text="this is a button")
button1.grid(row=0, column=0)
button2 = Button(frame, text="....here")
button2.grid(row=1, column=1)

root.mainloop()
