'''Perform following in python with the concept of Tuple:
Create following tuple which store product related details.
Create four different tuple: productId, Name, Price and Stock.
Take all tuple values from user like following:
product_ids = 101, 102, 103, 104
product_names = Pen, Pencil, Notebook, Eraser
prices = 10, 5, 50, 8
stock = 50, 100, 40, 60
Create a menu and perform the following tasks:
1. Display all products in single format like: Product_ID, Name, Price, Stock, Total_Value
2. Calculate total value of each product = price * stock and store in a tuple TotalValue and display
3. Find and display the product with the highest total value
4. Exit
'''

def display_products(product_ids, product_names, prices, stocks):
    print("Product_ID\tName\tPrice\tStock\tTotal_Value")
    for i in range(len(product_ids)):
        total_value = prices[i] * stocks[i]
        print(f"{product_ids[i]}\t\t{product_names[i]}\t{prices[i]}\t{stocks[i]}\t{total_value}")

def calculate_total_values(prices, stocks):
    """Return a tuple with total value per product (price * stock) in order."""
    total_values = ()
    for i in range(len(prices)):
        total_values += (prices[i] * stocks[i],)
    return total_values

def find_highest_total_value(product_ids, product_names, prices, stocks):
    highest_value = 0
    highest_product = ()
    for i in range(len(product_ids)):
        total_value = prices[i] * stocks[i]
        if total_value > highest_value:
            highest_value = total_value
            highest_product = (product_ids[i], product_names[i], prices[i], stocks[i], total_value)
    print("Product with Highest Total Value:")
    print(f"Product_ID: {highest_product[0]}, Name: {highest_product[1]}, Price: {highest_product[2]}, Stock: {highest_product[3]}, Total_Value: {highest_product[4]}")

product_ids = ()
product_names = ()
prices = ()
stocks = ()

# Taking user input for product details
while True:
    print("Enter product details (or type 'done' to finish):")
    pid = input("Enter Product ID: ")
    if pid.lower() == 'done':
        break
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    qty = int(input("Enter Stock: "))
    
    product_ids += (pid,)
    product_names += (name,)
    prices += (price,)
    stocks += (qty,)

while True:
    print("\nMenu:")
    print("1. Display all products in single format")
    print("2. Calculate total value of each product and display")
    print("3. Find and display the product with the highest total value")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        display_products(product_ids, product_names, prices, stocks)
    elif choice == '2':
        total_values = calculate_total_values(prices, stocks)
        print("Total Value per product (price * stock):")
        # Show as tuple and also aligned with products
        print(total_values)
        for i in range(len(product_ids)):
            print(f"{product_ids[i]} - {product_names[i]}: {prices[i]} x {stocks[i]} = {total_values[i]}")
    elif choice == '3':
        find_highest_total_value(product_ids, product_names, prices, stocks)

    elif choice == '4':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please try again.")