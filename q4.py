# Accept the gender from the user as char and print the 
# respective greeting message
# Ex - Good Morning Sir (on the basis of gender)

gender = input("Enter your gender (M/F): ")

if gender.upper() == 'M':
    print("Good Morning Sir")
else:
    print("Good Morning Ma'am")