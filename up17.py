# 🛠️ Dictionary Syntax
student = {
    "name": "Akarsh",
    "age": 21,
    "marks": [85, 90, 95],
    "details": {"city": "Delhi", "college": "IIT"}
}

print(student)

# Traversing by keys (default)
for i in student:
   print(i)                # key
   print(student[i])  # value

print()

# Traversing by values
for value in student.values():
   print(value)

print()

# Traversing by keys & values
for key , value in student.items():
   print(key)    # key
   print(value)  # value
   # print(value[0])  # if value is a list, print 1st element
   # print(value[1])  # if value is a list, print 2nd element

# write a python program to check if a given key exists in a dictionary or not
# def check_key_exists(dic, key):
#     if key in dic:
#         return True
#     else:
#         return False
    
# key = input("Enter key to search: ")
# if check_key_exists(student, key):
#     print(f"Key '{key}' exists in the dictionary.") 
# else:
#     print(f"Key '{key}' does not exist in the dictionary.")

# Write a Python program to sum all the values in a dictionary?
# def sum_dict_values(d):
#     total = 0
#     for value in d.values():
#         if isinstance(value, (int, float)):  # Check if value is int or float
#             total += value
#         else:
#             print(f"Warning: Non-numeric value '{value}' ignored in summation.")
#     return total

dic = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50,
    "f": "60",
}

# print("Sum of dictionary values:", sum_dict_values(dic))

# write a python program to remove a key from a dictionary which is given by the user

# def remove_key(dic, key):
#     if key in dic:
#         del dic[key]
#         # or
#         # dic.pop(key)
#         return True
#     else:
#         return False
    
# key = input("Enter key to remove: ")
# if remove_key(student, key):
#     print(f"Key '{key}' removed from the dictionary.")
#     print("Updated Dictionary:", student)
# else:
#     print(f"Key '{key}' does not exist in the dictionary.")

# write a python program to print the highest value in the dictionary

def highest_value(dic):
    max_value = None
    for value in dic.values():
        if isinstance(value, (int, float)):  # only numbers
            if max_value == None or value > max_value:
                max_value = value
    return max_value 

print("Highest value in the dictionary:", highest_value(dic))

# write a python program to print key value and count of a dictionary
def print_key_value_count(dic):
    for key, value in dic.items():
        print(f"Key: {key}, Value: {value}, Count: {len(str(value))}")

print_key_value_count(dic)

# write a program to print dictionary in table format


# write a program to print marksheet with total and percentage from a dictionary
marks = {
    "Math": 85,
    "Science": 90,
    "English": 78,
    "History": 88,
    "Geography": 92
}

def print_marksheet(marks):
    total = 0
    for subject, score in marks.items():
        total += score
    percentage = (total / (len(marks) * 100)) * 100  # assuming each subject is out of 100
    return total, percentage
total, percentage = print_marksheet(marks)
print("Total Marks:", total)
print("Percentage: {:.2f}%".format(percentage))