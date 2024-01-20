#Week 3 Interplanetary Scale

# Ratios For Conversion
lbs2kgs=.453592
mercury=.0553
mars=.107
venus=.815
earth=1
uranus=14.5
neptune=17.1
saturn=95.2
jupiter=318
pluto=.2
earthMoon=.165

# taking inputs from the user
# inputs will always be Strings!
print("Welcome to Barb's Space Ship!")
print("Today we will be traveling to different planets, but first I need some information.")
name=input("Please Enter Your Name.")
weightInLbs=input("Please Enter Your Weight(In Lbs).")

#conversions
weightInKgs=int(weightInLbs)*lbs2kgs
#print(weightInKgs)
weightOnUranus=weightInKgs*uranus
#print(weightOnUranus)

print("Welcome " + name + "!")
print("Our first stop is Uranus, and here you will weigh " + str(weightOnUranus) +"kgs.")








