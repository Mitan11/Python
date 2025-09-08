# 8. Take a number as input from the user and display the sum of its digits.

def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total


number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits is {result}")