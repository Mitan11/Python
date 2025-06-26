# main.py

"""
👋 Welcome to Python Tutorial!

💡 How to Use This File:
1. All code examples are commented out (start with #) so you can read through safely
2. To try any example:
   - Remove the # from the beginning of each line you want to run
   - You can select multiple lines and press Ctrl+/ (or Cmd+/ on Mac) to uncomment
3. To run the code:
   - Save the file after uncommenting
   - Run it using your Python interpreter

Example:
# name = "Mitan"     <- Currently commented (won't run)
name = "Mitan"      <- Uncommented (will run)

Feel free to experiment with the examples!
"""

print("Har Har Mahadev")


# -------------------- COMMENTS IN PYTHON --------------------
# Definition: Comments are lines of text in your code that are completely ignored by the Python interpreter.
# They serve as notes for humans reading the code, not for the computer to execute.

# 1. SINGLE-LINE COMMENTS:
# - Start with the '#' symbol
# - Everything after # on that line is ignored by Python
# - Used for brief explanations or quick notes

# Good examples of single-line comments:

# name = "Mitan"  # Storing user's first name
# age = 25        # User's current age in years
# print("Hello")  # Output greeting to console

# 2. MULTI-LINE COMMENTS:
# Python has two ways to write multi-line comments:

# Method 1: Using multiple # symbols
# This is the first line
# This is the second line
# This is the third line

# Method 2: Using triple quotes (docstrings)
"""
This is a multi-line comment using triple double-quotes.
Advantages of this method:
1. Easier to write multiple lines
2. Good for documentation
3. Commonly used for module/function/class documentation

Note: While this is technically a string literal,
      if it's not assigned to a variable, Python ignores it.
"""

"""
You can also use triple single-quotes
for multi-line comments.
Both triple quotes work the same way.
"""

# 3. BEST PRACTICES FOR COMMENTS:
# ✓ Write comments that explain WHY, not WHAT
# ✓ Keep comments up-to-date with code changes
# ✓ Use clear and concise language
# ✓ Add comments for complex logic
# ✗ Avoid obvious comments that don't add value

# Bad comment (states the obvious):
# x = 0           # Initialize counter
# x = x + 1      # Add 1 to x

# Good comment (explains why):
# counter = 0     # Initialize user interaction counter
# counter = counter + 1  # Increment counter for each user interaction

# -------------------- VARIABLES IN PYTHON --------------------
# 📦 What is a Variable?
# A variable is like a container that stores data in your program.
# Think of it as a labeled box where you can put different types of values.

# ✅ Basic Variable Examples:
# first_name = "Mitan"     # Stores text (string)
# age = 22                  # Stores a number (integer)
# height = 6.8             # Stores a decimal number (float)
# is_student = True        # Stores True/False (boolean)

# 🚫 INVALID Variable Names (These will cause errors):
# ❌ Can't start with a number:
# 1name = "Wrong"        # Error!

# ❌ Can't use spaces:
# my name = "Wrong"      # Error!

# ❌ Can't use special characters (except underscore):
# name$ = "Wrong"        # Error!
# user@name = "Wrong"    # Error!
# first-name = "Wrong"   # Error!

# ✅ VALID Variable Naming Styles:
# 1. snake_case (Python's preferred style):
# user_name = "mitan_tank"        # Words separated by underscores
# first_name = "Mitan"            # Easy to read
# date_of_birth = "2000-01-01"    # Clear and readable

# 2. camelCase (Common in JavaScript):
# userName = "mitanTank"          # First word lowercase, others capitalized
# firstName = "Mitan"             # Second word capitalized
# dateOfBirth = "2000-01-01"      # Each new word capitalized

# 3. PascalCase (Used for classes in Python):
# UserName = "MitanTank"          # Each word capitalized
# FirstName = "Mitan"             # Used mainly for class names
# DateOfBirth = "2000-01-01"      # Not common for regular variables

# 🎯 Variable Naming Best Practices:
# ✅ DO:
# max_attempts = 3        # Clear and descriptive
# user_age = 25          # Self-explanatory
# is_active = True       # Boolean variables often start with 'is_' or 'has_'

# ❌ DON'T:
# x = 3                  # Too vague
# a = 25                 # Not descriptive
# tmp = True             # Unclear purpose

# 💡 Variable Assignment Examples:
# Single assignment
# score = 100

# Multiple assignment on one line
# x, y, z = 1, 2, 3      # x = 1, y = 2, z = 3

# Same value to multiple variables
# a = b = c = 0          # All variables get value 0

# 🔄 Variable Reassignment:
# Variables can change their value
# counter = 1            # Initial value
# counter = counter + 1  # New value is 2
# counter += 1          # Shorter way to add 1 (now 3)

