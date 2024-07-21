from tkinter import *
from tkinter import messagebox
import random
import pyperclip    #needs to be separately installed in interpretar

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    entry3.insert(0, password)
    pyperclip.copy(password)

def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please, make sure you haven't left any field empty.")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")
        if is_okay:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                entry1.delete(0, END)
                entry3.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20) #padding means space between content (image) and borders

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")  #download this image from following link, store it in project folder where you have stored main.py. here is the link: https://drive.google.com/file/d/1uMzLA77KY4n4kvDYjoUWGsvqvgqR0Vuo/view?usp=drive_link
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)

entry1 = Entry(width=35)
entry1.focus()
entry1.grid(column=1, row=1, columnspan=2)

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

entry2 = Entry(width=35)
entry2.insert(0, "dummyEmail@gmail.com")
entry2.grid(column=1, row=2, columnspan=2)

label3 = Label(text="Password:")
label3.grid(column=0, row=3)

entry3 = Entry(width=21)
entry3.grid(column=1, row=3)

button1 = Button(text="Generate Password", command=generate_password)
button1.grid(column=2, row=3)

button2 = Button(text="Add", width=36, command=save)
button2.grid(column=1, row=4, columnspan=2)

window.mainloop()
