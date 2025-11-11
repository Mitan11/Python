'''6. 2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder. What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?'''
# num = 1
# while True:
#         for i in range(2, 10):
#             if num % i != 0:
#                 # print(num)
#                 break
#             else:    
#                 print(num)
#                 exit()
#         num += 1



def is_divisible_by_all(num, limit):
    for i in range(2, limit + 1):
        if num % i != 0:
            return False
    return True

num = 1
while True:
    if is_divisible_by_all(num, 10):
        print(num)
        break
    num += 1
