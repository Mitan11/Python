'''Perform following in python using the concept of List:
Create two list days and temperature and take input from user like following data for both list.
You are given the weekly temperature readings (in °C) for a city:
days = Mon, Tue, Wed, Thu, Fri, Sat, Sun
temperature = 32, 35, 31, 30, 33, 36, 34
Create a menu and perform the following tasks:
1. Display temperature with day in proper format.
1. Find the highest and lowest temperature of the week.
2. Calculate the average temperature.
3. Count the number of days when temperature was above 33°C.
4. Exit'''

def display_temperatures(days, temperature):
    print("Day\tTemperature (°C)")
    for day, temp in zip(days, temperature):
        print(f"{day}\t{temp}")

def find_highest_lowest(temperature):
    highest = max(temperature)
    lowest = min(temperature)
    print(f"Highest Temperature: {highest}°C")
    print(f"Lowest Temperature: {lowest}°C")

def avg(temperature):
    average = sum(temperature) / len(temperature)
    print(f"Average Temperature: {average:.2f}°C")

def count_days_above_threshold(temperature, threshold=33):
    count = 0
    for temp in temperature:
        if temp > threshold:
            count += 1
    print(f"Number of days above {threshold}°C: {count}")

days = []
temperature = []

# Taking user input for days and temperature
for i in range(7):
    day = input(f"Enter day {i+1} (e.g., Mon, Tue): ")
    temp = float(input(f"Enter temperature for {day} (in °C): "))
    days.append(day)
    temperature.append(temp)

while True:
    print("\nMenu:")
    print("1. Display temperature with day in proper format")
    print("2. Find the highest and lowest temperature of the week")
    print("3. Calculate the average temperature")
    print("4. Count the number of days when temperature was above 33°C")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_temperatures(days, temperature)

    elif choice == '2':
        find_highest_lowest(temperature)

    elif choice == '3':
        avg(temperature)

    elif choice == '4':
        count_days_above_threshold(temperature)

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print