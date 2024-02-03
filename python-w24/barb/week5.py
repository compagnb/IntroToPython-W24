#Week 5
import turtle

test=input("type something")
print(test.lower().strip())

shapeOfT=input("what shape do you want your turtle? ")
colorOfT=input("what color do you want your turtle? ")
drawShape=input("what shape do you want the turtle to draw? ")
howBig=input("how big (in pixels) do you want the shape to be? ")
shapeFill=input("do you want the shape filled in (yes or no)? ")

t=turtle.Turtle()
t.shape(shapeOfT.lower().strip())
t.color(colorOfT.lower().strip())

if shapeFill=="yes":
    t.begin_fill()
if drawShape=="square":
    for i in range(0,4):
        t.forward(int(howBig))
        t.right(90)
if drawShape=="triangle":
    for i in range(0,3):
        t.forward(int(howBig))
        t.right(360/3)
if drawShape=="circle":
    t.circle(int(howBig))
if drawShape=="octogon":
    for i in range(0,8):
        t.forward(int(howBig))
        t.right(360/8)
if drawShape=="star":
    for i in range(0,19):
        t.forward(int(howBig))
        if i%2==0:
            t.left(175)
        else:
            t.left(225)
         
if shapeFill=="yes":
    t.end_fill()

t.hideturtle()



    


        
