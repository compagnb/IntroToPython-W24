#ratios for conversions
lbs2kgs=.453592
Uranus=14.5

print("welcome to the aquabus")
print("today we ar sailing to Uranus")
name=input("please input your name.")
weightinlbs=input("please enter your weight")

weightinkgs= int(weightinlbs)*lbs2kgs
#print(weightinkgs)
weightonUranus=weightinkgs*Uranus
#print(weightonUranus)
print("Welcome" + name)
print("here you will weigh " + str(weightonUranus))



