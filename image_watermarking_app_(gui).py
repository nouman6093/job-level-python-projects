import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk

def select_image():
    global image_label, photo1, image
    path = filedialog.askopenfilename()
    image = Image.open(path)
    image = image.resize((200, 200))
    photo1 = ImageTk.PhotoImage(image)
    image_label.config(image=photo1)

def select_watermark_image():
    global watermark_label, photo2, watermark
    path = filedialog.askopenfilename()
    watermark = Image.open(path)
    watermark = watermark.resize((200, 200))
    photo2 = ImageTk.PhotoImage(watermark)
    watermark_label.config(image=photo2)

def watermark():
    global photo1, photo2, image_label, watermark_label, image, watermark
    position = (image.width - watermark.width, image.height - watermark.height)
    image.paste(watermark, position)
    watermarked_photo = ImageTk.PhotoImage(image)
    watermarked_label.config(image=watermarked_photo)
    watermarked_label.image = watermarked_photo  # Keep a reference to the image

def save_image():
    global image
    path = filedialog.asksaveasfilename(defaultextension=".png")
    image.save(path)

def reset_everything():
    global image_label, watermark_label, watermarked_label, photo1, photo2, image, watermark
    image_label.config(image=None)
    watermark_label.config(image=None)
    watermarked_label.config(image=None)
    photo1 = None
    photo2 = None
    image = None
    watermark = None

window = tkinter.Tk()
window.title("Image Watermarking App")
window.minsize(width=700, height=600)

label1 = tkinter.Label(text="Choose Image: ")
# label1.place(x=100, y=50)
label1.grid(row=0, column=0)

button1 = tkinter.Button(text="Select", command=select_image)
# button1.place(x=200, y=50)
button1.grid(row=0, column=1)

image_label = tkinter.Label()
# image_label.place(x=100, y=100)
image_label.grid(row=1, column=0)

label2 = tkinter.Label(text="Choose Watermark Image: ")
# label2.place(x=100, y=320)
label2.grid(row=2, column=0)

button2 = tkinter.Button(text="Select", command=select_watermark_image)
# button2.place(x=250, y=320)
button2.grid(row=2, column=1)

watermark_label = tkinter.Label()
# watermark_label.place(x=100, y=350)
watermark_label.grid(row=3, column=0)

label3 = tkinter.Label(text="Press 'Apply' to Apply Watermark: ")
# label3.place(x=100, y=500)
label3.grid(row=4, column=0)

button3 = tkinter.Button(text="Apply", command=watermark)
# button3.place(x=250, y=320)
button3.grid(row=4, column=1)

label4 = tkinter.Label(text="Watermarked image:")
label4.grid(row=0, column=2)

watermarked_label = tkinter.Label()
# watermark_label.place(x=100, y=350)
watermarked_label.grid(row=1, column=2)

button3 = tkinter.Button(text="Save", command=save_image)
# button3.place(x=250, y=320)
button3.grid(row=2, column=2)

button4 = tkinter.Button(text="Reset", command=reset_everything)
# button3.place(x=250, y=320)
button4.grid(row=2, column=3)

window.mainloop()
