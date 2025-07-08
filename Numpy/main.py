# ===============================
# Introduction to NumPy Arrays (Theory and Practice)
# ===============================
#
# What is a NumPy Array?
# ----------------------
# NumPy (Numerical Python) is a fundamental library for scientific computing in Python. Its main feature is the ndarray (n-dimensional array),
# which is a container for large, homogeneous data (all elements of the same type) and supports efficient numerical operations.
#
# Conceptually, a NumPy array is like a multi-dimensional table (vector, matrix, tensor, etc.) of numbers. Unlike Python lists, NumPy arrays store data
# in contiguous memory and are implemented in C for speed and efficiency. This makes operations on large datasets much faster and more memory-efficient
# than using plain Python lists or loops.
#
# Python Lists vs NumPy Arrays
# ---------------------------
# Python lists are flexible containers that can hold heterogeneous data (different types) and resize dynamically.
# In contrast, NumPy arrays require homogeneous types (all elements share the same data type) and have a fixed size once created.
#
# | Feature         | Python List                        | NumPy Array (ndarray)         |
# |-----------------|-----------------------------------|-------------------------------|
# | Data Types      | Heterogeneous (mixed types)        | Homogeneous (one type only)   |
# | Size            | Dynamic (can grow/shrink)          | Fixed (size set at creation)  |
# | Memory Layout   | References to separate objects     | Contiguous block of memory    |
# | Performance     | Slower for math, uses Python loops | Fast, uses compiled C code    |
# | Math Operations | Need loops or list comprehensions  | Vectorized (element-wise)     |
#
# - Python lists are flexible and can hold anything, but are slow for math.
# - NumPy arrays are strict (one type, fixed size), but are extremely fast and powerful for numerical data.
#
# Why use NumPy arrays?
# ---------------------
# - Homogeneous Data: Arrays store elements of one type (e.g. all floats), which simplifies memory layout and speeds up computations.
# - Performance: NumPy arrays leverage optimized C code under the hood. Element-wise operations on large arrays are vectorized (done in compiled loops) instead of Python loops, making them much faster on numeric data.
# - Memory Layout: A Python list actually stores references (pointers) to separate Python objects for each element. In contrast, a NumPy array stores its elements contiguously in memory, like a C array. This contiguous storage improves cache performance.
# - Functionality: Arrays enable powerful operations (matrix math, linear algebra, statistics) that are either impossible or very slow with plain lists.
#
# Creating NumPy Arrays
# ---------------------
# You create an array by calling np.array() with a Python sequence (list or nested lists). NumPy infers the shape and data type from the input.
#
# Example:
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr)          # [1 2 3 4]
# print(arr.dtype)    # int64 (for example)
#
# # Mixed types: all converted to float
# arr2 = np.array([1, 2, 3.5])
# print(arr2)         # [1.  2.  3.5]
# print(arr2.dtype)   # float64
#
# Multi-dimensional arrays (matrices) are created by passing nested lists:
# mat = np.array([[1, 2, 3], [4, 5, 6]])
# print(mat)
# # [[1 2 3]
# #  [4 5 6]]
# print(mat.shape)  # (2, 3) → 2 rows, 3 columns
#
# NumPy also provides functions to generate arrays of specific shapes filled with default values:
# - np.zeros(shape): creates a new array of given shape filled with 0.
# - np.ones(shape): does the same but fills with 1.
# - np.arange(start, stop, step): like Python’s range(), but returns an array.
# - np.linspace(start, stop, num): evenly spaced values between start and stop.
#
# Vectors and Matrices
# --------------------
# In NumPy terms, a vector is simply a 1D array (shape like (N,)) and a matrix is a 2D array (shape (M, N)).
#
# Random Number Generation
# ------------------------
# NumPy has a powerful submodule np.random for generating pseudorandom numbers:
# - np.random.rand(*dims): Uniform random floats in [0, 1)
# - np.random.randn(*dims): Standard normal (mean=0, std=1)
# - np.random.randint(low, high, size): Random integers
# - np.random.choice(a, size, replace, p): Random sample from array/list
#
# Array Attributes
# ----------------
# - .shape: Tuple of dimensions (e.g., (3, 4))
# - .ndim: Number of dimensions (axes)
# - .size: Total number of elements
# - .dtype: Data type of elements
#
# Array Methods
# -------------
# - .sum(axis=None): Sum of elements (optionally along axis)
# - .mean(axis=None): Mean of elements
# - .max(axis=None), .min(axis=None): Max/min
# - .flatten(): 1D copy of array
# - .reshape(newshape): Change shape (must have same number of elements)
# - .T or .transpose(): Transpose (swap rows/columns)
#
# Indexing and Slicing
# --------------------
# - 1D: arr[2:5], arr[::-1] (reverse)
# - 2D: arr[1, 2] (row 1, col 2), arr[:, 1] (all rows, col 1), arr[1:3, 0:2] (submatrix)
# - Boolean: arr[arr > 30] (all elements > 30)
#
# Arithmetic Operations and Broadcasting
# -------------------------------------
# - Element-wise: A + B, A * B, etc. (shapes must match or be broadcastable)
# - Broadcasting: NumPy can “stretch” arrays of size 1 to match the other array’s shape.
# - Matrix multiplication: Use @ or np.dot() for true matrix product.
#
# Deep vs. Shallow Copies
# -----------------------
# - b = a → both refer to the same data (shallow copy)
# - b = a.copy() → new, independent array (deep copy)
#
# Matrix Operations
# -----------------
# - Matrix multiplication: A @ B or np.dot(A, B)
# - Transpose: A.T or np.transpose(A)
#
# Stacking and Splitting Arrays
# -----------------------------
# - Stacking: np.vstack, np.hstack (vertical/horizontal)
# - Splitting: np.vsplit, np.hsplit, np.array_split (for unequal splits)
#
# For more, see: numpy.org, geeksforgeeks.org

