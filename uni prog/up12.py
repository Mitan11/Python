def isPerfectNumber(number):
    digit = 0
    sum = 0
    mul = 1
    while number > 0 :
        digit = number % 10
        sum = sum + digit
        mul = mul * digit
        number = number // 10
    return sum == mul

# Input from user
num = int(input("Enter a number: "))

prefect = isPerfectNumber(num)

if (prefect):
    print("Number is Perfect")
else :
    print("Number is not Perfect")