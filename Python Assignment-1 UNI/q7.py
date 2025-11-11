'''7. By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 101st prime number?'''


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def nth_position_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

n = int(input("Enter which prime number you want to find: "))

result = nth_position_prime(n)
print(f"The {n}th prime number is {result}")