# ===============================
# NumPy Beginner's Guide (with Theory, Tips, and Examples)
# ===============================

# --- Introduction ---
print("Welcome to the NumPy Beginner's Guide!")

# What is NumPy?
# NumPy (Numerical Python) is a Python library that makes working with numbers and large sets of data much easier and faster.
# It is especially useful for math, science, engineering, and data analysis.
# Think of NumPy as a supercharged version of Python lists, designed for math!

# Why use NumPy?
# - Speed: NumPy is much faster than regular Python lists for math operations.
# - Functionality: It has many built-in math functions (like sum, mean, reshape, etc.).
# - Memory: It stores data more efficiently, so you can work with bigger datasets.
# - Foundation: Many other libraries (like pandas, scikit-learn, TensorFlow) use NumPy under the hood.

# --- Importing NumPy ---
# To use NumPy, you first need to import it. The standard way is to use the alias 'np'.
import numpy as np  # 'np' is a short name for NumPy, used by everyone

# === Topic: Creating NumPy Arrays ===
# What is a NumPy array?
# A NumPy array is like a grid or table of values, all of the same type (like all numbers or all strings).
# Arrays can be 1D (like a list), 2D (like a table), or even more dimensions.

# np.array(): This function turns a Python list (or other sequence) into a NumPy array.
arr = np.array([1, 2, 3, 4])  # Creates a 1D array from a list of integers
print("1D array:", arr)

# If you give np.array() a list with mixed types (like ints and floats),
# NumPy will convert everything to the most general type (here, float).
a = [1, 2, 3.5]
print("Python list:", a)
print("NumPy array from list:", np.array(a))  # Notice all elements become floats

# --- Theory: Python Lists vs NumPy Arrays ---
# - Python lists can store different types (int, float, str, etc.), but NumPy arrays store only one type.
# - NumPy arrays are much faster for math because they're written in C (a fast language) under the hood.
# - NumPy arrays use less memory for large numbers of elements.
# - NumPy arrays let you do math on whole arrays at once ("vectorized operations"), no need for loops.

