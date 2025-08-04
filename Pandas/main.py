"""
🐼 PANDAS SERIES TUTORIAL
=========================

PANDAS SERIES DEFINITION:
========================
A Series is a one-dimensional labeled array capable of holding any data type. 
The axis labels are collectively called the index.

KEY FEATURES:
- 1D array (like a single column)
- Has an index (row labels)
- Can hold any data type
- Building block of DataFrames
"""

import pandas as pd
import numpy as np

print("🐼 PANDAS SERIES TUTORIAL")
print("=" * 50)

# ============================================================================
# CREATING SERIES - DIFFERENT METHODS
# ============================================================================
print("\n📊 CREATING SERIES - DIFFERENT METHODS")
print("-" * 40)
print("EXPLANATION: There are multiple ways to create a Pandas Series.")
print("Each method has its own advantages depending on your data source.")
print("The index is automatically created if not specified.")

# Method 1: From a list
print("1. Creating Series from a list:")
print("EXPLANATION: Simplest way - just pass a list to pd.Series()")
print("Pandas automatically creates numeric index (0, 1, 2, ...)")
my_list = [10, 20, 30]
series1 = pd.Series(my_list)
print("pd.Series(my_list):")
print(series1)
print(f"Type: {type(series1)}")
print(f"Index: {list(series1.index)}")
print("Note: Default index starts from 0")

# Method 2: From a list with custom index
print("\n2. Creating Series from a list with custom index:")
print("EXPLANATION: You can specify custom labels for the index")
print("This makes the Series more meaningful and easier to access")
labels = ['a', 'b', 'c']
series2 = pd.Series(my_list, index=labels)
print("pd.Series(my_list, index=labels):")
print(series2)
print(f"Index: {list(series2.index)}")
print("Now you can access elements by label: series2['a'] = 10")

# Method 3: From a NumPy array
print("\n3. Creating Series from a NumPy array:")
print("EXPLANATION: NumPy arrays work seamlessly with Pandas")
print("This is useful when working with numerical computations")
arr = np.array([10, 20, 30])
series3 = pd.Series(arr)
print("pd.Series(arr):")
print(series3)
print("NumPy arrays are efficient for numerical operations")

# Method 4: From a dictionary
print("\n4. Creating Series from a dictionary:")
print("EXPLANATION: Dictionary keys automatically become the index")
print("This is very convenient when you have labeled data")
d = {'a': 10, 'b': 20, 'c': 30}
series4 = pd.Series(d)
print("pd.Series(d):")
print(series4)
print("Note: Dictionary keys become the index!")
print("This is one of the most intuitive ways to create Series")

# ============================================================================
# SERIES WITH DIFFERENT DATA TYPES
# ============================================================================
print("\n📈 SERIES WITH DIFFERENT DATA TYPES")
print("-" * 40)
print("EXPLANATION: Pandas Series can hold different data types.")
print("The dtype attribute shows the data type of the Series.")
print("Mixed types are stored as 'object' dtype.")

# String Series
print("1. String Series:")
print("EXPLANATION: Strings are stored as 'object' dtype in Pandas")
print("This allows for flexible string operations")
string_series = pd.Series(['apple', 'banana', 'cherry'], index=['fruit1', 'fruit2', 'fruit3'])
print(string_series)
print(f"Data type: {string_series.dtype}")
print("String Series support text operations like .str.upper()")

# Float Series
print("\n2. Float Series:")
print("EXPLANATION: Float numbers are stored as 'float64' dtype")
print("This provides high precision for decimal calculations")
float_series = pd.Series([3.14, 2.71, 1.41], index=['pi', 'e', 'sqrt2'])
print(float_series)
print(f"Data type: {float_series.dtype}")
print("Float Series are perfect for mathematical operations")

# Mixed data types (object)
print("\n3. Mixed data types:")
print("EXPLANATION: When Series contains different types, it becomes 'object' dtype")
print("This is flexible but less efficient than homogeneous types")
mixed_series = pd.Series(['hello', 42, 3.14, True], index=['str', 'int', 'float', 'bool'])
print(mixed_series)
print(f"Data type: {mixed_series.dtype}")
print("Mixed types are useful but avoid for large datasets")

# ============================================================================
# SERIES OPERATIONS AND METHODS
# ============================================================================
print("\n🔧 SERIES OPERATIONS AND METHODS")
print("-" * 40)
print("EXPLANATION: Pandas Series come with many built-in methods.")
print("These methods make data analysis much easier than working with lists.")
print("Operations are 'vectorized' - applied to all elements at once.")

