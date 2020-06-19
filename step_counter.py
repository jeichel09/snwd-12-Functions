# a function that will calculate the number of steps that you make for a certain distance

def stepCount():
    distance = float(input("How far did you walk(in meters)?: "))
    step = float(input("How long is your step(in cm.)?: "))
    return distance//step

a = stepCount()
print("You made " + str(int(a)) + " steps during your walk.")