# 3. The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 6000?

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_factor(num, factor):
    return num % factor == 0

def prime_factors(n):
    for i in range(1,n+1):
        if is_factor(n, i) and is_prime(i):
            print(i, end=' ')

n = int(input("Enter a number to find its prime factors: "))
prime_factors(n)

