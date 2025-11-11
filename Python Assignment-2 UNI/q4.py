'''Create a dictionary Employee with the following details:
Take user input for Key - Value of EmpID, Name, Gender, BasicSalary, HRA and DA.
Create the following menu and perform the following tasks on created dictionary:
 1. Display all details of the employee in proper format.
 2. Calculate Net Salary and add that net salary as key in employee dictionary
 Formula:
 Net Salary = Basic + HRA + DA
 Calculate HRA % and DA % on the basis of Basic salary.
 3. Remove Only Gender key from dictionary.
 4. Exit
'''

employee = {}

employee['EmpID'] = input("Enter Employee ID: ")
employee['Name'] = int(input("Enter Employee Name: "))
employee['Gender'] = input("Enter Gender: ")
employee['BasicSalary'] = float(input("Enter Basic Salary: "))
employee['HRA'] = float(input("Enter HRA: "))
employee['DA'] = float(input("Enter DA: "))

while True:
    print("\nMenu:")
    print("1. Display all details of the employee in proper format")
    print("2. Calculate Net Salary and add that net salary as key in employee dictionary")
    print("3. Remove Only Gender key from dictionary")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\nEmployee Details:")
        for key, value in employee.items():
            print(f"  {key}: {value}")

    elif choice == '2':
        net_salary = employee['BasicSalary'] + employee['HRA'] + employee['DA']
        employee['NetSalary'] = net_salary
        employee['HRA%'] = (employee['HRA'] / employee['BasicSalary']) * 100
        employee['DA%'] = (employee['DA'] / employee['BasicSalary']) * 100
        print(f"Net Salary calculated and added to employee dictionary.")

    elif choice == '3':
        employee.pop('Gender', None)
        print(f"Gender key removed from employee dictionary.")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")