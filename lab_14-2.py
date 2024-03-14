# Liam O'Hara

import turtle
import math

# Create a turtle window
window = turtle.Screen()
window.title("Lab 2")
window.setup(width=500, height=500)

# Create a turtle object
t = turtle.Turtle()

# Draw an equilateral triangle
side_length = 100

t.penup()
t.goto(0, 0)  # Move to the starting point
t.setheading(60)  # Set initial angle to draw equilateral triangle
t.pendown()

for _ in range(3):
   t.forward(side_length)
   t.left(120)

# Keep the window open
turtle.done()