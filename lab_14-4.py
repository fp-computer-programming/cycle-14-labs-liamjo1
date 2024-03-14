# Liam O'Hara

import turtle

# Create a default-size turtle window with title "Lab 4"
window = turtle.Screen()
window.title("Lab 4")

# Create a turtle object
t = turtle.Turtle()

# Change the turtle's speed and color
t.speed(3)  # Set the drawing speed to 3 (medium speed)
t.color("red")  # Set the color of the turtle

# Create a stamp of the turtle at the origin
t.stamp()

# Create a square with top-left vertex at position (100, 100) and sides of length 100
square_side = 100

t.penup()
t.goto(100, 100)  # Move to the starting point
t.pendown()

t.begin_fill()  # Begin filling the square
for _ in range(4):
   t.forward(square_side)
   t.right(90)
t.end_fill()  # End filling the square

# Fill the square with another color
t.fillcolor("yellow")

# Keep the window open
turtle.done()