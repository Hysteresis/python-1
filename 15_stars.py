import turtle

wn = turtle.Screen()
my_art = turtle.Turtle()

my_art.penup()
my_art.forward(-200)
my_art.pendown()

my_art.speed(100)


branch_length = 100


# Draw 1
# my_art.color("red")
# my_art.fillcolor("red")
# my_art.begin_fill()
# for i in range(5):
#     my_art.forward(branch_length)
#     my_art.right(144)
#
#
#
# my_art.penup()
# my_art.forward(200)
# my_art.pendown()

# Draw 2
# my_art.color("green")
# my_art.fillcolor("mediumspringgreen")
# my_art.begin_fill()
# branch_length = 50
# for i in range(5):
#     for j in range(2):
#         my_art.forward(branch_length)
#         my_art.left(72)
#     my_art.left(144)
#
# my_art.end_fill()


def stars():
    for i in range(5):
        my_art.forward(branch_length)
        my_art.right(144)


def circles():
    for i in range(36):
        r = 1 - i / 36.0
        g = 0.5
        b = 1.0 - i / 36.0
        my_art.pencolor(r, g, b)
        my_art.circle(90)
        my_art.right(10)


for i in range(0, 2):
    circles()
    my_art.forward(i * 10 + 1)

turtle.exitonclick()
