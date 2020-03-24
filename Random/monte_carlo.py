# TODO:
# - Fix points plot velocity;
# - Add ticks to axes;
# - Fix weird bug of window closing;


from turtle import Turtle, Screen
import numpy as np
import tkinter as tk

FONT = ("Arial", 10)


def draw_circle(radius):
    turtle = Turtle(visible=False)
    turtle.setpos(0, 0)
    turtle.penup()

    turtle.right(90)
    turtle.forward(radius)
    turtle.right(270)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()


def draw_square(x_vert, y_vert):
    turtle = Turtle(visible=False)
    turtle.penup()

    for i in range(len(x_vert)):
        turtle.goto(x_vert[i], y_vert[i])
        turtle.pendown()


def draw_axis(length):
    turtle = Turtle(visible=False)
    turtle.pensize(1)
    turtle.penup()
    turtle.setpos(0, 0)

    turtle.pendown()
    turtle.goto(0, length)
    turtle.setpos(0, 0)
    turtle.goto(0, -length)
    turtle.setpos(0, 0)

    turtle.goto(-length, 0)
    turtle.setpos(0, 0)
    turtle.goto(length, 0)
    turtle.setpos(0, 0)


def plot_n_calculate(n, radius):
    turtle = Turtle(visible=False)
    turtle.speed('fastest')
    turtle.penup()

    x_ran = []
    y_ran = []

    for _ in range(0, n):
        x_ran.append(np.random.random_integers(-radius, radius + 1))
        y_ran.append(np.random.random_integers(-radius, radius + 1))

    score = 0

    for i in range(len(x_ran)):
        if x_ran[i] ** 2 + y_ran[i] ** 2 <= radius ** 2:
            score += 1

    for i in range(len(x_ran)):
        turtle.goto(x_ran[i], y_ran[i])
        turtle.dot(size=3)

    return 4 * (score / n)


def text_at_xy(x, y, text):
    turtle = Turtle(visible=False)
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(text, font=FONT)


def main():
    screen = Screen()
    screen.setup(width=800, height=600, startx=250, starty=0)

    screen.title('Monte Carlo method for estimating the value of pi')
    radius = screen.numinput('Radius of the circle input', 'Your radius of choose: ', minval=0, maxval=300)
    points = int(
        screen.numinput('Number of points that will be generated', 'Number of points: ', minval=0, maxval=3000))
    draw_axis(radius * 0.8)
    draw_square([-0.5 * radius, 0.5 * radius, 0.5 * radius, -0.5 * radius, -0.5 * radius],
                [0.5 * radius, 0.5 * radius, -0.5 * radius, -0.5 * radius, 0.5 * radius])
    draw_circle(radius * 0.708)
    pi_aprox = plot_n_calculate(points, radius)
    text_at_xy(-270, -250, 'Estimated value of pi: {}'.format(pi_aprox))
    tk.mainloop()


if __name__ == '__main__':
    main()
