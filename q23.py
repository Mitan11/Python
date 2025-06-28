# Accept a number and print its reverse

num = 12345

while num > 0:
    digit = num % 10
    print(digit, end="")
    num = num // 10