import numpy as np  # Import NumPy library
print("Imported NumPy successfully!")

# Creating a one-dimensional NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])
print("1D Array from list:", arr)

# Creating arrays with specific data types
int_array = np.array([1, 2, 3, 4, 5], dtype=np.int32)  # Explicit dtype for predictable memory usage
float_array = np.array([1.5, 2.7, 3.9, 4.2], dtype=np.float64)  # Floating-point precision example
print("Integer array:", int_array)
print("Float array:", float_array)

# Creating a two-dimensional NumPy array (matrix)
mul_dim = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array (matrix) with 2 rows and 3 columns
print("\n2D Array (matrix):\n", mul_dim)

# ===== ARRAY PROPERTIES =====
# Inspect ndim, shape, size, dtype, and memory footprint to understand layout and storage.
# Print the number of dimensions of the arrays
print("Dimension of arr:", arr.ndim)
print("Dimension of mul_dim:", mul_dim.ndim)

# Print the shape of the arrays (rows, columns)
print("Shape of arr:", arr.shape)
print("Shape of mul_dim:", mul_dim.shape)

# Print the size (total number of elements) of the arrays
print("Size of arr:", arr.size)
print("Size of mul_dim:", mul_dim.size)

# Print the data type of the elements
print("Datatype of arr:", arr.dtype)
print("Datatype of float_array:", float_array.dtype)

# Print memory usage information
print("Item size of arr (bytes):", arr.itemsize)
print("Total bytes of arr:", arr.nbytes)

# ===== ARRAY INDEXING AND SLICING =====
# 1D slices return views; 2D slices use [row, col] to access elements or ranges.
print("\n" + "=" * 50)
print("ARRAY INDEXING AND SLICING")
print("=" * 50)

# Indexing 1D arrays
print("First element of arr:", arr[0])
print("Last element of arr:", arr[-1])
print("Elements from index 1 to 4:", arr[1:5])
print("Every second element:", arr[::2])

# Indexing 2D arrays
print("Element at row 0, column 1 of mul_dim:", mul_dim[0, 1])
print("First row of mul_dim:", mul_dim[0, :])
print("Second column of mul_dim:", mul_dim[:, 1])
print("Slice of mul_dim (rows 0-1, columns 1-2):\n", mul_dim[0:2, 1:3])

# ===== ARITHMETIC OPERATIONS =====
# Element-wise math works when shapes match (or broadcast); operators and NumPy ufuncs behave similarly.
print("\n" + "=" * 50)
print("ARITHMETIC OPERATIONS")
print("=" * 50)

# Creating two one-dimensional arrays for arithmetic operations
x = np.array([1, 2, 3, 4, 5])
y = np.array([11, 12, 13, 14, 15])
print("Array x:", x)
print("Array y:", y)

