# Liam O'Hara

import turtle

# Create a turtle window
window = turtle.Screen()
window.title("Lab 1")
window.setup(width=1000, height=1000)

# Create a turtle object
t = turtle.Turtle()

# Draw a rectangle
t.penup()
t.goto(0, 0)  # Move to the starting point
t.pendown()
for _ in range(2):
   t.forward(250)  # Draw the first side
   t.left(90)  # Turn left by 90 degrees
   t.forward(100)  # Draw the second side
   t.left(90)  # Turn left by 90 degrees

# Keep the window open
turtle.done()