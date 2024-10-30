#code to draw a square
import turtle #turtle library used to draw lines in python
for steps in range(4): # here for loop used to run below steps  4 times
    # we can use any name inplace of steps
    turtle.forward(100)#draw a line of length 100pixel
    turtle.right(90)#turns the line in right angle
#nested square
for steps in range(4): 
    turtle.forward(100)
    turtle.right(90)
    for steps1 in range(4): 
        turtle.forward(110)#this loop will run 4 times 4 
        turtle.right(90)
#we can also use a variable to define range
a=int(input())
for steps in range(a):
    turtle.forward(100)
    turtle.right(360/a)