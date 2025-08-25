# Function to calculate cube of a digit
def cube(digit):
    return digit * digit * digit

# Function to calculate remainder
def mode(divisor, dividend):
    return dividend % divisor

# Function to check if a number is Armstrong
def isArmstrong(num):
    sum = 0
    temp = num

    while num > 0:
        digit = mode(10, num)
        sum = sum + cube(digit)
        num = num // 10
    
    return temp == sum

# Input from user
num = int(input("Enter a number: "))

# Check and display result
if isArmstrong(num):
    print("Armstrong")
else:
    print("Not Armstrong")
