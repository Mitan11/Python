# Check wether the number is prime or not 

n = int(input("Enter a number : "))

count = 0

for i in range(1,n+1):
    if n%i == 0:
        count = count + 1

if count == 2:
    print("your number is prime")
else:
    print("your number is not prime")

