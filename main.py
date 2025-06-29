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

# -------------------- END --------------------

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

# -------------------- END --------------------

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

# -------------------- END --------------------

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

# -------------------- END --------------------

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

# -------------------- END --------------------

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

# -------------------- END --------------------

# -------------------- INPUT & OUTPUT IN PYTHON --------------------
# 🖨️ Output in Python
# ✅ How to Show Output?
# Use the print() function to show anything on the screen.
#
# print("Hello, World!")
#
# ✅ Printing Variables
# You can also show the value of variables:
# name = "Mitan"
# print(name)  # Output: Mitan
#
# ✅ Using Formatted Strings (f-strings)
# You can insert variables inside a string using f""
# name = "Mitan"
# age = 20
# print(f"My name is {name} and I am {age} years old.")

# ⌨️ Input in Python
# ✅ How to Get Input From the User?
# Use the input() function.
# name = input("What is your name? ")
# print(f"Hello, {name}!")
#
# ⚠️ Default Data Type = String
# All input is taken as a string, even if you enter a number.
# age = input("Enter your age: ")
# print(type(age))  # <class 'str'>
#
# So if you want it as a number (like for calculation), you must convert it:
# age = int(input("Enter your age: "))
# print(f"Next year, you will be {age + 1} years old.")

# ✅ Example: Input + Output Together
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"Hi {name}, you are {age} years old.")

# 🧠 Summary Table
# Task            Function         Example
# Show output     print()          print("Hello")
# Get input       input()          name = input("Enter name: ")
# Convert input   int(), float()   age = int(input("Enter age: "))
# Combine output  f-string         f"Hi {name}"

# -------------------- END --------------------

# -------------------- OPERATORS IN PYTHON --------------------
# ⚙️ What are Operators?
# Definition: Operators are special symbols or keywords in Python that are used to perform operations on values or variables. 
# They let you do things like add numbers, compare values, assign data, and combine conditions.
# For example: + adds numbers, == compares values, and checks logic conditions.
#
# Operators make it easy to write calculations, logic, and data manipulation in your code.
#
# 🔢 1. Arithmetic Operators (Basic Math)
# Operator   Name              Example     Output
#   +        Addition          5 + 3       8
#   -        Subtraction       10 - 4      6
#   *        Multiplication    2 * 3       6
#   /        Division          10 / 3      3.33
#   //       Floor Division    10 // 3     3
#   %        Modulus           10 % 3      1
#   **       Exponent          2 ** 3      8
#
# 🧪 Example:
# a = 10
# b = 3
# print(a + b)   # 13
# print(a % b)   # 1
# print(a ** b)  # 1000

# 📝 2. Assignment Operators (Assigning Values)
# Operator   Meaning              Example
#   =        Assign               x = 5
#   +=       Add and assign       x += 2
#   -=       Subtract and assign  x -= 1
#   *=       Multiply and assign  x *= 3
#   /=       Divide and assign    x /= 2
#   //=      Floor divide assign  x //= 2
#   %=       Modulus assign       x %= 2
#   **=      Exponent assign      x **= 2
#
# 🧪 Example:
# x = 5
# x += 3    # x = x + 3
# print(x)  # Output: 8

# ⚖️ 3. Comparison Operators (Compare Values)
# Used to compare values, gives True or False.
# Operator   Meaning                  Example     Output
#   ==       Equal to                 5 == 5      True
#   !=       Not equal to             5 != 3      True
#   >        Greater than             5 > 3       True
#   <        Less than                5 < 3       False
#   >=       Greater or equal         5 >= 5      True
#   <=       Less or equal            5 <= 4      False

# 🔗 4. Logical Operators (Combine Conditions)
# Used to combine multiple conditions.
# Operator   Meaning                  Example                Result
#   and      True if both are True    5 > 2 and 3 < 4        True
#   or       True if any is True      5 > 2 or 3 > 5         True
#   not      Reverses condition       not (5 > 2)            False

