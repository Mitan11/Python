# Electricity Bill Calculator
# First 100 units are free

# Next 100 units = ₹5/unit

# Beyond 200 units = ₹10/unit

units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + ((units - 200) * 10)

print(f"Electricity bill: ₹{bill}")