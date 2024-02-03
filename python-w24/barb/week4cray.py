import turtle
import random

minions=[]
maxMinions=100
wn = turtle.Screen()
wn.tracer(5)
counter = 0

for i in range(0,maxMinions):
    minions.append(turtle.Turtle())

for minion in minions:
    minion.color(random.randint(0,1),random.randint(0,1),random.randint(0,1))
    minion.shape("turtle")
    minion.penup()
    minion.setheading(random.randint(0,360))
    #minion.goto(random.randint(-300,300),random.randint(-300,300))
    minion.goto(counter * 10, counter * 10)
    minion.pendown()
    minion.speed(0)

counter=0
while True:
    for minion in minions:
          #if counter%10==0:
        minion.right(10)
        minion.forward(15)
        counter=counter+1

    
