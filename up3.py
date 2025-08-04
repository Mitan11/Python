# Calculate h:m:s from number of seconds

seconds = int(input("Enter total seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"{hours} hours : {minutes} minutes : {remaining_seconds} seconds")