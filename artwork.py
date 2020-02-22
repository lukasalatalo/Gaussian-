# Author: Lukas Alatalo
# McGill ID: 260923751
# Assignment 1, Question 2

# Your code here.
from turtle import forward,right,left,speed,circle,up,down

def move(d): #moves the drawing mouse away from the other shapes
    up()
    left(90)
    forward(d)
    down()

speed("fastest")

for i in range(5):  #draws a pentagon.
    forward(100)
    right(72)
move(50)

for i in range(4):   #draws a square.
    forward(100)
    right(90)
    
move(200)

rad = 50 
for i in range(2): #draws a circle within a circle
    circle(rad,360)
    up()
    right(90)
    forward(rad)
    left(90)
    down()
    rad= rad*2

#This code moves the drawing mouse to the bottom right of the frame.
up()
left(90)
forward(500)
left(90)
forward(500)
down()

#This code writes the first letter of my first name, L.
right(90)
forward(50)
left(90)
forward(40)