# Create a sample series for operations
numbers = pd.Series([1, 3, 5, 7, 9, 2, 4, 6, 8, 10], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print("Sample Series:")
print(numbers)

# Basic statistics
print("\n1. Basic Statistics:")
print("EXPLANATION: Statistical methods are built-in and optimized")
print("No need to write loops - just call the method!")
print(f"Mean: {numbers.mean()}")
print(f"Median: {numbers.median()}")
print(f"Sum: {numbers.sum()}")
print(f"Min: {numbers.min()}")
print(f"Max: {numbers.max()}")
print(f"Standard deviation: {numbers.std():.2f}")
print("These methods ignore missing values automatically")

# Indexing and selection
print("\n2. Indexing and Selection:")
print("EXPLANATION: iloc uses integer positions, loc uses labels")
print("iloc is like list indexing, loc is like dictionary access")
print(f"First element: {numbers.iloc[0]}")
print(f"Last element: {numbers.iloc[-1]}")
print(f"Element with index 'c': {numbers.loc['c']}")
print(f"First 3 elements: {numbers.head(3).tolist()}")
print(f"Last 3 elements: {numbers.tail(3).tolist()}")
print("head() and tail() are convenient for previewing data")

# Boolean indexing
print("\n3. Boolean Indexing:")
print("EXPLANATION: Boolean indexing filters data based on conditions")
print("The condition creates a True/False mask for each element")
even_numbers = numbers[numbers % 2 == 0]
print("Even numbers:")
print(even_numbers)
print("This is much cleaner than writing loops!")

# Mathematical operations
print("\n4. Mathematical Operations:")
print("EXPLANATION: Mathematical operations are 'vectorized'")
print("They apply to all elements at once, not element by element")
print("Original series:")
print(numbers)
print("\nSquared values:")
print(numbers ** 2)
print("\nValues + 10:")
print(numbers + 10)
print("Vectorized operations are much faster than loops")

# ============================================================================
# SERIES WITH MISSING DATA
# ============================================================================
print("\n❓ SERIES WITH MISSING DATA")
print("-" * 40)
print("EXPLANATION: Real-world data often has missing values.")
print("Pandas represents missing data as NaN (Not a Number).")
print("Handling missing data is crucial for data analysis.")

# Create series with missing values
missing_series = pd.Series([1, None, 3, np.nan, 5], index=['a', 'b', 'c', 'd', 'e'])
print("Series with missing values:")
print(missing_series)

# Check for missing values
print("\n1. Checking for missing values:")
print("EXPLANATION: isnull() returns True for missing values")
print("isnull().sum() counts how many missing values exist")
print(f"Has missing values: {missing_series.isnull().any()}")
print(f"Number of missing values: {missing_series.isnull().sum()}")
print("This helps you understand your data quality")

# Fill missing values
print("\n2. Filling missing values:")
print("EXPLANATION: fillna() replaces missing values with specified values")
print("You can fill with constants, means, medians, or forward/backward fill")
filled_series = missing_series.fillna(0)
print("After filling with 0:")
print(filled_series)
print("Choose filling strategy based on your data context")

# Drop missing values
print("\n3. Dropping missing values:")
print("EXPLANATION: dropna() removes rows with missing values")
print("Use this when missing data is not critical or you have enough data")
clean_series = missing_series.dropna()
print("After dropping missing values:")
print(clean_series)
print("Be careful - dropping can lose important data")

# ============================================================================
# SERIES INDEXING AND SLICING
# ============================================================================
print("\n🔍 SERIES INDEXING AND SLICING")
print("-" * 40)
print("EXPLANATION: Pandas provides powerful indexing capabilities.")
print("iloc: Integer-based indexing (like list indexing)")
print("loc: Label-based indexing (like dictionary access)")
print("Boolean indexing: Filter based on conditions")

# Create a series with string index
name_series = pd.Series([25, 30, 35, 40], index=['Alice', 'Bob', 'Charlie', 'Diana'])
print("Name-Age Series:")
print(name_series)

# Integer-based indexing (iloc)
print("\n1. Integer-based indexing (iloc):")
print("EXPLANATION: iloc uses integer positions (0, 1, 2, ...)")
print("Works exactly like Python list indexing")
print(f"First person: {name_series.iloc[0]}")
print(f"Last person: {name_series.iloc[-1]}")
print(f"First 2 people: {name_series.iloc[:2].tolist()}")
print("iloc is useful when you know the position but not the label")

# Label-based indexing (loc)
print("\n2. Label-based indexing (loc):")
print("EXPLANATION: loc uses the index labels (names in this case)")
print("Like accessing a dictionary with keys")
print(f"Alice's age: {name_series.loc['Alice']}")
print(f"Bob and Charlie: {name_series.loc[['Bob', 'Charlie']].tolist()}")
print("loc is more intuitive when you have meaningful labels")

# Boolean indexing
print("\n3. Boolean indexing:")
print("EXPLANATION: Boolean indexing filters data based on conditions")
print("The condition creates a mask of True/False values")
young_people = name_series[name_series < 35]
print("People under 35:")
print(young_people)
print("This is the most powerful way to filter data")

# ============================================================================
# SERIES METHODS AND UTILITIES
# ============================================================================
print("\n🛠️ SERIES METHODS AND UTILITIES")
print("-" * 40)
print("EXPLANATION: Pandas Series have many useful utility methods.")
print("These methods help you explore and understand your data.")
print("They save you from writing custom functions.")

# Create a sample series
sample_series = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 5], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
print("Sample Series:")
print(sample_series)

