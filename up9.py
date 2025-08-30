def countDigit(number):
    digit = 0
    while number > 0 :
        digit += 1
        number = number // 10
    return digit

# Input from user
num = int(input("Enter a number: "))

digit = countDigit(num)
print(f"Number of digits in {num} is {digit}")