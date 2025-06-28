# Accept a number and check if it a perfect number or not.

n = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, n):
    if n % i == 0:
        sum_of_divisors += i

if sum_of_divisors == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")

"""
Initialization:

n = 6
sum_of_divisors = 0
First iteration (i = 1):

Check if 6 % 1 == 0 → Yes, so 1 is a divisor of 6.
Update sum_of_divisors:
sum_of_divisors = 0 + 1 = 1
Second iteration (i = 2):

Check if 6 % 2 == 0 → Yes, so 2 is a divisor of 6.
Update sum_of_divisors:
sum_of_divisors = 1 + 2 = 3
Third iteration (i = 3):

Check if 6 % 3 == 0 → Yes, so 3 is a divisor of 6.
Update sum_of_divisors:
sum_of_divisors = 3 + 3 = 6
Fourth iteration (i = 4):

Check if 6 % 4 == 0 → No, so we skip.
Fifth iteration (i = 5):

Check if 6 % 5 == 0 → No, so we skip.
End of the loop:

The loop ends because we reach i = 6 and the range is 1 to n-1.
Check if sum of divisors equals n:

sum_of_divisors = 6 and n = 6.
Since sum_of_divisors == n, the number is a perfect number.
Output:

The program will print:
6 is a perfect number.
"""