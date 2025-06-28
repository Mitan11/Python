# Count all letters, digits, and special symbols from a given string

#  Given: str1 = "P@#yn26at^&i5ve"
#  Expected Outcome:
#  Total counts of chars, digits, and symbols
#  Chars = 8
#  Digits = 3
#  Symbol = 4

str = "P@#yn26at^&i5ve"

count_char = 0
count_digit = 0
count_symbol = 0

for i in str:
    if i.isalpha():
        count_char += 1
    elif i.isdigit():
        count_digit += 1
    else:
        count_symbol += 1

print(f"Total counts of chars: {count_char}")
print(f"Total counts of digits: {count_digit}")
print(f"Total counts of symbols: {count_symbol}")

