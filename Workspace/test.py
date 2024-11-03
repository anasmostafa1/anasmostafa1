import turtle
import math

# Set up the turtle screen
turtle.setup(800, 800)
turtle.bgcolor("black")
turtle.speed(0)  # Fastest drawing speed
turtle.width(2)  # Line width
turtle.colormode(255)  # Use RGB color mode

# Parameters for the spiral pattern
radius = 1  # Starting radius, will increase over time
angle_increment = math.pi / 10# Increment angle in radians

# Start drawing the infinite pattern
while True:
    # Calculate x and y positions using sin and cos with increasing radius
    x = radius * math.cos(radius)
    y = radius * math.sin(math.pi * radius)

    # Set the pen color using a gradient pattern
    r = int((math.sin(radius * 0.1) + 1) * 127)
    g = int((math.cos(radius * 0.1) + 1) * 127)
    b = int((math.sin(radius * 0.15) + 1) * 127)
    turtle.pencolor(r, g, b)

    # Move to the calculated position and draw a small dot
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(5)  # Draws a dot at the position

    # Increase radius for next loop iteration, creating a spiral
    radius += angle_increment  # Adjusts how tight the spiral is

# No need to call turtle.done() because it's infinite
