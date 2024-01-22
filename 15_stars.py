import turtle

wn = turtle.Screen()
my_art = turtle.Turtle()

my_art.penup()
my_art.forward(-200)
my_art.pendown()


branch_length = 100

# Draw 1
my_art.color("red")
my_art.fillcolor("red")
my_art.begin_fill()
for i in range(5):
    my_art.forward(branch_length)
    my_art.right(144)



my_art.penup()
my_art.forward(200)
my_art.pendown()

# Draw 2
my_art.color("green")
my_art.fillcolor("green")
my_art.begin_fill()
branch_length = 50
for i in range(5):
    for j in range(2):
        my_art.forward(branch_length)
        my_art.left(72)
    my_art.left(144)

my_art.end_fill()


turtle.exitonclick()