# ✅ Example Using All
# a = 10
# b = 5
#
# # Arithmetic
# print(a + b)      # 15
#
# # Assignment
# a += 2
# print(a)          # 12
#
# # Comparison
# print(a == b)     # False
#
# # Logical
# print(a > b and b > 2)  # True

# -------------------- END --------------------

# -------------------- CONDITIONAL STATEMENTS IN PYTHON --------------------
# ✅ Conditional Statements in Python
# 💡 What Are Conditional Statements?
# Conditional statements let your program make decisions and run different code depending on conditions.
# They help you control the flow of your program — that's why they're also called control flow statements.
#
# 🧠 Real-Life Example:
# You ask a user to enter a number.
# If the number is greater than 10, print "Task A"
# Otherwise, print "Task B"
# Here, the number decides what code to run. This is what conditional logic does.
#
# 🧱 Types of Conditional Statements
#
# 🔹 1. if Statement
# Runs a block of code only if the condition is True.
# number = int(input("Enter a number: "))
# if number > 10:
#     print("Task A")
#
# 🔹 2. if-else Statement
# Runs one block if condition is True, another block if False.
# number = int(input("Enter a number: "))
# if number > 10:
#     print("Task A")
# else:
#     print("Task B")
#
# 🔹 3. if-elif-else Statement
# Use when you have multiple conditions to check in order.
# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 70:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")
#
# ⚠️ Python Syntax Rules
# - Use a colon : at the end of if, elif, and else lines.
# - The code under them must be indented (usually 4 spaces).
#
# ✅ Summary Table
# Statement        Description
# if               Runs when condition is True
# if-else          One block runs if True, another if False
# if-elif-else     Multiple conditions, runs only one match

# -------------------- END --------------------

# -------------------- LOOPS IN PYTHON --------------------
# 🔁 Loops in Python
# ✅ What Are Loops?
# Loops let you run a block of code multiple times without writing it again and again.
#
# For example, instead of writing:
# print("Hello")
# print("Hello")
# print("Hello")
# # ... 100 times!
# You can simply do:
# for i in range(100):
#     print("Hello")
#
# 🔄 Types of Loops in Python
# There are 2 main types of loops:
# - for loop: Use when you know how many times to run.
# - while loop: Use when you don't know how many times, but have a condition.
#
# 🪣 Understanding with Bucket Example:
# You have two buckets and a mug.
# If you know you need 4 mugs, you use a for loop.
# If you don't know how many mugs, but stop when the bucket is full, you use a while loop.
#
# 1️⃣ for Loop
# ✅ Syntax:
# for i in range(start, stop, step):
#     # code block
# start: where to begin (default is 0)
# stop: where to end (not included)
# step: how many numbers to skip (default is 1)
#
# 🔹 Example: Print numbers 1 to 5
# for i in range(1, 6):
#     print(i)
#
# 🔹 Example: Print "Hello" 10 times
# for i in range(10):
#     print("Hello")
#
# 2️⃣ while Loop
# ✅ Syntax:
# while condition:
#     # code block
# The loop will run as long as the condition is True.
#
# 🔹 Example: Print numbers from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
#
# 🔤 Loops with Strings
# There are two ways to loop through a string:
#
# A. Using index (with range)
# name = "Python"
# for i in range(len(name)):
#     print(name[i])
#
# B. Directly over the string
# name = "Python"
# for char in name:
#     print(char)
# This method is shorter and gives characters directly.
#
# 📌 Summary
# Loop Type   Use When You...                Example
# for         Know how many times to repeat  for i in range(5)
# while       Repeat until a condition False while x < 5
#
# Loop Use    Task                          Example
# Numbers     Print 1 to 10                 range(1, 11)
# Strings     Character-by-character loop   for c in "Python"

# -------------------- END --------------------

