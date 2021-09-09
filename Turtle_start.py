#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.Turtle()
turtle.penup()
turtle.goto(22,70)
turtle.pendown()
turtle.pensize(5)
turtle.forward(50)
turtle.circle(20)
turtle.backward(100)
turtle.circle(20)
turtle.penup()
turtle.goto(10,15)
turtle.pendown()
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.penup()

turtle.goto(180,50)
turtle.pendown()
turtle.pensize(15)
turtle.color(20,50,100)
turtle.begin_fill()
turtle.fillcolor("red")
turtle.forward(50)
turtle.right(72)
turtle.forward(50)
turtle.right(72)
turtle.forward(50)
turtle.right(72)
turtle.forward(50)
turtle.right(72)
turtle.forward(50)
turtle. end_fill()








#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#   turtle.done()
''