# Write a program to accept a range of numbers from the user and display all even and odd numbers in that range in a tabular format. Also, count the total number of even and odd numbers and display them. 

# start = int(input("Start number: "))
# end = int(input("End number: "))

# even_count = 0
# odd_count = 0

# print("Odd\tEven")

# for i in range(start, end + 1):
#     if i % 2 != 0:
#         print(i, end='\t')  # print odd number with tab
#         odd_count += 1
#     else:
#         print(i)  # print even number and move to new line
#         even_count += 1

# print(f"\nTotal odd numbers are {odd_count}")
# print(f"Total even numbers are {even_count}")

# Write a program to accept a number from the user and display its multiplication table using loops.

# num = int(input("Enter number: "))

# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")

# Write a program to accept a range of numbers from the user and display the multiplication table of each number in that range using functions.

# def multiplication_table(num):
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")
#     print()

# def multiplication_table_range(start, end):
#     for number in range(start, end + 1):
#         multiplication_table(number)


# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))

# multiplication_table_range(start, end)

# Write a program to accept a range of numbers from the user and display all numbers in that range except those which are divisible by 3 and 6 using continue statement.

# start = int(input("Start number: "))
# end = int(input("End number: "))

# for i in range(start, end):
#     if (i % 3 == 0) or (i % 6 == 0):
#         continue
#     print(i)

# Write a program to accept a range of numbers from the user and display all numbers in that range which are divisible by both 5 and 7 using the modulus operator.

# start = int(input("Start number: "))
# end = int(input("End number: "))

# for i in range(start, end):
#     if (i % 7 == 0) and (i % 5 == 0):
#         print(i)

# Guess the Number Game 

# import random as r

# while True:
#     random_num = r.randint(1, 10)
#     guess = int(input("Guess the number between 1 to 10: "))

#     if guess == random_num:
#         print("Correct !!!!")
#         break
#     else:
#         print("Try Again")

# write a program to accept a number from the user and check whether it is a prime number or not using functions.

# Function to check if a number is prime
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, number ):
#         if number % i == 0:
#             return False
#     return True

# # Input from user
# num = int(input("Enter a number: "))

# # Check and display result
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# Write a program to accept a range of numbers from the user and display all prime numbers in that range using functions.

# Function to check if a number is prime
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True

# # Input range from user
# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))

# print(f"Prime numbers between {start} and {end} are:")

# for num in range(start, end + 1):
#     if is_prime(num):
#         print(num, end=" ")

# Write a program to accept a number from the user and check whether it is a prime number or not using functions.

# Function to count factors of a number
# def count_factors(num):
#     total_factors = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             total_factors += 1
#     return total_factors

# # Function to check if a number is prime
# def is_prime(num):
#     return count_factors(num) == 2

# # Input from user
# num = int(input("Enter a number: "))
# if is_prime(num):
#     print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")

# Write a program to accept a number from the user and check whether it is an Armstrong number or not using functions.

# Function to calculate cube of a digit
# def cube(digit):
#     return digit * digit * digit

# # Function to calculate remainder
# def mode(divisor, dividend):
#     return dividend % divisor

# # Function to check if a number is Armstrong
# def isArmstrong(num):
#     sum = 0
#     temp = num

#     while num > 0:
#         digit = mode(10, num) # num % 10
#         sum = sum + cube(digit) # sum += digit ** 3
#         num = num // 10 # num = num // 10

#     return temp == sum

# # Input from user
# num = int(input("Enter a number: "))

# # Check and display result
# if isArmstrong(num):
#     print("Armstrong")
# else:
#     print("Not Armstrong")

# Write a program to accept a number from the user and count the number of digits in that number using functions.

# def countDigit(number):
#     digit = 0
#     while number > 0 :
#         digit += 1
#         number = number // 10
#     return digit

# # Input from user
# num = int(input("Enter a number: "))

# digit = countDigit(num)
# print(f"Number of digits in {num} is {digit}")

# Write a program to accept a number from the user and calculate the sum of its digits using functions.

# def sumOfDigit(number):
#     digit = 0
#     sum = 0

#     while number > 0 :
#         digit = number % 10
#         sum = sum + digit
#         number = number // 10
#     return sum

# # Input from user
# num = int(input("Enter a number: "))

# sum = sumOfDigit(num)

# print(f"Sum of digits is {sum}")

# Write a program to accept a number from the user and reverse that number using functions.

# def reverseNumber(number):
#     digit = 0
#     sum = 0

#     while number > 0 :
#         digit = number % 10
#         sum = sum * 10 + digit
#         number = number // 10
#     return sum

# # Input from user
# num = int(input("Enter a number: "))

# reversed = reverseNumber(num)

# print(f"Reverse number is {reversed}")

# Write a program to accept a number from the user and check whether it is a palindrome or not using functions.

# def reverseNumber(number):
#     digit = 0
#     sum = 0

#     while number > 0 :
#         digit = number % 10
#         sum = sum * 10 + digit
#         number = number // 10
#     return sum

# # Input from user
# num = int(input("Enter a number: "))

# reversed = reverseNumber(num)

# if (reversed == num):
#     print("Number is Palindrome")
# else :
#     print("Number is not Palindrome")

# Write a program to accept a number from the user and check whether it is a perfect number or not using functions.

# def isPerfectNumber(number):
#     digit = 0
#     sum = 0
#     mul = 1
#     while number > 0 :
#         digit = number % 10
#         sum = sum + digit
#         mul = mul * digit
#         number = number // 10
#     return sum == mul

# # Input from user
# num = int(input("Enter a number: "))

# prefect = isPerfectNumber(num)

# if (prefect):
#     print("Number is Perfect")
# else :
#     print("Number is not Perfect")


