# Liam O'Hara

import turtle

# Create a turtle window with a grey background
window = turtle.Screen()
window.title("Lab 3")
window.setup(width=500, height=500)
window.bgcolor("grey")

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")

# Set the color of the turtle's line to your favorite color
favorite_color = "blue"  # Change this to your favorite color
t.color(favorite_color)

# Draw an equilateral triangle
side_length = 200

t.penup()
t.goto(-side_length / 2, 0)  # Move to the starting point
t.pendown()

for _ in range(3):
   t.forward(side_length)
   t.left(120)

# Keep the window open
turtle.done()