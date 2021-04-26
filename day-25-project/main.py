import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

correct_states = []
correct_states_total = 0

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{correct_states_total}/50", prompt="What's another state's name").title()
    data = pandas.read_csv("50_states.csv")
    all_states = data.state

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_states ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_Learn")
        break

    for state in all_states:
        if state == answer_state:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[all_states == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
            correct_states.append(answer_state)
            correct_states_total += 1



#states to learn
