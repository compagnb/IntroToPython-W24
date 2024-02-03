import turtle

mike=turtle.Turtle()
mike.color("orange")
mike.shape("turtle")

mike.begin_fill()
for x in range(0,4):
    mike.forward(100)
    mike.right(90)
mike.end_fill()

raph=turtle.Turtle()
raph.color("red")
raph.shape("turtle")

raph.begin_fill()
for x in range(0,4):
    raph.forward(-100)
    raph.right(90)
raph.end_fill()

dom=turtle.Turtle()
dom.color("purple")
dom.shape("turtle")

dom.begin_fill()
for x in range(0,4):
    dom.forward(-100)
    dom.right(-90)
dom.end_fill()
