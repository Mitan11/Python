# Write a Python program to sum all the values in a dictionary?

dic = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50,
}

sum = 0
for i in dic.values():
    sum += i

print(sum)
