# 9. Read a number from the user and output its reverse.


def reverse_number(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum * 10 + digit
        num //= 10
    return sum


number = int(input("Enter a number: "))
result = reverse_number(number)
print(f"The reverse of the number is {result}")