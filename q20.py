# - Check string is Pallindrome or not 

str = "madam"
rev = ""
temp = str
for i in range(len(str) - 1, -1, -1):
    rev = rev + str[i]
if temp == rev:
    print("String is Pallindrome")
else:
    print("String is not Pallindrome")


