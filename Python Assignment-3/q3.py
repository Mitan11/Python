'''Write a menu driven python script for managing score of cricketer, which will
allow user to perform following operations:
1. Add cricketer (Which will allow user to enter the details of cricketer like,
cricketer no, name, total runs scored, and total wickets taken)
2. Display cricketer whose name starts with ‘S’ and wickets more than 3.
3. Display man of the match based on highest score.
4. Exit'''

cricketers = []

def add_cricketer():
    cricketer_no = input("Enter Cricketer No: ")
    name = input("Enter Cricketer Name: ")
    total_runs = int(input("Enter Total Runs Scored: "))
    total_wickets = int(input("Enter Total Wickets Taken: "))
    cricketers.append({'no': cricketer_no, 'name': name, 'runs': total_runs, 'wickets': total_wickets})

def display_s_wicket_takers():
    print("Cricketers whose name starts with 'S' and wickets more than 3:")
    for cricketer in cricketers:
        if cricketer['name'].startswith('S') and cricketer['wickets'] > 3:
            print(f"Cricketer No: {cricketer['no']}, Name: {cricketer['name']}, Runs: {cricketer['runs']}, Wickets: {cricketer['wickets']}")

def display_man_of_the_match():
    man_of_the_match = 0
    best_cricketer = None
    for cricketer in cricketers:
        if cricketer['runs'] > man_of_the_match:
            man_of_the_match = cricketer['runs']
            best_cricketer = cricketer
    print(f"Man of the Match: Cricketer No: {best_cricketer['no']}, Name: {best_cricketer['name']}, Runs: {best_cricketer['runs']}, Wickets: {best_cricketer['wickets']}")


while True:
    print("\nMenu:")
    print("1. Add Cricketer")
    print("2. Display cricketer whose name starts with 'S' and wickets more than 3")
    print("3. Display man of the match based on highest score")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add_cricketer()
    elif choice == '2':
        display_s_wicket_takers()
    elif choice == '3':
        display_man_of_the_match()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")