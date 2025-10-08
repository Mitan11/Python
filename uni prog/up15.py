# Accept a list of integers from the user.

# my_list = list(map(int, input("Enter integers separated by spaces: ").split()))

my_list = [12, 11 , 25, 12, 36, 11, 47, 25 ,12, 58, 36]

print("Original List:", my_list)

# remove duplicates while preserving order
def remove_duplicates(lst):
    result = []
    for item in lst:    
        if item not in result:
            result.append(item)
    return result

my_list = remove_duplicates(my_list)
print("List after removing duplicates:", my_list)

# rearrange the the list such that all prime number appear first in ascending order non-prime numbers 
# followed by non-prime numbers in descending order
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

my_list.sort()  # Sort the list in ascending order

for i in my_list:
    if is_prime(i):
        print(i, end=" ")

for i in reversed(my_list):
    if not is_prime(i):
        print(i, end=" ")