# Performing element-wise arithmetic operations using operators
print("\nUsing Operators:")
print("Addition (x + y):", x + y)
print("Subtraction (x - y):", x - y)
print("Multiplication (x * y):", x * y)
print("Division (x / y):", x / y)
print("Floor Division (x // y):", x // y)
print("Power (x ** 2):", x ** 2)

# Using NumPy functions for arithmetic operations
print("\nUsing NumPy Functions:")
sum_result = np.add(x, y)
print("Sum using np.add:", sum_result)
print("Difference using np.subtract:", np.subtract(x, y))
print("Product using np.multiply:", np.multiply(x, y))
print("Quotient using np.divide:", np.divide(x, y))
print("Modulus using np.mod:", np.mod(x, y))
print("Power using np.power (x^2):", np.power(x, 2))
print("Square root using np.sqrt:", np.sqrt(y))
print("Absolute value using np.abs:", np.abs(x - y))

# Scalar operations or broadcasting
print("\nScalar Operations:")
print("x + 10:", x + 10)
print("x * 3:", x * 3)
print("x / 2:", x / 2)

# ===== STATISTICAL FUNCTIONS (1D Arrays) =====
# Reduction operations (min, max, sum, mean, etc.) collapse an array to a single value.
# Creating another one-dimensional NumPy array
a = np.array([1, 2, 3, 4, 5])
print("Array a:", a)

# Finding the minimum and maximum values in the array
print("Minimum value in a:", np.min(a))
print("Maximum value in a:", np.max(a))

# Finding the sum and mean (average) of the array
print("Sum of elements in a:", np.sum(a))
print("Mean of elements in a:", np.mean(a))
print("Median of elements in a:", np.median(a))
print("Standard deviation:", np.std(a))
print("Variance:", np.var(a))

# ===== 2D ARRAYS (MATRICES) - OPERATIONS =====
# Element-wise operations require identical shapes; transpose flips rows/columns.
print("\n" + "=" * 50)
print("2D ARRAYS - MATRIX OPERATIONS")
print("=" * 50)

# Creating two two-dimensional arrays (matrices)
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrix a:\n", a)
print("Matrix b:\n", b)

# Print properties of the 2D arrays
print("\nProperties:")
print("Number of dimensions in a:", a.ndim)
print("Size of a:", a.size)
print("Shape of a:", a.shape)

# Element-wise operations on matrices
print("\nElement-wise Operations:")
print("Sum of a and b (a + b):\n", a + b)
print("Difference (a - b):\n", a - b)
print("Element-wise multiplication (a * b):\n", a * b)
print("Element-wise division (a / b):\n", a / b)

# Matrix transpose
print("\nTranspose of a:\n", a.T)  # Swap rows and columns

# ===== STATISTICAL FUNCTIONS (2D Arrays) =====
# Axis parameter: 0 aggregates columns; 1 aggregates rows.
print("\n" + "=" * 50)
print("STATISTICAL FUNCTIONS - 2D ARRAYS")
print("=" * 50)

# Summation and other statistical functions on the two-dimensional array
print("Sum of all elements in a:", np.sum(a))
print("Minimum value in a:", np.min(a))
print("Maximum value in a:", np.max(a))
print("Mean of elements in a:", np.mean(a))
print("Median of elements in a:", np.median(a))
print("Standard deviation of a:", np.std(a))

# Transpose and matrix multiplication
print("\nTranspose and Matrix Multiplication:")
array = np.array([[25,64],[45,23]])
print(array)
print("\nrows become Column:\n", array.T)  #rows become column and column become rows

b1 = np.array([[2,3],[4,5]])
b2 = np.array([[5,6],[7,8]])
'''
[
  (2*5) + (3*7) , (2*6) + (3*8)
  (4*5) + (5*7) , (4*6) + (5*8)
]
'''
print(b1)
print(b2)
matrix_multi = np.dot(b1, b2) # matrix multiplication requires inner dims to align (2x2 @ 2x2 here)
print("Matrix multiplication (b1 . b2):\n")
print(matrix_multi)
print(b1@b2)  # @ is equivalent dot product
print()
# Creating matrices for multiplication
mat1 = np.array([[1, 2], [3, 4], [5, 6]])  # 3x2 matrix
mat2 = np.array([[7, 8, 9], [10, 11, 12]])  # 2x3 matrix
print("Matrix 1 (3x2):\n", mat1)
print("Matrix 2 (2x3):\n", mat2)

# Matrix multiplication (dot product)
result = np.dot(mat1, mat2)
print("Matrix multiplication (mat1 @ mat2):\n", result)  # 3x2 @ 2x3 => 3x3

# Creating arrays with convenience functions
zeros_array = np.zeros(5)  # Array of zeros
ones_array = np.ones(5)  # Array of ones
range_array = np.arange(0, 10, 2)  # Inclusive start, exclusive stop, step 2
a2 = np.arange(9)

print("Zeros array:", zeros_array)
print("Ones array:", ones_array)
print("Range array (0 to 10, step 2):", range_array)
print(a2)

# Creating 2D arrays with convenience functions
zeros_2d = np.zeros((3, 4))  # 3x4 matrix of zeros
# zeros_2d = np.zeros([3, 4])  # 3x4 matrix of zeros
ones_2d = np.ones((2, 3))  # 2x3 matrix of ones
identity_matrix = np.eye(3)  # Square identity matrix
print("2D Zeros array (3x4):\n", zeros_2d)
print("2D Ones array (2x3):\n", ones_2d)
print("Identity matrix (3x3):\n", identity_matrix)

bool = np.array([[True, True],[True, False]])
print("all() with axis 0:", np.all(bool))  # True only if every element is True
print("all() with axis none:", np.all(bool,axis=0))  # Column-wise logical AND

# Reshaping arrays
reshaped = arr.reshape(2, 3)  # Total elements must stay constant (6 -> 2x3)
print("Original arr:", arr)
print("Reshaped arr (2x3):\n", reshaped)

#reshape matrix
reshape = a2.reshape(3,3)  # 9 elements -> 3x3 grid
print("Reshape:\n", reshape)

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

#third column remove
result = reshape[:, :2]  # Keep first two columns
print("Only two column Reshape:\n",result)

result = reshape[:2, :]  # Keep first two rows
print("Only two Row Reshape:\n",result)

#vertically printing
x = np.array([[12,23],[23,43]])
y = np.array([[56,67],[78,89]])
z = np.array([[32,43],[54,65]])
print("X:\n",x,"\nY:\n", y, "\nZ:\n", z)

v= np.vstack((x,y,z)) # Stack vertically (increase rows)
print("Vertically vstack:\n", v)

h= np.hstack((x,y,z)) # Stack horizontally (increase columns)
print("Horizontally vstack:\n", h)

# Vertical and horizontal split
arrr = np.array([[1,2,3,4],[5,6,7,8]])
print(arrr)

vsplit = np.vsplit(arrr, 2)  # Split into 2 row blocks
print("\nVertically split\n", vsplit)

hsplit = np.hsplit(arrr, 2)  # Split into 2 column blocks
print("\nHorizontally split\n", hsplit)

jp = np.array([2,36,49,64])
print("Sqrt : ",np.sqrt(jp)) #squrt function
print("EXP : ", np.exp(jp)) #exponential function
print("sin : ", np.sin(jp)) #sin function
print("Cos : ", np.cos(jp)) #cos function
print("std : ", np.std(jp)) # standard deviation

#Random Function
print("random:", format(np.random.random(20)))  # 20 random floats in [0, 1)
#Random Function matrix
print("2d array random:\n", format(np.random.rand(3,4)))  # 3x4 random floats
#Random Function integer serie
print("Random Integer:\n", format(np.random.randint(0,100,20)))  # 20 ints in [0, 100)
#Random Function Permutation
print("Permutation:\n", format(np.random.permutation(np.arange(20))))  # Shuffle range(20)