# Liam O'Hara

import turtle
import tkinter as tk

# Function to draw a square
def draw_square(x, y):
   t.penup()
   t.goto(x, y)
   t.pendown()
   t.begin_fill()
   for _ in range(4):
       t.forward(100)
       t.left(90)
   t.end_fill()

# Prompt the user for a color
color = turtle.textinput("Color", "Enter a color name:")

# Prompt the user for a size
size = turtle.numinput("Size", "Enter a size (1-5):", minval=1, maxval=5)

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")

# Set the color and size of the turtle
t.color(color)
t.shapesize(size)

# Create an onclick event to draw a square
turtle.onscreenclick(draw_square, 1)

# Keep the window open
turtle.done()