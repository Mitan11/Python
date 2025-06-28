# Write a Python script to merge two Python dictionaries?

dic = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50,
}

dic2 = {
    "f": 60,
    "g": 70,
    "h": 80,
    "i": 90,
}

merged = {**dic, **dic2}

print(merged)
