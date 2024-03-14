# Liam O'Hara

import turtle

# Create a default-size turtle window
window = turtle.Screen()
window.title("Lab 5")

# Create a turtle object
t = turtle.Turtle()

# Function to move the turtle forward
def move_forward():
   t.forward(10)

# Function to move the turtle backward
def move_backward():
   t.backward(10)

# Function to turn the turtle left
def turn_left():
   t.left(90)

# Function to turn the turtle right
def turn_right():
   t.right(90)

# Bind keyboard events to functions
window.listen()
window.onkey(move_forward, "Up")
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")

# Keep the window open
window.mainloop()