# Variables can even change type (though not recommended)
# variable = 100        # Number
# variable = "hundred"  # Now it's text

# -------------------- DATA TYPES --------------------
# 📦 What are Data Types?
# A data type is like a label that tells Python what kind of data you're storing
# Just like different boxes for different items at home!

# 🔢 1. NUMBERS:
# There are 3 types of numbers in Python:

# Type 1: Integer (int) - Whole numbers
# age = 25              # No decimal point
# score = 100
# temperature = -5      # Can be negative too

# Type 2: Float (float) - Decimal numbers
# price = 99.99        # Has decimal point
# height = 5.8
# weight = 68.5

# Type 3: Complex - Numbers with real and imaginary parts
# Usually used in advanced math, don't worry much about these!
# complex_num = 4 + 5j  # j represents imaginary part

# 🔤 2. STRING (str) - Text Data:
# Anything in quotes is a string
# name = "Mitan"                # Double quotes work
# message = 'Hello, World!'     # Single quotes work too
# address = "123 Main Street"   # Numbers in quotes are still strings
# empty_string = ""            # An empty string is valid too

# 💡 Fun Fact: You can use either single (') or double (") quotes
# They work exactly the same way!

# ✅ 3. BOOLEAN (bool) - True/False:
# Like a light switch - only two possible values!
# is_student = True            # Yes, I am a student
# is_raining = False          # No, it's not raining
# has_passed = True           # Yes, test is passed

# 🎯 Real World Examples:
# student_info = "Mitan Tank"     # String: For names
# student_age = 22               # Integer: For age
# student_grade = 95.5           # Float: For grade/marks
# is_present = True             # Boolean: For attendance

# 💡 Quick Tip: Check Type
# To find out the type of any value, use type():
# name = "Mitan"
# print(type(name))    # Will show: <class 'str'>

# 🔄 Converting Between Types:
# score = "100"        # This is a string
# score = int(score)   # Now converted to integer (100)
# 
# price = 99
# price = str(price)   # Now converted to string ("99")
# 
# text = "True"
# text = bool(text)    # Now converted to boolean (True)

# -------------------- STRING INDEXING & SLICING --------------------
# 🔤 What is a String?
# A string is just text! It can contain letters, numbers, symbols, spaces, even emojis!
# You can use single quotes (') or double quotes (")

# Examples:
# name = "Mitan"                 # Letters
# number_text = "123"           # Numbers (as text)
# mixed = "Hello! 123 🌟"       # Mix of everything
# empty = ""                    # Empty string

# 💾 Understanding Unicode in Strings
# Every character in a string has a unique number (Unicode)
# You can find these numbers using ord() and chr()

# Examples of ord() - Get Unicode number of character:
# print(ord("A"))      # 65
# print(ord(" "))      # 32 (space)
# print(ord("😊"))     # 128522 (emoji)

# Examples of chr() - Get character from Unicode number:
# print(chr(65))       # A
# print(chr(128522))   # 😊

# 🔢 STRING INDEXING (Getting Single Characters)
# Each character has a position number (index)
# First character is index 0
# Last character is index -1

# Example string:
# message = "Hello"
#  Index:   01234
# -Index:  -5-4-3-2-1

# Getting characters by index:
# text = "Hello"
# print(text[0])     # H (first character)
# print(text[1])     # e (second character)
# print(text[4])     # o (last character)

# Negative indexing (counting from end):
# print(text[-1])    # o (last character)
# print(text[-2])    # l (second-last character)
# print(text[-5])    # H (first character)

# ✂️ STRING SLICING (Getting Parts of Strings)
# Think of slicing like cutting a piece of bread - you need to know where to start and stop!

# 📝 Slicing Format: string[start : stop : step]
#    - start: Where to begin the slice (included)
#    - stop:  Where to end the slice (not included)
#    - step:  How many characters to jump/skip

# 🎯 Let's understand with a simple word: "Python"
# 
#    P   y   t   h   o   n
#    0   1   2   3   4   5   (Positive index)
#   -6  -5  -4  -3  -2  -1   (Negative index)
#
# 1️⃣ Basic Slicing (start:stop)
# word = "Python"
# print(word[0:2])    # "Py"    (Start at 0, stop before 2)
# print(word[2:4])    # "th"    (Start at 2, stop before 4)
# print(word[4:6])    # "on"    (Start at 4, stop before 6)

# 2️⃣ Using Negative Index
# print(word[-3:-1])  # "ho"    (Start at -3, stop before -1)
# print(word[-2:])    # "on"    (Start at -2, go to end)
# print(word[:-2])    # "Pyth"  (Start at beginning, stop before -2)

# 3️⃣ Using Step
# word = "Python"
# print(word[::1])    # "Python"  (Every character - step 1)
# print(word[::2])    # "Pto"     (Every 2nd character)
# print(word[::3])    # "Ph"      (Every 3rd character)

