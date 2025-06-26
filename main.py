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
