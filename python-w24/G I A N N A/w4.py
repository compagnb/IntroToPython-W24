
#Turtle Graphics
#baldaglia.forward(1000)
#baldaglia.backward(100000)
#Baldaglia.penup()

import turtle

baldaglia = turtle.Turtle()
baldaglia.shape("turtle")
baldaglia.color("blue")

baldaglia.left(360)
##baldaglia.begin_fill()
##baldaglia.forward(100)
##baldaglia.left(90)
##baldaglia.forward(100)
##baldaglia.left(90)
##baldaglia.forward(100)
##baldaglia.left(90)
##baldaglia.forward(100)
##baldaglia.end_fill()                    
##baldaglia.left(90)
##baldaglia.penup()
##baldaglia.forward(200)
##baldaglia.pendown()
##baldaglia.begin_fill()
##baldaglia.forward(100)
##baldaglia.left(90)
##baldaglia.forward(100)
##baldaglia.left(90)
##baldaglia.forward(100)
##baldaglia.left(90)
##baldaglia.forward(100)
##baldaglia.end_fill()

##for x in range (0,4):
##  baldaglia.penup()
##  baldaglia.forward(50)
##  baldaglia.pendown()
##  baldaglia.forward(100)
##  baldaglia.right(90)              
##  baldaglia.penup()
##  baldaglia.forward(50)
##  baldaglia.pendown()
##  baldaglia.forward(100)

##for i in range (0,3):            
## baldaglia.forward(500)
## baldaglia.left(360/3)

baldaglia.begin_fill()
for i in range (0,8):
    baldaglia.right(360)
    baldaglia.forward(100)
    baldaglia.left(45)
    baldaglia.end_fill()
    baldaglia.right(360)

  
                
    
