# Find the second greatest element?

# Find the greatest element and print its index too?

lst = [12,16,13,19,17]

first_max = lst[0]
second_max = 0

for i in range(len(lst)):
    if lst[i] > first_max:
        second_max = first_max
        first_max = lst[i]
    elif lst[i] > second_max :
        second_max = lst[i]

print(first_max ,second_max)
