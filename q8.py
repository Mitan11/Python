temperature = int(input("Enter a temperature in celsius : "))

if(temperature < 0):
    print("Freezing Cold")

elif(temperature >= 0 and temperature < 10):
    print("Very Cold")

elif(temperature >= 10 and temperature < 20):
    print("Cold")

elif(temperature >= 20 and temperature < 30):
    print("Pleasant")

elif(temperature >= 30 and temperature < 40):
    print("Hot")

elif(temperature >= 40 ):
    print("Very Hot")