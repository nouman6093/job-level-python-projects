from turtle import Turtle, Screen
import pandas

with open("states.csv", mode="w") as data:
    data.write("state,x,y\n"
               "Alabama,139,-77\n"
               "Alaska,-204,-170\n"
               "Arizona,-203,-40\n"
               "Arkansas,57,-53\n"
               "California,-297,13\n"
               "Colorado,-112,20\n"
               "Connecticut,297,96\n"
               "Delaware,275,42\n"
               "Florida,220,-145\n"
               "Georgia,182,-75\n"
               "Hawaii,-317,-143\n"
               "Idaho,-216,122\n"
               "Illinois,95,37\n"
               "Indiana,133,39\n"
               "Iowa,38,65\n"
               "Kansas,-17,5\n"
               "Kentucky,149,1\n"
               "Louisiana,59,-114\n"
               "Maine,319,164\n"
               "Maryland,288,27\n"
               "Massachusetts,312,112\n"
               "Michigan,148,101\n"
               "Minnesota,23,135\n"
               "Mississippi,94,-78\n"
               "Missouri,49,6\n"
               "Montana,-141,150\n"
               "Nebraska,-61,66\n"
               "Nevada,-257,56\n"
               "New Hampshire,302,127\n"
               "New Jersey,282,65\n"
               "New Mexico,-128,-43\n"
               "New York,236,104\n"
               "North Carolina,239,-22\n"
               "North Dakota,-44,158\n"
               "Ohio,176,52\n"
               "Oklahoma,-8,-41\n"
               "Oregon,-278,138\n"
               "Pennsylvania,238,72\n"
               "Rhode Island,318,94\n"
               "South Carolina,218,-51\n"
               "South Dakota,-44,109\n"
               "Tennessee,131,-34\n"
               "Texas,-38,-106\n"
               "Utah,-189,34\n"
               "Vermont,282,154\n"
               "Virginia,234,12\n"
               "Washington,-257,193\n"
               "West Virginia,200,20\n"
               "Wisconsin,83,113\n"
               "Wyoming,-134,90\n")

screen = Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif") #download this image from the following link: https://i0.wp.com/whatsanswer.com/wp-content/uploads/2018/03/Blank-outline-map-of-the-United-States-611.jpg?fit=2000%2C1354&ssl=1
t1 = Turtle("blank_states_img.gif") #name the image exactly as what is written here and store image in the same project folder where you have stored main.py file

contents = pandas.read_csv("states.csv")
all_states = contents["state"].to_list()  #column of state converted into a list

guessed_states = []
while len(guessed_states) < 50:
    input1 = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another states name? or type 'Exit'")
    if input1 == "Exit" or input1 == "exit":
        missing_states = []
        for i in all_states:
            if i not in guessed_states:
                missing_states.append(i)
                data1 = pandas.DataFrame(missing_states)
                data1.to_csv("states_to_learn.csv")
        break
    elif input1 in all_states:
        guessed_states.append(input1)
        t2 = Turtle()
        t2.hideturtle()
        t2.penup()
        state_data = contents[contents["state"] == input1]
        t2.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))   #alternative to this line is below but it may cause exceptional errors:
        # t2.goto(int(state_data.x), int(state_data.y))
        t2.write(input1)
