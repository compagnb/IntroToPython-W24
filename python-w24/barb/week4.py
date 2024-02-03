#Week 4: Turtle Graphics
import turtle #allows us to use the code from the turtle library/module

mike = turtle.Turtle() #creates an instance of the class Turtle 
mike.shape("turtle")
mike.color("orange")

##
## mike.right(90) # rotates the turtle from in the direction its facing
## mike.backward(40)# moves the turtle backward in the direction its facing
## mike.left(270) # rotates the turtle from in the direction its facing
## mike.forward(100) # moves the turtle forward in the direction its facing
## mike.penup() # stops the turtle from drawing
## mike.pendown()# starts the turtle drawing again
## mike.begin_fill() # starts to begin fil
## mike.end_fill() # ends the fill shape

# Make reg square
##mike.forward(100)
##mike.right(90)
##mike.forward(100)
##mike.right(90)
##mike.forward(100)
##mike.right(90)
##mike.forward(100)

# Making a square without corners
raph = turtle.Turtle()
raph.color("red")
raph.shape("turtle")

##for x in range(0,4):
##    raph.penup()
##    raph.forward(50)
##    raph.pendown()
##    raph.forward(100)
##    raph.penup()
##    raph.forward(50)
##    raph.pendown()
##    raph.right(90)

# Making a triangle
dom = turtle.Turtle()
dom.shape("turtle")
dom.color("purple")

for i in range(0,3):
    dom.forward(50)
    dom.right(360/3)

# Making a octogon

# Making a filled in octogon 







