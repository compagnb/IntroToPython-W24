lbs2kgs=.453592
neptune=17.19
print("Welcome to Arianna's space ship!")
print("We are traveling to Neptune")
      
name=input("Please Enter Your Name.")
weightInLbs=input("Please Enter Your weight.")

weightInkgs=int(weightInLbs)*lbs2kgs
print(weightInkgs)
weightOnneptune=weightInkgs*neptune
print(weightOnneptune)
           
print("Welcome " +name+"!")
print("Our first stop is Neptune, and here you will weigh "+str(weightOnneptune) +".")
