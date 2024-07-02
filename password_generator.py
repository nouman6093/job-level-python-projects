#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for i in range(nr_letters):
    ra = random.randint(0,len(letters) - 1)
    password += letters[ra] #yeh line sahi samajh nahi aayi

for i in range(nr_symbols):
    ra = random.randint(0, len(symbols) - 1)
    password += symbols[ra] #yeh line sahi samajh nahi aayi

for i in range(nr_numbers):
    ra = random.randint(0, len(numbers) - 1)
    password += numbers[ra] #yeh line sahi samajh nahi aayi

password_list = list(password)  #converts string into list because following .shuffle function can be applied on list but not on a string
random.shuffle(password_list)
final = ''.join(password_list)  #now converting that list into string again

print(f"Your Password is: {final}")
