import turtle

wn = turtle.Screen()
my_art = turtle.Turtle()

# determinate the length of a branch
branch_length = 50


for i in range(10):
    my_art.forward(branch_length)
    if i % 2 == 0:
        my_art.left(72)
    else:
        my_art.right(144)


turtle.exitonclick()
