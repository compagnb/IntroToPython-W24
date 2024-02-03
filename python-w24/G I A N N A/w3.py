#ratios for conversions
lbs2kgs=.453592
Uranus=14.5
Venus=.815

print("welcome to the aquabus")
print("today we ar sailing to different planets")
name=input("please input your name.")
weightinlbs=input("please enter your weight")

weightinkgs= int(weightinlbs)*lbs2kgs
#print(weightinkgs)
weightonUranus=weightinkgs*Uranus
#print(weightonUranus)
print ("First we are going to Uranus")
print("Welcome" + name)
print("here you will weigh " + str(weightonUranus))

print ("next we are going to Neptune")
weightonVenus=weightinkgs*Venus
#print(weightonVenus)
print("here you will weigh " + str(weightonVenus))




