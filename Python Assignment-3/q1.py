''''Write a menu driven python script for managing employee pay roll, which will
allow user to perform following operations:
1. Add Employee (Which will allow user to enter the employee ID, employee
name, employee basic salary)
2. Display gross salary (Which will allow user to enter the employee ID and will
display employee’s gross salary based on following condition)
Gross salary calculation:
If basic salary is below 5000, 10% TA and 10% HRA,
If basic salary is between 5000 and 10000, 8% TA and 8% HRA,
If basic salary is between 10,000 and 20,000, 5% TA and 5% HRA,
If more than 20,000 no TA and DA.
3. Display employees with maximum and minimum salary.
4. Exit'''

employees = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Employee Basic Salary: "))
    employees.append({'id': emp_id, 'name': name, 'basic_salary': basic_salary})

def calculate_gross_salary(basic_salary):
    emp_id = input("Enter Employee ID to calculate gross salary: ")
    for emp in employees:
        if emp['id'] == emp_id:
            basic_salary = emp['basic_salary']
            if basic_salary < 5000:
                ta = 0.10 * basic_salary
                hra = 0.10 * basic_salary
            elif 5000 <= basic_salary < 10000:
                ta = 0.08 * basic_salary
                hra = 0.08 * basic_salary
            elif 10000 <= basic_salary < 20000:
                ta = 0.05 * basic_salary
                hra = 0.05 * basic_salary
            else:
                ta = 0
                hra = 0
            gross_salary = basic_salary + ta + hra
            print(f"Gross Salary of Employee ID {emp_id} is: {gross_salary}")


def display_max_min_salary():
    if not employees:
        print("No employees to display.")
        return
    max_salary = 0
    min_salary = float('inf')
    max_salary_emp = None
    min_salary_emp = None
    for emp in employees:
        if emp['basic_salary'] > max_salary:
            max_salary = emp['basic_salary']
            max_salary_emp = emp
        if emp['basic_salary'] < min_salary:
            min_salary = emp['basic_salary']
            min_salary_emp = emp
    print(f"Employee with Maximum Salary: ID {max_salary_emp['id']}, Name {max_salary_emp['name']}, Salary {max_salary_emp['basic_salary']}")
    print(f"Employee with Minimum Salary: ID {min_salary_emp['id']}, Name {min_salary_emp['name']}, Salary {min_salary_emp['basic_salary']}")

while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Display Gross Salary")
    print("3. Display Employees with Maximum and Minimum Salary")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_employee()
    elif choice == '2':
        calculate_gross_salary(0)
    elif choice == '3':
        display_max_min_salary()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")