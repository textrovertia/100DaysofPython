import colorgram as c
import turtle as t
import random

# extract all colors from the picture

rgb_colors = []
colors = c.extract("image.jpg", 50)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


color_list = [(237, 224, 201), (217, 218, 226), (203, 157, 109), (238, 215, 227), (105, 109, 129), (138, 141, 157),
              (219, 233, 222), (222, 212, 119), (168, 77, 46), (195, 146, 171), (175, 155, 46), (105, 111, 172),
              (16, 20, 58), (229, 168, 195), (14, 36, 18), (219, 77, 55), (147, 79, 91), (35, 32, 13), (144, 160, 149),
              (179, 22, 9), (97, 113, 101), (200, 77, 96), (237, 170, 158), (43, 44, 113), (179, 19, 32), (39, 20, 37),
              (182, 179, 222), (219, 210, 20), (115, 135, 121), (178, 203, 177), (73, 75, 35), (45, 76, 45),
              (170, 198, 208), (44, 74, 80), (107, 134, 138), (247, 10, 18), (248, 14, 13)]

tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.setx(-300)
tim.speed("fastest")


def change_color():
    return random.choice(color_list)



def move_right():
    for i in range(10):
        tim.pendown()
        tim.color(change_color())
        tim.dot(20)
        tim.up()
        tim.forward(40)


def move_up():
    tim.penup()
    tim.setx(-300)
    tim.sety(tim.ycor()+40)


def draw_dots():
    for i in range(0, 10):

        move_right()
        move_up()

draw_dots()


screen = t.Screen()
screen.exitonclick()
