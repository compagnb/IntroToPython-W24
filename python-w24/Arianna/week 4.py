#week 4:Turtle Graphics
import turtle
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("green")

##bob.begin_fill()
##bob.forward(100)
##bob.right(90)
##bob.forward(100)
##bob.right(90)
##bob.forward(100)
##bob.right(90)
##bob.forward(100)
##bob.forward(100)
##bob.right(90)
##bob.forward(100)
##bob.right(90)
##bob.forward(100)
##bob.end_fill(100)

 ##boob.shape("turtle")
 ##boob.color("green")

 ##boob.forward(500)
 ##boob.right(360/3)

puffs = turtle.Turtle()
puffs.shape("turtle")
puffs.color("red")
puffs.begin_fill()
for h in range(0,8):
    puffs.forward(100)
    puffs.right(360/8)
puffs.end_fill()
