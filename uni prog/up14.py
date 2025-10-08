# 1. Add
# 2. Search (input→>30)
    # a. Linear 
    # b. binary
# 3. Max
# 4. Min
# 5. Sort
# 6. Exit

print("1. Add")
print("2. Search")
print("3. Max")
print("4. Min")
print("5. Sort")
print("6. Exit")

my_list = []

while True:
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num = int(input("Enter a number to add: "))
        my_list.append(num)
        print(f"{num} added to the list.")
    
    elif choice == 2:
        
        target = int(input("Enter a number to search : "))
        method = input("Enter method (linear/binary): ").strip().lower()
        if method == "linear":
            found = False
            for num in my_list:
                if num == target:
                    found = True
                    break
            if found:
                print(f"{target} found in the list.")
            else:
                print(f"{target} not found in the list.")
        
        elif method == "binary":
            my_list.sort()
            left, right = 0, len(my_list) - 1
            found = False
            
            while left <= right:
                mid = (left + right) // 2
                if my_list[mid] == target:
                    found = True
                    break
                elif my_list[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if found:
                print(f"{target} found in the list.")
            else:
                print(f"{target} not found in the list.")
        
        else:
            print("Invalid method. Please choose 'linear' or 'binary'.")
        # or
        # found = False

        # if target in my_list:
        #     found = True
        
        # if found:
        #     print(f"{target} found in the list.")
        # else:
        #     print(f"{target} not found in the list.")

    elif choice == 3:
        if my_list:
            max = my_list[0]
            for num in my_list:
                if num > max:
                    max = num
            print("Maximum value:", max)
            # or
            # print("Maximum value:", max(my_list))
        else:
            print("List is empty.")
    
    elif choice == 4:
        if my_list:
            min = my_list[0]
            for num in my_list:
                if num < min:
                    min = num
            print("Minimum value:", min)
            # or
            # print("Minimum value:", min(my_list))
        else:
            print("List is empty.")

    elif choice == 5:
        if my_list:
            # Bubble Sort
            for i in range(len(my_list)):
                for j in range(0, len(my_list)-i-1):
                    if my_list[j] > my_list[j+1]:
                        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            print("Sorted List:", my_list)
            # or
            # print("Sorted List:", sorted(my_list)) # returns a new sorted list
            # print("Sorted List:", my_list.sort()  # in-place sort)
        else:
            print("List is empty.")

    elif choice == 6:
        print("Exiting...")
        exit()
    
    else:
        print("Invalid choice. Please try again.")