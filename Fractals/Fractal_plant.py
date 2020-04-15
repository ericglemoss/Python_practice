# Idea for code base on: https://en.wikipedia.org/wiki/L-system


import turtle

fwd = 4
turn = 25
pile = []
directions_pile = []


turtle.pencolor('GREEN')
turtle.left(90)
turtle.penup()
turtle.setpos(0, -350)
turtle.pendown()
turtle.shapesize(0.1)
turtle.shape("circle")


def gen(n):
    """
    :param n: number of iterations (generations) you want to draw;
    :return: str with letters that follow the rule of the system (X → F+[[X]-X]-F[-FX]+X), (F → FF).
    """
    input_rule = ["F", "X"]
    output_rule = ["FF", "F+[[X]-X]-F[-FX]+X"]
    result = "X"
    tmp = ""

    for i in range(n):
        for j in range(len(result)):
            for k in range(len(input_rule)):
                if result[j] == input_rule[k]:
                    tmp += output_rule[k]
                    break
                if k == len(input_rule)-1:
                    tmp += result[j]
        result = tmp
        tmp = ""
    return result


def draw_plant(vec):
    """
    :param vec: str generated following the system's rule;
    :return: draw plant on screen with turtle module.
    """
    for x in vec:
        if x == 'F':
            turtle.forward(fwd)

        elif x == '-':
            turtle.left(turn)
        elif x == '+':
            turtle.right(turn)

        elif x == '[':
            pile.append(turtle.pos())
            directions_pile.append(turtle.heading())

        elif x == ']':
            turtle.penup()
            post = pile.pop()
            direc = directions_pile.pop()
            turtle.setpos(post)
            turtle.setheading(direc)
            turtle.pendown()

    turtle.hideturtle()
    turtle.done()

draw_plant(gen(6))
