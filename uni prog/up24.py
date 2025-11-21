# 1. add cars
# 2. view cars
# 3. search car by color and price
# 4. update car details
# 5. delete car
# 6. exit


class Car:
    def __init__(self):
        self.no = 0
        self.name = ""
        self.color = ""
        self.price = 0.0

    def add_car(self):
        self.no = int(input("Enter Car No: "))
        self.name = input("Enter Car Name: ")
        self.color = input("Enter Car Color: ")
        self.price = float(input("Enter Car Price: "))

    def display_cars(self):
        print(f"Car No: {self.no}, Name: {self.name}, Color: {self.color}, Price: {self.price}")
    
    def search_car(self, color, price):
        if self.color == color and self.price <= price:
            return True
        return False

    def update_car(self):
        if input("Do you want to Update Car Name? (y/n): ").lower() == 'y':
            self.name = input("Enter new Car Name: ")
        if input("Do you want to Update Car Color? (y/n): ").lower() == 'y':
            self.color = input("Enter new Car Color: ")
        if input("Do you want to Update Car Price? (y/n): ").lower() == 'y':
            self.price = float(input("Enter new Car Price: "))

cars = []

while True:
    print("\nMenu:")
    print("1. Add Car")
    print("2. View Cars")
    print("3. Search Car by Color and Price")
    print("4. Update Car Details")
    print("5. Delete Car")
    print("6. Sort Cars by Price")
    print("7. min price")
    print("8. max price")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")
    if choice == '1':
        car = Car()
        car.add_car()
        cars.append(car)
    elif choice == '2':
        for car in cars:
            car.display_cars()
    
    elif choice == '3':
        color = input("Enter Color to search: ")
        price = float(input("Enter maximum Price: "))
        found = False
        for car in cars:
            if car.search_car(color, price):
                print(f"Found Car")
                car.display_cars()
                found = True
        if not found:
            print("No cars found matching the criteria.")

    elif choice == '4':
        car_no = int(input("Enter Car No to update: "))
        for car in cars:
            if car.no == car_no:
                car.update_car()
                print("Car details updated.")
                break
        else:
            print("Car not found.")
        

    elif choice == '5':
        car_no = int(input("Enter Car No to delete: "))
        for car in cars:
            if car.no == car_no:
                cars.remove(car)
                #pop from delete by index
                print("Car deleted.")
                break
        else:
            print("Car not found.")
    
    elif choice == '6':
        # cars.sort(key=lambda x: x.price)
        # print("Cars sorted by price.")
    # Sort by price using bubble sort
        for i in range(len(cars)):
            for j in range(i+1 , len(cars)):
                if cars[i].price > cars[j].price:
                    cars[i], cars[j] = cars[j], cars[i]
        print("Cars sorted by price.")

        for car in cars:
            car.display_cars()

    elif choice == '7':
        if not cars:
            print("No cars available.")
        else:
            # min_price_car = min(cars, key=lambda x: x.price)
            # print("Car with Minimum Price:")
            # min_price_car.display_cars()
            min_price = cars[0].price
            for car in cars:
                if car.price < min_price:
                    min_price = car.price
            print(f"Minimum price is: {min_price}")

    elif choice == '8':
        if not cars:
            print("No cars available.")
        else:
            # max_price_car = max(cars, key=lambda x: x.price)
            # print("Car with Maximum Price:")
            # max_price_car.display_cars()
            max_price = cars[0].price
            for car in cars:
                if car.price > max_price:
                    max_price = car.price
            print(f"Maximum price is: {max_price}")

    elif choice == '9':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")