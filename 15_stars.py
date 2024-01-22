import turtle

wn = turtle.Screen()
my_art = turtle.Turtle()

my_art.penup()
my_art.forward(-200)
my_art.pendown()


branch_length = 100

# Draw 1
my_art.color("red")
for i in range(5):
    my_art.forward(branch_length)
    my_art.right(144)


my_art.penup()
my_art.forward(200)
my_art.pendown()

my_art.color("green")
branch_length = 50
for i in range(5):
    for j in range(2):
        my_art.forward(branch_length)
        my_art.left(72)
    my_art.left(144)


turtle.exitonclick()
