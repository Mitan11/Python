# Accept a number and check if it is a pallindromic number

num = 12345
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Number is Pallindromic")
else:
    print("Number is not Pallindromic")