# --- 2. Vectors and Matrices ---
# In NumPy:
# - A vector is a 1D array (like a list of numbers)
# - A matrix is a 2D array (like a table with rows and columns)

# Creating a vector (1D array)
# np.array([values]) creates a 1D array (vector)
vector = np.array([1, 2, 3, 4, 5])
print("\nVector:", vector)
print("Shape of vector:", vector.shape)  # .shape tells you the size and dimensions of the array

# Creating a matrix (2D array)
# np.array([[row1], [row2], ...]) creates a 2D array (matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\nMatrix:\n", matrix)
print("Shape of matrix:", matrix.shape)  # (3, 3) means 3 rows, 3 columns

# === Topic: Array Generation Functions ===
# NumPy can create arrays filled with zeros, ones, or sequences of numbers.

# np.zeros(shape): Creates an array filled with zeros. 'shape' can be a single number (for 1D) or a tuple (for 2D or more).
zeros_1d = np.zeros(5)  # 1D array of 5 zeros
print("\n1D array of zeros:", zeros_1d)
zeros_2d = np.zeros((3, 4))  # 2D array: 3 rows, 4 columns
print("2D array of zeros:\n", zeros_2d)

# np.ones(shape): Creates an array filled with ones.
ones_1d = np.ones(7)  # 1D array of 7 ones
print("1D array of ones:", ones_1d)
ones_2d = np.ones((2, 5))  # 2D array: 2 rows, 5 columns
print("2D array of ones:\n", ones_2d)

# np.arange(start, stop, step): Creates an array with a range of numbers (like Python's range, but returns an array).
range_arr = np.arange(10)  # Numbers from 0 to 9
print("Array from arange(10):", range_arr)
range_with_step = np.arange(2, 10, 2)  # Numbers from 2 to 8, step 2
print("Array from arange(2, 10, 2):", range_with_step)

# np.linspace(start, stop, num): Creates an array of evenly spaced values between start and stop.
linspace_arr = np.linspace(0, 1, 5)  # 5 values from 0 to 1 (inclusive)
print("Array from linspace(0, 1, 5):", linspace_arr)
linspace_arr_2 = np.linspace(10, 20, 10)  # 10 values from 10 to 20
print("Array from linspace(10, 20, 10):", linspace_arr_2)

# === Topic: Random Number Generation ===
# NumPy's random module lets you create arrays of random numbers for simulations, testing, and more.

# np.random.rand(): Returns random numbers from 0 to 1 (uniform distribution)
random_num = np.random.rand()  # Single random number
print("\nSingle random number (0-1):", random_num)
random_arr_1d = np.random.rand(5)  # 1D array of 5 random numbers
print("1D array of random numbers:", random_arr_1d)
random_arr_2d = np.random.rand(3, 4)  # 2D array: 3 rows, 4 columns
print("2D array of random numbers:\n", random_arr_2d)

# np.random.randn(): Returns random numbers from a standard normal distribution (mean=0, std=1)
random_normal_num = np.random.randn()  # Single random number
print("Single random number (normal):", random_normal_num)
random_normal_arr_1d = np.random.randn(5)  # 1D array
print("1D array (normal):", random_normal_arr_1d)
random_normal_arr_2d = np.random.randn(3, 4)  # 2D array
print("2D array (normal):\n", random_normal_arr_2d)

# np.random.randint(low, high, size): Returns random integers from low (inclusive) to high (exclusive)
random_int = np.random.randint(10)  # Single random integer from 0 to 9
print("Single random integer (0-9):", random_int)
random_int_arr_1d = np.random.randint(5, 20, 8)  # 1D array of 8 random ints from 5 to 19
print("1D array of random integers (5-19):", random_int_arr_1d)
random_int_arr_2d = np.random.randint(100, 200, size=(4, 5))  # 2D array
print("2D array of random integers (100-199):\n", random_int_arr_2d)

