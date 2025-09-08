'''
1. If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
'''
def sum_of_multiples(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

n = int(input("Enter the limit: "))
result = sum_of_multiples(n)

print(f"Sum of multiples of 3 or 5 below {n} is {result}")