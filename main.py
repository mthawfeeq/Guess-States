import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess the Country! Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

input_data = pandas.read_csv("50_states.csv")
all_states = input_data["state"].tolist()
guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                   prompt="What's another state's name? ").title()

    if user_answer == "exit":
        break
    if user_answer in all_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = input_data[input_data.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_answer)


# def getting_mouse_clicks_coordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(getting_mouse_clicks_coordinates)
# turtle.mainloop()


screen.exitonclick()