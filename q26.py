# Print positive and negative elements of an List?

lst = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

for i in lst:
    if i > 0:
        print(i, end=" ")
print()
for i in lst:
    if i < 0:
        print(i, end=" ")