# Value counts
print("\n1. Value counts:")
print("EXPLANATION: value_counts() counts how many times each value appears")
print("Very useful for categorical data analysis")
print(sample_series.value_counts())
print("Shows frequency distribution of values")

# Unique values
print("\n2. Unique values:")
print("EXPLANATION: unique() returns all distinct values in the Series")
print("Useful for understanding what categories exist")
print(f"Unique values: {sample_series.unique()}")
print("Returns a NumPy array of unique values")

# Sort values
print("\n3. Sort values:")
print("EXPLANATION: sort_values() arranges data by values, not by index")
print("ascending=True (default) or ascending=False")
print("Sorted (ascending):")
print(sample_series.sort_values())
print("\nSorted (descending):")
print(sample_series.sort_values(ascending=False))
print("Useful for finding min/max values or creating rankings")

# Sort index
print("\n4. Sort index:")
print("EXPLANATION: sort_index() arranges data by index labels")
print("Useful when you want alphabetical or chronological order")
print("Sorted by index:")
print(sample_series.sort_index())
print("Different from sort_values() - sorts by labels, not values")

# ============================================================================
# SERIES VS LIST COMPARISON
# ============================================================================
print("\n📊 SERIES VS LIST COMPARISON")
print("-" * 40)
print("EXPLANATION: Let's compare Series with Python lists.")
print("Series have more features but lists are simpler.")
print("Choose based on your needs - Series for analysis, lists for simple data.")

# Create a list and series with same data
data_list = [10, 20, 30, 40, 50]
data_series = pd.Series(data_list, index=['a', 'b', 'c', 'd', 'e'])

print("List:")
print(data_list)
print(f"List type: {type(data_list)}")
print(f"List length: {len(data_list)}")

print("\nSeries:")
print(data_series)
print(f"Series type: {type(data_series)}")
print(f"Series length: {len(data_series)}")
print(f"Series index: {list(data_series.index)}")

# Operations comparison
print("\nOperations Comparison:")
print("EXPLANATION: Series have built-in methods, lists need manual calculation")
print("Series are more convenient for data analysis")
print(f"List sum: {sum(data_list)}")
print(f"Series sum: {data_series.sum()}")
print(f"List mean: {sum(data_list)/len(data_list)}")
print(f"Series mean: {data_series.mean()}")
print("Series methods are optimized and handle edge cases")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n🎉 PANDAS SERIES SUMMARY")
print("=" * 50)

print("✅ WHAT WE LEARNED:")
print("1. Series is a 1D labeled array")
print("2. Multiple ways to create Series:")
print("   - From lists, arrays, dictionaries")
print("   - With custom or default index")
print("3. Series supports different data types")
print("4. Powerful indexing (iloc, loc)")
print("5. Built-in statistical methods")
print("6. Missing data handling")
print("7. Mathematical operations")

print("\n🔑 KEY CONCEPTS:")
print("- Index: Labels for each element")
print("- dtype: Data type of the series")
print("- iloc: Integer-based indexing")
print("- loc: Label-based indexing")
print("- Vectorized operations: Apply to all elements")

print("\n📚 COMMON METHODS:")
print("- .mean(), .median(), .sum(), .min(), .max()")
print("- .isnull(), .fillna(), .dropna()")
print("- .sort_values(), .sort_index()")
print("- .value_counts(), .unique()")
print("- .head(), .tail()")

print("\n✨ Series are the building blocks of DataFrames! 🐼")