# np.random.choice(): Randomly picks elements from a list or array
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_element = np.random.choice(my_list)  # Single random element
print("Random element from list:", random_element)
random_elements_with_replacement = np.random.choice(my_list, size=5, replace=True)  # Can repeat
print("Random elements with replacement:", random_elements_with_replacement)
random_elements_without_replacement = np.random.choice(my_list, size=5, replace=False)  # No repeats
print("Random elements without replacement:", random_elements_without_replacement)
elements = ['A', 'B', 'C', 'D']
probabilities = [0.1, 0.2, 0.3, 0.4]  # Probabilities must add up to 1
random_element_with_prob = np.random.choice(elements, p=probabilities)
print("Random element with probabilities:", random_element_with_prob)

# np.random.seed(): Sets the random seed for reproducibility (so you get the same random numbers every time)
np.random.seed(42)
print("\nRandom numbers with seed 42:", np.random.rand(5))
np.random.seed(42)
print("Random numbers with seed 42 (again):", np.random.rand(5))
np.random.seed(123)
print("Random numbers with seed 123:", np.random.rand(5))

# === Topic: Array Attributes ===
# NumPy arrays have special properties (attributes) that tell you about their structure:
# - .shape: The size of each dimension (e.g., (3, 4) means 3 rows, 4 columns)
# - .ndim: The number of dimensions (1D, 2D, etc.)
# - .size: The total number of elements
# - .dtype: The data type of the elements (int, float, etc.)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray:", arr_2d)
print("Shape:", arr_2d.shape)  # (2, 3)
print("Dimensions (ndim):", arr_2d.ndim)  # 2
print("Total elements (size):", arr_2d.size)  # 6
print("Data type (dtype):", arr_2d.dtype)  # int64 (or int32)

# === Topic: Array Methods ===
# NumPy arrays have built-in methods (functions you call with a dot) for common math operations:
# - .sum(): Adds up all elements
# - .mean(): Calculates the average
# - .max(): Finds the largest value
# - .min(): Finds the smallest value
# - .flatten(): Turns any array into a 1D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("\nSum of all elements:", arr.sum())
print("Sum along columns (axis=0):", arr.sum(axis=0))  # Adds down each column
print("Sum along rows (axis=1):", arr.sum(axis=1))    # Adds across each row
print("Mean:", arr.mean())
print("Max:", arr.max())
print("Min:", arr.min())
print("Flattened:", arr.flatten())

# .reshape(new_shape): Changes the shape of the array (must have the same number of elements)
arr = np.arange(12)  # 1D array with 12 elements
print("\nOriginal array:", arr)
print("Reshaped to 3x4:\n", arr.reshape(3, 4))  # 3 rows, 4 columns
print("Reshaped to 2x6:\n", arr.reshape(2, 6))  # 2 rows, 6 columns
print("Reshaped to 4x3 (using -1):\n", arr.reshape(4, -1))  # -1 lets NumPy figure out the right size

# np.resize(array, new_shape): Changes the size of the array, repeating elements if needed
arr = np.array([1, 2, 3, 4, 5, 6])
print("\nOriginal array:", arr)
print("Resized to 8 elements:", np.resize(arr, (8,)))  # Repeats elements
print("Resized to 4 elements:", np.resize(arr, (4,)))  # Truncates
print("Resized to 3x3:\n", np.resize(arr, (3, 3)))

# === Topic: Indexing and Slicing ===
# Indexing: Getting a single element from an array
# Slicing: Getting a part (sub-array) of an array

# 1D Indexing
vector = np.array([10, 20, 30, 40, 50])
print("\nVector:", vector)
print("Element at index 0:", vector[0])  # First element
print("Element at index 3:", vector[3])  # Fourth element
print("Last element:", vector[-1])      # Last element
print("Second to last element:", vector[-2])  # Second last