# -------------------- LOOP CONTROL STATEMENTS IN PYTHON --------------------
# 🚦 Loop Control Statements in Python
# These special keywords help you control the behavior of a loop:
#
# break – Stops the loop completely.
# continue – Skips the current iteration, continues to next.
# else (with loop) – Runs only if loop didn't break.
#
# 🛑 1. break – Exit the loop early
# 📖 Definition:
# break is used to immediately stop the loop when a condition is met.
#
# 🏁 Example: Race Track & Rain
# for lap in range(1, 21):
#     if lap == 16:
#         print("It started raining. Race stopped!")
#         break
#     print(f"Completed lap {lap}")
# ✅ Output:
# Completed lap 1
# Completed lap 2
# ...
# Completed lap 15
# It started raining. Race stopped!
#
# ⏭️ 2. continue – Skip one loop round
# 📖 Definition:
# continue skips the current iteration and moves to the next one.
#
# 🏃 Example: Skip Lap 16
# for lap in range(1, 21):
#     if lap == 16:
#         print("Skipped lap 16 due to injury.")
#         continue
#     print(f"Completed lap {lap}")
# ✅ Output:
# Completed lap 1
# ...
# Completed lap 15
# Skipped lap 16 due to injury.
# Completed lap 17
# ...
# Completed lap 20
#
# ➕ 3. else with Loops – Run after loop only if no break
# 📖 Definition:
# You can use else after a loop — it runs only if the loop finishes completely without hitting a break.
#
# ✅ Example A: Loop without break
# for i in range(5):
#     print(i)
# else:
#     print("Loop completed fully without break.")
# ✅ Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed fully without break.
#
# ❌ Example B: Loop with break
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("This will NOT be printed.")
# ✅ Output:
# 0
# 1
# 2
#
# 🧠 Summary Table
# Statement   What it does                        When to use
# break       Exits the loop early                When a condition is met to stop loop
# continue    Skips one iteration and continues   When you want to skip specific round
# else        Runs after the loop ends w/o break  To confirm loop ran fully

# -------------------- END --------------------

# -------------------- WHILE LOOP IN PYTHON --------------------
# 🔁 while Loop in Python
# 📌 What is a while loop?
# The while loop repeats a block of code as long as a condition is True.
# Use it when you don't know how many times the loop should run — you only know the condition to keep going.
#
# 🧠 Syntax:
# while condition:
#     # code to repeat
#
# 🔹 Example 1: Print numbers from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# 🟢 Output:
# 1
# 2
# 3
# 4
# 5
#
# 🔹 Example 2: while with break
# i = 1
# while i <= 10:
#     if i == 6:
#         print("Loop stopped at 6")
#         break
#     print(i)
#     i += 1
# 🟢 Output:
# 1
# 2
# 3
# 4
# 5
# Loop stopped at 6
#
# 🔹 Example 3: while with continue
# i = 0
# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
# 🟢 Output:
# 1
# 2
# 4
# 5
# (3 was skipped)
#
# 🔹 Example 4: while with else
# i = 1
# while i <= 3:
#     print(i)
#     i += 1
# else:
#     print("Loop ended naturally.")
# 🟢 Output:
# 1
# 2
# 3
# Loop ended naturally.
#
# 🔹 Example 5: while loop as input validator
# password = ""
# while password != "1234":
#     password = input("Enter password: ")
# print("Access granted!")
#
# 🤔 When to use while vs for:
# Use Case                    Loop Type
# You know how many times     for loop
# You don't know, but you have a condition    while loop
#
# ✅ Now you're ready to identify what type of loop to use:
# Fixed count → for
# Unknown repetitions with condition → while

# -------------------- END --------------------

