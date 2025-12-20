import string
import numpy as np  # Import NumPy library
print("Imported NumPy successfully.\n")

# Q1. Create the same NumPy array using a Python range and a list.

# Using range
arr_range = np.array(range(5))
print(arr_range)

# Using list
arr_list = np.array([0, 1, 2, 3, 4])
print(arr_list)

# Q2. Using a NumPy function, create a 1D NumPy array from 10 to 100 counting by 10

arr_10_to_100 = np.arange(10, 101, 10)
print(arr_10_to_100)

# Q3. Create a NumPy array of capital letters A–Z (np.array(list(ascii_uppercase)))

arr_A_Z = np.array(list(string.ascii_uppercase))
print(arr_A_Z)

# Q4. Create a ten-element NumPy array of all zeros

arr_zeros = np.zeros(10)
print(arr_zeros)

# Q5. Create a ten-element NumPy array of all ones

arr_ones = np.ones(10)
print(arr_ones)

# Q6. Find the data type of the array created in Question 3
print(arr_A_Z.dtype)  # Should print 'U1' for Unicode string of length 1

# Q7. Create a ten-element NumPy array of random integers between 1 and 5 (inclusive) #inclusive meaning both 1 and 5 are included

arr_random_ints = np.random.randint(1, 6, size=10)  # 6 is exclusive
print(arr_random_ints)

# Q8. Create a 1D array of numbers from 0 to 9

arr_0_to_9 = np.arange(10)
print(arr_0_to_9)

# Q9. Extract all odd numbers from the array (arr_0_to_9[arr_0_to_9 % 2 == 1])
odd_numbers = arr_0_to_9[arr_0_to_9 % 2 == 1]
print(odd_numbers)

# Q10. Replace all odd numbers in the array with -1
arr_0_to_9[arr_0_to_9 % 2 == 1] = -1
print(arr_0_to_9)
