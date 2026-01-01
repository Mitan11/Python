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

# Q11. Create a numpy array of even numbers from 10 to 20.
even_number = np.arange(2 , 21 , 2)
print(even_number)

# Q12. Create a numpy array of 5 equally spaced numbers between 0 and 1
even_space_numbers = np.linspace(0 , 1 , 5)
even_space_numbers

# Q13. Create a 3*3 numpy array filled with the value 7
arr_7 = np.full((3,3),7)
arr_7

# Q14 Create a 4*4 identity matrix using numpy
identity_matrix = np.eye(4)
print(identity_matrix)

# Q15. Create a numpy array of 10 random floating-point numbers between 0 and 1
random_floats = np.random.rand(10)
print(random_floats)

# Q16. Reashape a 1D array of numbers from 1 to 12 into a 3*4 matrix
array_1_to_12 = np.arange(1, 13)
reshaped_matrix = array_1_to_12.reshape(3, 4)
print(reshaped_matrix)

# Q17. Find the shape and dimension of the array created in Question 16
print("Shape:", reshaped_matrix.shape)
print("Dimension:", reshaped_matrix.ndim)

# Q18. Create a numpy array of integers from 1 to 25 and reshape it into a 5*5 matrix
array_1_to_25 = np.arange(1, 26)
print(array_1_to_25.reshape(5, 5))

# Q19. Extract the first row from the array created in Question 18
first_row = array_1_to_25.reshape(5, 5)[0]
print(first_row)

# Q20. Extract the last column from the array created in Question 18
last_column = array_1_to_25.reshape(5, 5)[: , -1]
print(last_column)

# Q21. Replace all values greater than 15 in the array created in question 18 with 0
array_1_to_25_reshaped = array_1_to_25.reshape(5, 5)
array_1_to_25_reshaped[array_1_to_25_reshaped > 15] = 0
print(array_1_to_25_reshaped)