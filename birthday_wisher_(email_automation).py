#download required files here: https://drive.google.com/drive/folders/1gluaYhQAvO03CiJhyrIpNeNYIjl9jA2Y?usp=drive_link
import datetime
import pandas
import random
import smtplib

my_email = "enter your email here"
my_password = "enter password which you got from google security"

today = datetime.datetime.now()
today_tuple = (datetime.datetime.now().month, datetime.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

birthday_dictionary = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dictionary:
    birthday_person = birthday_dictionary[today_tuple]
    file_path = f"letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")
