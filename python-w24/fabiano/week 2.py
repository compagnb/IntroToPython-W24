#mad libs!
#Masking allows strings and ints to be disguised as each other
#int()will diguise as a number
#str()will diguise as a string
#this comes in handy because we cant add strings and integgers!
 
stament1 = "Hi my name is "
stament2 = ".I am currently "
stament3 = " years old. That means in "
stament4 = " years i will be able to drive."

name=input("what is your name?")
age=input("what is your Age?")
drivingAge=16
yearsToDrive=drivingAge-int (age)

story= stament1 + name + stament2 + age + stament3 + str (yearsToDrive) + stament4
print(story) 
 
