# Print the sum of all even & odd numbers in a range separately

even = 0
odd = 0

n = int(input("Enter a number : "))

for i in range(n+1):
    if(i%2 == 0):
        even+=i
    else:
        odd+=i
print(f"even {even} and odd {odd}")