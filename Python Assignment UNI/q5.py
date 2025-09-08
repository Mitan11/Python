'''5. The sum of the squares of the first ten natural numbers is,
1 + 2 + ... + 10 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10) = 55 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.'''


def first_n_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum

def square_of_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum * sum

def difference(n):
    diff = square_of_sum(n) - first_n_squares(n)
    return diff

n = int(input("Enter a number: "))
result = difference(n)
print(f"The difference is {result}")