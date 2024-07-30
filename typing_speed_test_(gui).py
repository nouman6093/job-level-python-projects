import time
import tkinter

def start_typing(event):
    global starting_time
    starting_time = time.time()

def typing_speed():
    ending_time = time.time()
    text = area1.get("1.0", "end-1c")   #"1.0" refers to the very beginning of the text area. "end" refers to the very end of the text area. its just specifying the range from where to where it should get the text
    words = len(text.split()) #used to split a string into a string of words
    time_taken = ending_time - starting_time
    speed = words / time_taken * 60
    label2.config(text=f"Your Typing Speed is: {speed} words per minute")

starting_time = time.time()

window = tkinter.Tk()
window.title("Typing Speed Test")
window.minsize(width=500, height=500)

label1 = tkinter.Label(text="Enter Text: ")
label1.grid(row=0, column=0)

scrollbar1 = tkinter.Scrollbar()
scrollbar1.grid(row=0, column=2, sticky='ns') #'ns' means that the widget should stick to the North and South sides of the cell

area1 = tkinter.Text(width=40, height=10, yscrollcommand=scrollbar1.set)
area1.grid(row=0, column=1)

button1 = tkinter.Button(text="Calculate Speed", command=typing_speed)
button1.grid(row=1, column=0)

label2 = tkinter.Label(text=f"Your Typing Speed is: ")
label2.grid(row=1, column=1)

window = tkinter.mainloop()
