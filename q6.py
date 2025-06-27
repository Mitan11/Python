# Accept name and age from the user. Check if the user is a valid voter or not.

name = input("Enter your name : ")
age = int(input("Enter your age : "))

if(name and age >= 18):
    print("Your are valid voter")
else:
    print("You are not valid voter")