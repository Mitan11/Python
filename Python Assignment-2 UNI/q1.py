'''Create a dictionary with the name Product.
Take user input for given key value: ProductID, ProductName, Brand, Price, Stock
Create a menu that perform the following task on created dictionary:
1. Display all key-value pairs.
2. Add a new key 'Warranty' with value '2 Years'.
3. Increase 'Price' by 10%.
4. Display the total stock value (Price * Stock).
5. Exit'''

def display_product_info(product):
    for key, value in product.items():
        print(f"{key}: {value}")

def add_warranty(product):
    product['Warranty'] = '2 Years'
    print("Warranty added.")

def increase_price(product):
    product['Price'] *= 1.10
    print("Price increased by 10%.")

def display_total_stock_value(product):
    total_value = product['Price'] * product['Stock']
    print(f"Total Stock Value: {total_value}")

product = {}

# Taking user input for product details
product['ProductID'] = input("Enter Product ID: ")
product['ProductName'] = input("Enter Product Name: ")
product['Brand'] = input("Enter Brand: ")
product['Price'] = float(input("Enter Price: "))
product['Stock'] = int(input("Enter Stock: "))

while True:
    print("\nMenu:")
    print("1. Display all key-value pairs")
    print("2. Add a new key 'Warranty' with value '2 Years'")
    print("3. Increase 'Price' by 10%")
    print("4. Display the total stock value (Price * Stock)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        display_product_info(product)
    elif choice == '2':
        add_warranty(product)
    elif choice == '3':
        increase_price(product)
    elif choice == '4':
        display_total_stock_value(product)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")