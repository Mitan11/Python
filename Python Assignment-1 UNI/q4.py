'''4. Take two inputs from the user and display the multiplication tables for all
numbers in that range.
'''

def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()

def multiplication_table_range(start, end):
    for number in range(start, end + 1):
        multiplication_table(number)


start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

multiplication_table_range(start, end)