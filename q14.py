# Factorial of a number

fact = 1

n = int(input("Enter a number : "))

for i in range(1 , n+1):
    fact *= i

print(fact)