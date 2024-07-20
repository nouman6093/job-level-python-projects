import tkinter

def calculate(event=None):
    miles = float(entry1.get())
    kilometers = miles * 1.60934
    label3["text"] = kilometers

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=160, height=70)

entry1 = tkinter.Entry(width=10)
entry1.grid(column=1, row=0)
entry1.bind("<Return>", calculate)
entry1.focus_set()

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

label2 = tkinter.Label(text="is equal to: ")
label2.grid(column=0, row=1)

label3 = tkinter.Label(text=0)
label3.grid(column=1, row=1)

label4 = tkinter.Label(text="Km")
label4.grid(column=2, row=1)

button1 = tkinter.Button(text="Calculate", command=calculate)
button1.grid(column=1, row=2)

window.mainloop()
