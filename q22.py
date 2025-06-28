#  Separate each digit of a number and print it on the new line

num = 12345

while num > 0:
    digit = num % 10
    print(digit)
    num = num // 10
    