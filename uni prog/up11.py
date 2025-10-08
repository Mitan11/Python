def reverseNumber(number):
    digit = 0
    sum = 0

    while number > 0 :
        digit = number % 10
        sum = sum * 10 + digit
        number = number // 10
    return sum

# Input from user
num = int(input("Enter a number: "))

reversed = reverseNumber(num)

print(f"Reverse number is {reversed}")


if (reversed == num):
    print("Number is Palindrome")
else :
    print("Number is not Palindrome")