# 1D Slicing: [start:stop:step]
vector = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\nSlice from index 2 to 5:", vector[2:5])  # 2, 3, 4
print("Slice from beginning to index 4:", vector[:4])  # 0, 1, 2, 3
print("Slice from index 6 to the end:", vector[6:])    # 6, 7, 8, 9
print("Slice with step of 2:", vector[::2])            # Every second element
print("Slice from 1 to 8 with step 3:", vector[1:8:3]) # 1, 4, 7
print("Reversed vector:", vector[::-1])               # All elements, reversed

# 2D Indexing and Slicing
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])
print("\nMatrix:\n", matrix)
print("Element at row 0, col 1:", matrix[0, 1])  # 20
print("Element at row 2, col 2:", matrix[2, 2])  # 90
print("Element at last row, last col:", matrix[-1, -1])  # 90

# 2D Slicing: [row_slice, col_slice]
matrix = np.array([[ 0,  1,  2,  3],
                   [10, 11, 12, 13],
                   [20, 21, 22, 23],
                   [30, 31, 32, 33]])
print("\nFirst row:", matrix[0, :])  # All columns of first row
print("Second column:", matrix[:, 1])  # All rows of second column
print("Sub-matrix (rows 1-2, cols 0-1):\n", matrix[1:3, 0:2])
print("Every second row:\n", matrix[::2, :])
print("Every second column:\n", matrix[:, ::2])
print("Sub-matrix with steps:\n", matrix[0:3:2, 1:4:2])

# Boolean Indexing: Use a boolean array to select elements
arr = np.array([10, 20, 30, 40, 50])
boolean_index = np.array([True, False, True, False, True])
print("\nElements selected by boolean index:", arr[boolean_index])  # 10, 30, 50
print("Elements greater than 30:", arr[arr > 30])  # 40, 50

# === Topic: Arithmetic Operations ===
# You can do math directly on arrays (element-wise operations)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("\nArray 1:\n", arr1)
print("Array 2:\n", arr2)
print("Element-wise addition:\n", arr1 + arr2)  # Adds each element
print("Element-wise subtraction:\n", arr1 - arr2)
print("Element-wise multiplication:\n", arr1 * arr2)
print("Element-wise division:\n", arr1 / arr2.astype(float))  # Use float to avoid integer division
print("Element-wise exponentiation:\n", arr1 ** arr2)  # arr1 to the power of arr2

# === Topic: Broadcasting ===
# Broadcasting: NumPy can automatically expand arrays of different shapes to work together, if their shapes are compatible.
# Example: Adding a number to every element of a matrix
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMatrix:\n", matrix)
print("Matrix + 10 (broadcasting):\n", matrix + 10)  # Adds 10 to every element
# Example: incompatible shapes
vector_incompatible = np.array([100, 200])
try:
    print(matrix + vector_incompatible)
except ValueError as e:
    print("Error with incompatible shapes:", e)

# === Topic: Deep vs Shallow Copy ===
# Shallow copy: Just another name for the same array (changes affect both)
# Deep copy: A true copy of the data (changes do NOT affect the original)
original_array = np.array([1, 2, 3, 4, 5])
shallow_copy = original_array  # Just a reference
shallow_copy[0] = 99  # Changes original_array too!
print("\nOriginal after shallow copy change:", original_array)
deep_copy = original_array.copy()  # True copy
# Now, changing deep_copy does NOT affect original_array
deep_copy[0] = 100
print("Deep copy after change:", deep_copy)
print("Original after deep copy change:", original_array)

