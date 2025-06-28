# Find the greatest element and print its index too?

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

max = lst[0]
index = 0

for i in range(len(lst)):
    if lst[i] > max:
        max = lst[i]
        index = i

print(max, index)