# -------------------- FUNCTIONS IN PYTHON --------------------
# 🔧 Functions in Python
# ✅ What is a Function?
# A function is a reusable block of code that performs a specific task.
# It avoids repetition and keeps your program organized and readable.
#
# 🔹 Built-in vs User-Defined Functions
# Built-in functions: Already provided by Python
# → Examples: print(), input(), len(), range()
#
# User-defined functions: Functions you create using the def keyword.
#
# 🧠 Syntax of a Function
# def function_name():
#     # block of code
#
# 🔸 Example:
# def greet():
#     print("Hello, welcome!")
# greet()  # Calling the function
#
# 🧺 Parameters vs Arguments
# Parameters: Variables listed when defining a function.
# Arguments: Values you pass when calling the function.
#
# 🔸 Example:
# def greet(name):       # 'name' is a parameter
#     print("Hello", name)
# greet("Alice")         # "Alice" is an argument
#
# 🧩 Types of Arguments
# There are 3 main types of arguments:
#
# 1️⃣ Positional Arguments
# Values are assigned in the same order as parameters.
# def add(a, b):
#     print(a + b)
# add(5, 3)   # a = 5, b = 3
#
# 2️⃣ Default Arguments
# You can give a default value to parameters.
# If no argument is passed, default is used.
# def greet(name="User"):
#     print("Hello", name)
# greet()         # Output: Hello User
# greet("Mitan")  # Output: Hello Mitan
#
# 3️⃣ Keyword Arguments
# Pass arguments using key = value format.
# Order doesn't matter.
# def student(name, age):
#     print(f"{name} is {age} years old.")
# student(age=20, name="Akarsh")
#
# 🔁 Summary Table
# Type            Description                                    Order Matters?
# Positional      Match arguments to parameters by position     ✅ Yes
# Default         Uses default if argument not provided         ❌ No
# Keyword         Pass using key=value, order doesn't matter    ❌ No
#
# 🏗️ 6 Types of Functions
#
# 1️⃣ Function with No Parameters and No Return
# def greet():
#     print("Hello!")
# greet()
#
# 2️⃣ Function with Parameters but No Return
# def greet(name):
#     print(f"Hello, {name}!")
# greet("Mitan")
#
# 3️⃣ Function with Parameters and Return
# def add(a, b):
#     return a + b
# result = add(5, 3)
# print(result)  # 8
#
# 4️⃣ Function with Default Parameters
# def greet(name="User", age=18):
#     print(f"Hello {name}, you are {age} years old.")
# greet()  # Uses defaults
# greet("Mitan", 20)  # Uses provided values
#
# 5️⃣ Function with Variable Arguments (*args)
# def sum_all(*numbers):
#     return sum(numbers)
# result = sum_all(1, 2, 3, 4, 5)
# print(result)  # 15
#
# 6️⃣ Function with Keyword Arguments (**kwargs)
# def student_info(**info):
#     for key, value in info.items():
#         print(f"{key}: {value}")
# student_info(name="Mitan", age=20, grade="A")

# -------------------- END --------------------

# -------------------- DATA STRUCTURES IN PYTHON --------------------
# 📦 Data Structures in Python
# ✅ What are Data Structures?
# Data structures are used to store, organize, and manage data efficiently. 
# Python provides many built-in data structures that make your coding life easier.
#
# 🔹 Built-in Data Structures in Python
# Name        What it does                    Example
# List        Stores ordered, changeable data [1, 2, 3]
# Tuple       Stores ordered, unchangeable    (1, 2, 3)
# Set         Stores unique, unordered data   {1, 2, 3}
# Dictionary  Stores data in key-value pairs  {"name": "Akarsh"}
#
# 📋 Focus: List in Python
# ✅ Key Properties of Lists
# Property      Meaning
# Mutable       You can change values (add/remove/update) after creating the list.
# Duplicates    Allows repeated elements.
# Ordered       Maintains the order of items (indexing works).
# Heterogeneous Can store mixed data types (e.g., numbers, strings, etc.).
#
# 🔹 List Syntax
# my_list = [5, 2, 9, 1, 5, 6]  # Square brackets
#
# 🔹 List Indexing & Slicing (Same as Strings)
# print(my_list[0])    # Access by index
# print(my_list[-1])   # Negative indexing
# print(my_list[1:4])  # Slicing from index 1 to 3
#
# 🛠️ Common List Methods
# numbers = [5, 2, 9, 1, 5, 6]  # Initial list
#
# numbers.append(10)             # Adds 10 to the end
# numbers.insert(2, 15)          # Inserts 15 at index 2
# numbers.extend([20, 25, 30])   # Adds multiple elements at the end
# numbers.remove(5)              # Removes first occurrence of 5
# popped_item = numbers.pop(3)   # Removes and returns element at index 3
# index = numbers.index(6)       # Finds index of value 6
# count_5 = numbers.count(5)     # Counts how many times 5 appears
# numbers.sort()                 # Sorts the list in ascending order
# numbers.reverse()              # Reverses the order of the list
# new_numbers = numbers.copy()   # Makes a copy of the list
# numbers.clear()                # Removes all elements
#
# 🔁 List Traversing (Looping)
# A. Using index:
# for i in range(len(numbers)):
#     print(numbers[i])
#
# B. Directly:
# for num in numbers:
#     print(num)
#
# 🧠 Summary
# ✅ Use lists to store ordered, changeable collections.
# ✅ Use methods like .append(), .pop(), .sort() to manipulate them.
# ✅ You can loop using for, just like strings.
# ✅ Lists support indexing, slicing, and mixed data types.

