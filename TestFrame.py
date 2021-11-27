from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()

file = 'Makasan.png'

image = Image.open(file)

zoom = 1.0

#multiple image size by zoom
pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])

img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y))) 
label = Label(root, image=img)
label.image = img
label.pack()

root.mainloop()