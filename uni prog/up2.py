# Print 59.47 as Rs 59 and 47 paisa

amount = 59.47
rupees = int(amount)
paisa = int(round((amount - rupees) * 100))
print(f"Rs {rupees} and {paisa} paisa")
