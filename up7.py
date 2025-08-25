# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Input from user
num = int(input("Enter a number: "))

# Check and display result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Function to count factors of a number
def count_factors(num):
    total_factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            total_factors += 1
    return total_factors

# Function to check if a number is prime
def is_prime(num):
    return count_factors(num) == 2

# Input from user
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")


# # Function to check if a number is prime in range
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
