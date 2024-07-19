#creates a list of NATO Alphabets for whatever the word user inputs
import pandas

with open("alphabets.csv", mode="w") as data:
    data.write("letter,code\n"
    "A,Alfa\n"
    "B,Bravo\n"
    "C,Charlie\n"
    "D,Delta\n"
    "E,Echo\n"
    "F,Foxtrot\n"
    "G,Golf\n"
    "H,Hotel\n"
    "I,India\n"
    "J,Juliet\n"
    "K,Kilo\n"
    "L,Lima\n"
    "M,Mike\n"
    "N,November\n"
    "O,Oscar\n"
    "P,Papa\n"
    "Q,Quebec\n"
    "R,Romeo\n"
    "S,Sierra\n"
    "T,Tango\n"
    "U,Uniform\n"
    "V,Victor\n"
    "W,Whiskey\n"
    "X,X-ray\n"
    "Y,Yankee\n"
    "Z,Zulu\n")

contents = pandas.read_csv("alphabets.csv")
contents_dic = {row["letter"]:row["code"] for key, row in contents.iterrows()}

input1 = input("Enter A Word: ").upper()
l = [contents_dic[i] for i in input1]
print(l)
