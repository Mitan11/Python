# Check if List is sorted or not.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(lst) - 1):
    if lst[i] < lst[i + 1]:
        print("List is sorted")
        continue
    else:
        print("List is not sorted")
        break