# -------------------- TUPLE IN PYTHON --------------------
# 📦 Tuple in Python
# ✅ What is a Tuple?
# A tuple is a built-in data structure in Python that stores a collection of values. 
# It is similar to a list, but immutable (cannot be changed after creation).
#
# 🧠 Tuple Properties
# Property      Description
# Immutable     You cannot change, add, or remove elements once a tuple is created.
# Duplicates    Tuples allow repeated values (same as lists).
# Ordered       Tuples maintain the order of elements, and support indexing/slicing.
# Heterogeneous You can store different data types (int, string, list, etc.) in one tuple.
#
# 🧪 Syntax Example:
# my_tuple = (10, 20, 30, 10, "Hello", [1, 2])
# ✅ Yes, you can even store a list inside a tuple, though the tuple itself remains immutable.
#
# 🔁 Tuple Traversing
# ✅ Just like lists and strings:
# # Using index
# for i in range(len(my_tuple)):
#     print(my_tuple[i])
#
# # Directly
# for item in my_tuple:
#     print(item)
#
# 🔧 Tuple Methods (Only 2 Main Ones)
# 1️⃣ count() – Counts occurrences of a value
# my_tuple = (10, 20, 10, 30)
# print(my_tuple.count(10))  # Output: 2
#
# 2️⃣ index() – Returns the first index of a value
# print(my_tuple.index(30))  # Output: 3
#
# 📌 When to Use a Tuple?
# ✅ When you want to store a collection of values but don't want them to change.
# ✅ Ideal for fixed data, like days of the week, RGB color codes, etc.
# ✅ More memory-efficient than lists.
#
# 🆚 Tuple vs List (Quick Recap)
# Feature        List        Tuple
# Mutable        ✅ Yes      ❌ No
# Syntax         [1, 2, 3]  (1, 2, 3)
# Methods        Many        Only count() & index()
# Use case       General purpose    Fixed values

