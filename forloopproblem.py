#Your challenge

#* Get turtle to draw an octagon 

#* Hint: to calculate the angle, you take 360 degrees and divide it by the number of sides of the shape you are drawing # type: ignore

#* Extra challenge: Let the user specify how many sides the object will have and draw whatever they ask

#* Double bonus challenge, add a nested loop to draw a smaller version of the object inside!.
import turtle
n=int(input())
for i in range(n):
    turtle.forward(100)
    turtle.right(360/n)
    for i in range(1):
        turtle.forward(50)
        turtle.right(360/n)