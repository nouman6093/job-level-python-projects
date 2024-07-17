#creates a birthday letter for each person in the given list:

with open("names.txt", mode="w") as names_files:
    names_files.write("Nouman\n")
    names_files.write("Hameed\n")
    names_files.write("Asad\n")
    names_files.write("Umar\n")
    names_files.write("Aslam\n")
    names_files.write("Ahmad\n")
    names_files.write("Irdum\n")

with open("names.txt", mode="r") as names_files:
    names = names_files.readlines() #reads lines and then converts them into a list
    print(names)

with open("letter.txt", mode="w") as letter_file:
    letter_file.write("Dear [name],\n")
    letter_file.write("You are invited to my birthday this Saturday.\n")
    letter_file.write("Hope you can make it!\n")
    letter_file.write("Nouman Hameed")

with open("letter.txt", mode="r") as letter_file:
    letter = letter_file.read()
    for i in names:
        print(letter.replace("[name]", i.strip()))
        with open(f"letter_for_{i.strip()}.txt", mode="w") as completed_letter:
            completed_letter.write(letter.replace("[name]", i.strip()))