# -------------------- SET IN PYTHON --------------------
# 🧺 Set in Python
# ✅ What is a Set?
# A Set in Python is an unordered collection of unique and immutable elements.
# It's commonly used when you need to store items without duplicates.
#
# 🧠 Set Properties
# Property              Description
# ✅ Mutable            You can add or remove elements after creation.
# ❌ No Duplicates      Each element is unique, duplicates are removed automatically.
# ❌ Unordered          Elements don't maintain insertion order (can't use indexing).
# 🧩 Semi-Heterogeneous Can contain different data types, but only hashable types (e.g., numbers, strings, tuples).
# ❌ You cannot store lists or dictionaries inside sets.
#
# 🧪 Set Syntax
# my_set = {1, 2, 3}
# empty_set = set()  # NOTE: {} creates a dictionary, not a set
#
# 🔄 How Set Stores Data Internally
# Each value is passed through Python's built-in hash() function.
# These hashes are used to determine where to store items in memory.
# Because hash order isn't predictable, set items appear in random order.
#
# 🔁 Set Traversing
# Since sets don't have indexes, you must use a loop:
# for item in my_set:
#     print(item)  # Order is not guaranteed
#
# 🛠️ Common Set Methods
# s = {1, 2, 3}
# s.add(4)           # ➕ Adds 4 to the set
# s.remove(2)        # ➖ Removes 2 (❗Raises error if not found)
# s.discard(5)       # ➖ Removes 5 (✅ No error if not found)
# popped = s.pop()   # ❌ Removes a random item
# s.clear()          # 🔁 Empties the entire set
#
# 🔗 Special Set Operations (Between Two Sets)
# These are powerful methods that help compare and combine sets:
# a = {1, 2, 3}
# b = {3, 4, 5}
# a.union(b)         # {1, 2, 3, 4, 5}
# a.intersection(b)  # {3}
# a.difference(b)    # {1, 2}
# a.symmetric_difference(b)  # {1, 2, 4, 5}
#
# Operation               Symbol    Description
# Union                   |         All elements from both sets
# Intersection            &         Common elements only
# Difference              -         Elements in A but not in B
# Symmetric Difference    ^         All elements except the common ones
#
# 📌 When to Use a Set?
# ✅ When you need fast membership testing (e.g., if x in set).
# ✅ When you want to remove duplicates automatically.
# ✅ When performing mathematical set operations like union, intersection, etc.
#
# 🔗 Set Operations in Python
# Python allows us to perform set theory operations between two sets easily using methods and shortcuts (operators).
#
# 📘 Example:
# A = {1, 2, 3}
# B = {3, 4, 5}
#
# ✅ 1. Union — A ∪ B
# Combines all unique elements from both sets.
# A.union(B)        # {1, 2, 3, 4, 5}
# A | B             # Shortcut
#
# ✅ 2. Intersection — A ∩ B
# Returns only the elements common to both sets.
# A.intersection(B) # {3}
# A & B             # Shortcut
#
# ✅ 3. Difference — A - B
# Returns elements that are in A but not in B.
# A.difference(B)   # {1, 2}
# A - B             # Shortcut
#
# ✅ 4. Symmetric Difference — A △ B
# Returns elements that are in A or B, but not in both.
# A.symmetric_difference(B)  # {1, 2, 4, 5}
# A ^ B                      # Shortcut
#
# 📌 Summary Table
# Operation               Method                    Operator Shortcut
# Union                   A.union(B)               A | B
# Intersection            A.intersection(B)        A & B
# Difference (A minus B)  A.difference(B)          A - B
# Symmetric Difference    A.symmetric_difference(B) A ^ B
#
# 💡 Extra Tips:
# You can chain these operations like:
# (A | B) - {1}  # Union of A and B, then remove 1
# Set operations are especially useful in:
# - Filtering values
# - Finding duplicates
# - Comparing user inputs or data sets

# -------------------- DICTIONARIES IN PYTHON --------------------
# 📘 Dictionaries in Python
# A dictionary is a built-in data structure in Python used to store key-value pairs. 
# Think of it like a real-life dictionary — you look up a word (key), and you get its meaning (value).
#
# 🧠 Dictionary Powers
# Feature        Explanation
# Mutable        You can change, add, or remove key-value pairs after creation
# Unique Keys    Each key must be unique; values can be duplicated
# Ordered        Maintains insertion order (since Python 3.7+)
# Heterogeneous  Keys and values can be of different data types
#
# 🛠️ Dictionary Syntax
# student = {
#     "name": "Akarsh",
#     "age": 21,
#     "marks": [85, 90, 95],
#     "details": {"city": "Delhi", "college": "IIT"}
# }
# "name", "age" etc. are keys
# "Akarsh", 21, [85, 90, 95] are values
#
# 🧾 CRUD Operations (Create, Read, Update, Delete)
# # Create/Add
# student["course"] = "Python"
#
# # Read
# print(student["name"])  # Output: Akarsh
#
# # Update
# student["age"] = 22
#
# # Delete
# del student["marks"]
#
# 🔁 Dictionary Traversing
# By Keys (default):
# for key in student:
#     print(key, student[key])
#
# By Keys & Values:
# for key, value in student.items():
#     print(f"{key} -> {value}")
#
# By Values Only:
# for value in student.values():
#     print(value)
#
# 🧰 Useful Dictionary Methods
# Method              Description
# dict.get(key)       Returns value for key, or None if not found
# dict.keys()         Returns a view of all keys
# dict.values()       Returns a view of all values
# dict.items()        Returns a view of (key, value) pairs
# dict.update(other)  Updates dictionary with another
# dict.pop(key)       Removes key and returns its value
# dict.clear()        Removes all items from the dictionary
#
# 🧩 Dictionary Practice Questions
# 🔹 1. Merge Two Dictionaries
# dict1 = {"a": 10, "b": 20}
# dict2 = {"c": 30, "d": 40}
# merged = {**dict1, **dict2}
# print(merged)
#
# 🔹 2. Sum All Values
# data = {"a": 10, "b": 20, "c": 30}
# print(sum(data.values()))  # Output: 60
#
# 🔹 3. Count Frequency of Elements
# elements = ["a", "b", "a", "c", "b", "a"]
# freq = {}
# for item in elements:
#     freq[item] = freq.get(item, 0) + 1
# print(freq)  # {'a': 3, 'b': 2, 'c': 1}
#
# 🔹 4. Combine Two Dictionaries (Add Values for Common Keys)
# dict1 = {"a": 100, "b": 200, "c": 300}
# dict2 = {"a": 300, "b": 200, "d": 400}
# combined = dict1.copy()
# for key, value in dict2.items():
#     combined[key] = combined.get(key, 0) + value
# print(combined)
# # Output: {'a': 400, 'b': 400, 'c': 300, 'd': 400}