# === Topic: Matrix Operations ===
# Matrix multiplication: Combines two matrices in a special way (not element-wise)
# Use @ or np.dot()
matrix_a = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
matrix_b = np.array([[7, 8], [9, 10], [11, 12]])  # 3x2
print("\nMatrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("Matrix A @ Matrix B:\n", matrix_a @ matrix_b)  # Preferred for matrix multiplication
print("Matrix A . Matrix B (np.dot):\n", np.dot(matrix_a, matrix_b))
# Transpose: Flips rows and columns
matrix_c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("\nMatrix C:\n", matrix_c)
print("Transpose of Matrix C (using .T):\n", matrix_c.T)
print("Transpose of Matrix C (using np.transpose()):\n", np.transpose(matrix_c))

# === Topic: Stacking and Splitting Arrays ===
# Stacking: Combine arrays together
# np.vstack(): Stack vertically (row-wise)
# np.hstack(): Stack horizontally (column-wise)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("\nVertically stacked array:\n", np.vstack((arr1, arr2)))
arr3 = np.array([[1], [2]])
arr4 = np.array([[3], [4]])
print("Horizontally stacked array:\n", np.hstack((arr3, arr4)))
arr5 = np.arange(6).reshape(2, 3)
arr6 = np.arange(6, 12).reshape(2, 3)
print("Vertically stacked 2D arrays:\n", np.vstack((arr5, arr6)))
print("Horizontally stacked 2D arrays:\n", np.hstack((arr5, arr6)))

# Splitting: Divide an array into parts
# np.hsplit(): Split horizontally (columns)
# np.vsplit(): Split vertically (rows)
# np.array_split(): Split into unequal parts
arr = np.arange(16).reshape(4, 4)
print("\nOriginal array:\n", arr)
print("Horizontally split into 2 parts:", np.hsplit(arr, 2))
print("Horizontally split at indices [1, 3]:", np.hsplit(arr, [1, 3]))
print("Vertically split into 4 parts:", np.vsplit(arr, 4))
print("Vertically split at indices [1, 3]:", np.vsplit(arr, [1, 3]))
arr_unequal = np.arange(10)
print("Unequally split into 3 parts:", np.array_split(arr_unequal, 3))

# === Topic: Practical Tips and Common Pitfalls ===
# - Always check array shapes before operations (use .shape)
# - Use .copy() for deep copies, not =
# - Broadcasting only works if dimensions are compatible
# - Use np.arange for integer steps, np.linspace for evenly spaced floats
# - Use np.random.seed for reproducible results
# - NumPy arrays are fixed-size; to "resize", create a new array

# === Topic: When NOT to Use NumPy ===
# - For small lists or non-numeric data, plain Python lists are fine
# - For text, objects, or mixed types, use lists or pandas
# - For very large datasets, consider pandas or Dask for out-of-core computation

# === Topic: NumPy Cheat Sheet ===
print("\nNumPy Cheat Sheet:")
print("np.array([1,2,3])  # Create array")
print("np.zeros((2,3))    # 2x3 array of zeros")
print("np.ones(5)         # 1D array of ones")
print("np.arange(0,10,2)  # [0 2 4 6 8]")
print("np.linspace(0,1,5) # 5 evenly spaced values 0-1")
print("arr.shape          # Array shape")
print("arr.ndim           # Number of dimensions")
print("arr.size           # Number of elements")
print("arr.dtype          # Data type")
print("arr.sum(), arr.mean(), arr.max(), arr.min()")
print("arr.reshape(2,3)   # Change shape")
print("arr.flatten()      # 1D copy")
print("arr.T              # Transpose")
print("np.vstack([a,b])   # Stack vertically")
print("np.hstack([a,b])   # Stack horizontally")
print("np.hsplit(arr,2)   # Split columns")
print("np.vsplit(arr,2)   # Split rows")
print("np.random.rand(3)  # 3 random floats")
print("np.random.randint(0,10,5) # 5 random ints 0-9")

# === Topic: Try It Yourself! ===
# 1. Create a 2D array of shape (3, 4) filled with random integers from 0 to 9
# 2. Find the mean of each row
# 3. Reshape it to (4, 3)
# 4. Stack it with another array of the same shape
# 5. Split the stacked array into two

# --- End of Guide ---
print("\nCongratulations! You've completed the NumPy Beginner's Guide. Happy coding!")
