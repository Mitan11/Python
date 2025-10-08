def sumOfDigit(number):
    digit = 0
    sum = 0

    while number > 0 :
        digit = number % 10
        print(digit)
        sum = sum + digit
        number = number // 10
    return sum

# Input from user
num = int(input("Enter a number: "))

sum = sumOfDigit(num)

print(f"Sum of digits is {sum}")