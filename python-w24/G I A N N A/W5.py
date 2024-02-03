
import turtle

colorOfrober=input("what color do you want your drawing icon ")
shapeOfrober=input("what shape do you want your drawing icon ")
drawshape=input("What shape do you want the turtle to draw ")
howbig=input("How big (In pixels)  do you want the shape to be? ")
shapeFill=input("do you want the shape to be filled in (YES/NO)?" )

rober= turtle.Turtle()
rober.color(colorOfrober.lower().strip())
rober.shape(shapeOfrober.lower().strip())
                                        
rober=turtle. Turtle()
rober.shape (shapeOfrober.lower().strip())
rober.color(colorOfrober.lower().strip())
if shapeFill=="yes":
    rober.begin_fill()

if drawshape=="square":
    for i in range (0,4):
      rober.forward(int(howbig))
      rober.right(90)
elif drawshape== "triangle":
    for i in range (0,3):
     rober.forward(int(howbig))
     rober.right (360/3)
     
if drawshape=="circle":
    rober.circle(int(howbig))

if drawshape=="octogon":
 for i in range (0,8):
  rober.forward(int(howbig))
  rober.right (45)
 

if shapeFill=="yes":
    rober.end_fill()

    
