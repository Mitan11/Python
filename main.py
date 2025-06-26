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