# -------------------- EXCEPTION HANDLING IN PYTHON --------------------
# 🛠️ Exception Handling in Python
# 🔹 What is Exception Handling?
# Exception Handling in Python is a mechanism that allows you to gracefully respond to unexpected errors during program execution — rather than crashing the entire program.
# ✅ It helps maintain program stability and user-friendly error messages.
#
# ⚠️ Errors vs. Exceptions
# Type        Description                                    Can Be Handled?
# Errors      Syntax or coding mistakes that prevent code from running.    ❌ No
# Exceptions  Run-time issues that interrupt program execution unexpectedly. ✅ Yes
#
# 🔸 Examples of Errors (Uncatchable)
# Error Type        Example                 Description
# SyntaxError       if True print("Hi")    Missing : or incorrect structure
# IndentationError  Improper indentation    Indentation doesn't match Python rules
# TabError          Mixing tabs and spaces  Using both tabs and spaces for indentation
#
# 🔸 Examples of Exceptions (Catchable)
# Exception Type        When It Occurs
# ZeroDivisionError     Dividing a number by zero
# ValueError           Converting a string to an invalid number
# TypeError            Adding string to an integer
# IndexError           Accessing invalid list index
# KeyError             Accessing non-existent dictionary key
# FileNotFoundError    Trying to open a missing file
#
# 🧱 Keywords in Exception Handling
# Keyword   Purpose
# try       Wrap the block of code that might cause an exception
# except    Handle the exception if it occurs
# else      Executes if no exception occurs in the try block
# finally   Executes always, even if an exception occurs or not
# raise     Manually trigger an exception
#
# 📌 Syntax Template
# try:
#     # Risky code
# except SomeException:
#     # Handle the error
# else:
#     # Run if no error
# finally:
#     # Always runs (cleanup, etc.)
#
# 💡 Example: Full Exception Handling
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("❌ You cannot divide by zero.")
# except ValueError:
#     print("❌ Please enter a valid number.")
# else:
#     print("✅ Result is:", result)
# finally:
#     print("✅ This will always run.")
# Output Cases:
# Input: 0 → Division by zero handled
# Input: abc → ValueError handled
# Input: 5 → Works fine, executes else
# Any case → finally block executes
#
# 🧨 Raising Your Own Exceptions
# You can create your own error conditions using raise.
# age = int(input("Enter your age: "))
# if age < 0:
#     raise ValueError("❌ Age cannot be negative!")
# print("✅ Age is valid.")
#
# ✅ Best Practices
# Practice                    Reason
# Always use specific exceptions    Avoid catching general Exception unless absolutely needed
# Use finally for cleanup          E.g., closing files, releasing resources
# Don't suppress all exceptions    Debugging becomes difficult
# Avoid silent fails               Always log or print something when handling exceptions
#
# 📚 Extra: Multiple Except Blocks
# You can catch different exceptions differently:
# try:
#     with open("file.txt") as f:
#         data = f.read()
# except FileNotFoundError:
#     print("❌ File not found.")
# except PermissionError:
#     print("❌ You don't have permission to read the file.")
# except Exception as e:
#     print("❌ Some other error occurred:", e)
#
# 📎 Summary
# Feature   Use
# try       Wrap code that might crash
# except    Handle known errors
# else      Run when everything goes fine
# finally   Cleanup, close connections, files, etc.
# raise     Create and raise custom error messages
#
# 💡 Practical Examples:
# 🔹 Example 1: Division with Exception Handling
# a = int(input("tell your number :- "))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry there is an err as {err}")
# else:
#     print("good there is no exception")
# finally:
#     print("i will run no matter what")
# print("ok i have done the division")
#
# 🔹 Example 2: Age Validation with Custom Exception
# age = int(input("tell your age :- "))
# try:
#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")
# except Exception as err:
#     print(f"an error occured as {err}")
# print("the club will start soon")

