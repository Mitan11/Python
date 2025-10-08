# list 
my_list = [5, 2, 9, 1, 5, 6] 

# 🔁 List Traversing (Looping)
# A. Using index:
for i in range(len(my_list)):
    print(my_list[i])

# B. Directly:
for num in my_list:
    print(num)


print("Original List:", my_list)

# 🔹 List Indexing & Slicing (Same as Strings)
print(my_list[0])    # Access by index
print(my_list[-1])   # Negative indexing
print(my_list[1:4])  # Slicing from index 1 to 3
print(my_list[:3])   # Slicing from start to index 2
print(my_list[3:])   # Slicing from index 3 to end
print(my_list[:])    # Full list
print(my_list[::2])  # Slicing with step
print(my_list[::-1]) # Reversing the list
print()

# 🛠️ Common List Methods
numbers = [5, 2, 9, 1, 5, 6]  # Initial list

print("Initial List:", numbers)

numbers.append(10)             # Adds 10 to the end
numbers.insert(2, 15)          # Inserts 15 at index 2
numbers.extend([20, 25, 30])   # Adds multiple elements at the end
numbers.remove(5)              # Removes first occurrence of 5
popped_item = numbers.pop(3)   # Removes and returns element at index 3
index = numbers.index(6)       # Finds index of value 6
count_5 = numbers.count(5)     # Counts how many times 5 appears
numbers.sort()                 # Sorts the list in ascending order
numbers.reverse()              # Reverses the order of the list
new_numbers = numbers.copy()   # Makes a copy of the list
numbers.clear()                # Removes all elements
print("Modified List:", numbers)
print("Popped Item:", popped_item)
print("Index of 6:", index)
print("Count of 5:", count_5)
print("Copied List:", new_numbers)
print()