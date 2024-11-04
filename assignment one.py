# importing Required modules
# For More Projects Visit :
# Codewithcurious.com/projects
import turtle
import colorsys

# Create window to Display Pattern
t = turtle.Turtle()
s = turtle.Screen()

# Setting Background color
s.bgcolor("white")

# Speed of turtle to draw pattern
t.speed(12)
h = 200


# Loop for drawing Pattern
for i in range(80):
    c = colorsys.hsv_to_rgb(h,0.001,0.2)
    h+=1/h
    t.color(c)
    t.left(200)
    t.forward(100)
    t.right(130)
    
for j in range(80):
    c = colorsys.hsv_to_rgb(h,0.4,0.75)
    t.color(c)
    t.forward(200)
    t.left(230)

for k in range(80):
    c = colorsys.hsv_to_rgb(h,0.1,0.8)
    t.color(c)
    t.forward(250)
    t.right(250)
