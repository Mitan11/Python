# Reverse a string without using in build functions.4

str = "Hello World"
rev = ""

for i in range(len(str) - 1, -1, -1):
    rev = rev + str[i]
print(rev)