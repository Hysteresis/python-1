import turtle

wn = turtle.Screen()
my_art = turtle.Turtle()

# determinate the length of a branch
branch_length = 50

# draw a star
for i in range(5):
    for j in range(2):
        my_art.forward(branch_length)
        my_art.left(72)
    my_art.left(144)


turtle.exitonclick()
