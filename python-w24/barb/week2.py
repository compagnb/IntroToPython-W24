# Mad Libs!

# Masking allows strings and ints to be disguised as each other
# int() will disguise as a number
# str() will disguise as a string
# this comes in handy because we CAN'T add strings and integers!

statement1 = "Hi my name is "
statement2 = ". I am currently "
statement3 = " years old. That means in "
statement4 = " years I will be able to drive."

name = input("What is your name?")
age = input("What is your age?")
drivingAge = 16
yearsToDrive = drivingAge - int(age)

story = statement1 + name + statement2 + age + statement3 + yearsToDrive + statement4
print(story)
