# Accept a year and check if it a leap year or not

year =  int(input("Enter a year : "))

if(year % 4 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")