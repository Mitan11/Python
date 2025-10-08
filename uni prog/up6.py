# Q1
start = int(input("Start number: "))
end = int(input("End number: "))

even_count = 0
odd_count = 0

print("Even\tOdd")

for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end='\t')  # print even number with tab
        even_count += 1
    else:
        print(i)  # print odd number and move to new line
        odd_count += 1

print(f"Total even numbers are {even_count}")
print(f"Total odd numbers are {odd_count}")

# Q2
num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# Q3
start = int(input("Start number: "))
end = int(input("End number: "))

for i in range(start, end):
    if (i % 3 == 0) or (i % 6 == 0):
        continue
    print(i)



# Q4
start = int(input("Start number: "))
end = int(input("End number: "))

for i in range(start, end):
    if (i % 7 == 0) and (i % 5 == 0):
        print(i)


# Q5 - Guess the Number Game

import random as r

while True:
    random_num = r.randint(1, 10)
    guess = int(input("Guess the number between 1 to 10: "))
    
    if guess == random_num:
        print("Correct !!!!")
        break
    else:
        print("Try Again")

