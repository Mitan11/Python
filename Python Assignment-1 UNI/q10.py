'''10. Read two numbers from user and print all Armstrong numbers between two
numbers.'''

def is_armstrong(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** 3
        num //= 10
    return sum


def armstrong_between(start, end):
    for num in range(start, end + 1):
        armstrong = is_armstrong(num) 
        if num == armstrong :
            print(num, end=' ')

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
armstrong_between(start, end)