# 4️⃣ Common Patterns (with a longer example)
# text = "Hello, Python World!"
#
# Get first 5 characters:
# print(text[0:5])     # "Hello"
# print(text[:5])      # "Hello"  (Same as above - 0 can be omitted)
#
# Get last 6 characters:
# print(text[-6:])     # "World!"
#
# Reverse the string:
# print(text[::-1])    # "!dlroW nohtyP ,olleH"
#
# Get every 2nd character:
# print(text[::2])     # "Hlo yhnWrd"

# 🎨 More Creative Examples:
# message = "Hello, Python World!"
#
# Get only the word "Python":
# print(message[7:13])      # "Python"
#
# Get "Hello" and "World" only:
# print(message[:5] + message[-6:])  # "HelloWorld"
#
# Reverse only "Python":
# print(message[:7] + message[7:13][::-1] + message[13:])  # "Hello, nohtyP World!"

# 💡 Pro Tips:
# 1. If start is omitted, slice starts from beginning
#    print(text[:5])     # Same as text[0:5]
#
# 2. If stop is omitted, slice goes until end
#    print(text[7:])     # From index 7 to end
#
# 3. If step is negative, string is read backwards
#    print(text[::-1])   # Reverse entire string
#
# 4. You can't go out of bounds - Python handles it:
#    text = "Python"
#    print(text[0:100])  # Prints "Python" (no error)

# 🚫 Common Mistakes to Avoid:
# text = "Python"
# print(text[6])        # Error! Index 6 doesn't exist
# print(text[0:6:0])    # Error! Step cannot be 0

# -------------------- TYPE CONVERSION --------------------
# 🔄 Type Conversion in Python
# 📌 What is Type Conversion?
# Type conversion means changing one data type into another.
# Example: converting a number into a string or a string into a number.

# 🔷 1. Types of Type Conversion
#
# ✅ A. Implicit Conversion (Automatic)
# Python does this by itself when needed.
# Example:
# a = 10         # int
# b = 2.5        # float
# result = a + b
# print(result)        # 12.5
# print(type(result))  # <class 'float'>
# ✅ Python converted int to float because float is more precise.

# ✅ B. Explicit Conversion (Type Casting)
# You do this yourself using built-in functions.
#
# 🛠️ Common Type Conversion Functions:
# int()      # Converts to Integer
# float()    # Converts to Float
# str()      # Converts to String
# bool()     # Converts to Boolean
# complex()  # Converts to Complex Number
# list()     # Converts to List
# tuple()    # Converts to Tuple
# set()      # Converts to Set
# dict()     # Converts to Dictionary
#
# 🔸 Example of Explicit Conversion:
# a = 12
# print(type(a))    # <class 'int'>
# a = str(a)        # Convert to string
# print(a)          # "12"
# print(type(a))    # <class 'str'>

# ❗ Important Notes
# 🔺 You cannot convert letters or symbols directly to int():
# int("abc")   # ❌ Error
#
# ✅ You can convert number strings:
# a = "100"
# a = int(a)
# print(a)          # 100

# ✅ Truthy & Falsy Values (Using bool())
# 📌 What is a Truthy/Falsy value?
# When you use bool(something), Python checks whether the value is:
#   ✅ Truthy → becomes True
#   ❌ Falsy → becomes False
#
# ❌ These 7 values are always False in Python:
# 0
# 0.0
# False
# None
# "" (empty string)
# [] (empty list)
# {} or set() or tuple() (empty container)
#
# ✅ Everything else is considered True!
#
# 🔎 Examples:
# print(bool(0))        # False
# print(bool(""))       # False
# print(bool([]))       # False
# print(bool(1))        # True
# print(bool("hello"))  # True
# print(bool([1, 2]))   # True

# 🎯 Summary Table
# Type         Method           Example
# Implicit     Auto by Python   print(10 + 2.5)
# Explicit     Use function     int("5")
#
# Function     Converts To
# int()        Integer
# float()      Float
# str()        String
# bool()       Boolean

# 🚫 Common Mistakes
# Mistake                Fix
# int("abc")             Use valid number string only
# bool("False") → True   Non-empty string is always True
# int("12.5") → Error    First convert to float, then int

# -------------------- TRUTHY & FALSY VALUES --------------------
# Definition: In Python, every value can be evaluated as either True or False in a boolean context (like in if statements).
# Falsy values are treated as False; all other values are treated as True (truthy).
# Only 7 values are considered falsy:
# 0, 0.0, None, False, "", [], {}

# print(bool(0))       # False (zero is falsy)
# print(bool(""))      # False (empty string is falsy)
# print(bool([]))      # False (empty list is falsy)
# print(bool("Hi"))    # True (non-empty string is truthy)