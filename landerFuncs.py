#landerFuncs.py

def showWelcome():
	print ("Welcome to the moonlander module")
	

def getFuel():
	fuelAmount = int(input("How much fuel do you have (in liters)? "))
	while fuelAmount < 0:
		print ("Fuel level must be positive.")
		fuelAmount = int(input("How much fuel do you have? "))
	return fuelAmount

def getAltitude():
	altitude = int(input("What is the altitude? "))
	while altitude <=1 or altitude >=9999:
		print ("Error: Altitude must be between 1 and 9999.")
		altitude = float(input("What is the altitude? "))

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
	elpastedTime = int(elapsedTime)
	altitude = float(altitude)
	velocity = float(velocity)
	fuelAmount = int(fuelAmount)
	fuelRate = int(fuelRate)
	print ("The elasped time is "+ str(elapsedTime) + " mins") 
	print ("The altitude is " + str(altitude) + " m")
	print ("The velocity is "+str(velocity)+" m/s")
	print ("The fuelAmount "+str(fuelAmount)+" L")
	print ("Fuel rate is "+str(fuelRate)+" L/s")

def getFuelRate(currentFuel):
	currentFuel01 = int(input("Enter an int value between 0 and 9 to represent fuel level "))
	while currentFuel01 >9 or currentFuel <0:
		print("Error: you must input a value between 0 and 9 (inclusive)")
		currentFuel01 = int(input("Enter an int value between 0 and 9 to represent fuel level "))
	return min(currentFuel, currentFuel01)

def displayLMLandingStatus(velocity):
	if velocity <= 0 and velocity >= -1:
		print ("Status at landing - The eagle has landed!\n")
	elif velocity < -1 and velocity > -10:
		print ("Status at landing - Enjoy your oxygen while it lasts!\n")
	else: 
		print ("Status at landing - Ouch - that hurt!\n")

def updateAcceleration(fuelRate):
	acceleration = 1.62*((fuelRate/5)-1)
	return acceleration

def updateAltitude(altitude, velocity, acceleration):
	altitude0 = float (altitude)
	velocity0 = float (velocity)
	acceleration = float (acceleration)
	altitude1 = altitude0 + velocity0 + (acceleration/2)
	return altitude1

def updateVelocity(velocty, acceleration):
	velocty0 = float(velocity)
	velocity01 = velocity0 + acceleration
	return velocity01

def updateFuel(fuel, fuelRate):
	fuel0 = int (fuel)
	fuel1 = fuel0 - fuelRate
	return fuel1

