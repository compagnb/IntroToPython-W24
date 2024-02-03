#week 5
import turtle

colorOfT=input("what color do you want your turtle ")
shapeOfT=input("what shape do you want your turtle ")
drawShape=input("what shape do you want your turtleto draw? ")
howBig=input("how big do you want the shape to be? ")
shapeFill=input("do you want the shape filled in (yes or no)? ")


              
t=turtle.Turtle()
t.shape(shapeOfT.lower().strip())
t.color(colorOfT.lower().strip())
if shapeFill=="yes":
    t.begin_fill()



if drawShape =="square":
    for i in range (0,4):
        t.forward(int(howBig))
        t.right (90)
elif drawShape=="triangle":
    for i in range(0,3):
        t.forward(int(howBig))
        t.right(360/3)
if drawShape=="circle":
    t.circle(int(howBig))
if drawShape =="star":
    for i in range (0,19):
        t.forward(int(howBig))
        if i%2==0:
            t.left(175)
        else:
            t.left(225)

if shapeFill=="yes":
    t.end_fill()


t.hideturtle()     