# -------------------- END --------------------

# -------------------- FILE HANDLING IN PYTHON --------------------
# 📂 File Handling in Python
# 📘 What Are Files?
# Files are named storage units on disk that can store data. They come with various extensions:
# .txt → Text file
# .py → Python script
# .csv, .mp3, .json → Others
#
# Python lets us interact with files to Create, Read, Update, and Delete content. 
# This is known as File Handling or CRUD operations.
#
# 🔓 Opening Files in Python
# Use the open() function to work with files:
# file = open("filename.txt", "mode")
#
# Common File Modes
# Mode   Description
# 'r'    Read mode (default) – file must exist
# 'w'    Write mode – creates or overwrites the file
# 'a'    Append mode – adds to the end of the file
# 'x'    Exclusive creation – creates a new file, fails if exists
#
# 🧠 Tip: You can combine these with 'b' (binary) or 't' (text – default), like 'rb', 'wt', etc.
#
# 📖 Reading a File
# f = open("data.txt", "r")
# print(f.read())         # Reads entire file
# f.close()
#
# Useful reading methods:
# f.read()     # Reads entire file as string
# f.readline() # Reads one line
# f.readlines()# Returns a list of all lines
#
# ✍️ Writing to a File
# f = open("data.txt", "w")     # Overwrites if file exists
# f.write("Hello, world!")
# f.close()
#
# Use 'a' mode if you want to append instead of overwrite:
# f = open("data.txt", "a")
# f.write("\nNew line added")
# f.close()
#
# ✅ Best Practice: Using with
# Using with ensures files are closed automatically:
# with open("data.txt", "r") as f:
#     content = f.read()
#     print(content)
# No need for f.close() — Python handles it!
#
# ❌ File Closing Reminder
# If not using with, always close the file manually:
# f = open("file.txt", "r")
# # Do operations
# f.close()  # Important!
#
# 📌 Common Errors in File Handling
# Error               Description
# FileNotFoundError   Trying to read a non-existent file
# PermissionError     No rights to access or modify file
# IsADirectoryError   Provided a folder instead of a file
#
# You can handle these using try-except:
# try:
#     with open("test.txt", "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found!")
#
# 📂 File Object Methods Summary
# Method        Description
# .read()       Reads entire content
# .readline()   Reads one line
# .readlines()  Reads all lines into a list
# .write()      Writes a string
# .writelines() Writes a list of strings
# .seek()       Moves the file pointer
# .tell()       Returns current pointer position
# .close()      Closes the file manually
#
# 🧪 Real-World Use Case
# Let's say you want to create a log file that keeps track of each time your program runs:
# from datetime import datetime
# with open("log.txt", "a") as log:
#     log.write(f"Program run at {datetime.now()}\n")
#
# 🔚 Conclusion
# Use open() with appropriate mode for the task
# Always close files — or better, use with block
# File handling is essential for reading/writing persistent data
# Use exception handling to avoid crashes from file errors

# -------------------- END --------------------

