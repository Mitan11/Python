'''2. Accept two numbers from user and print all prime numbers between two
numbers.'''

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primes_between(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
primes_between(start, end)