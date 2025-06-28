# Write a Python program to combine two dictionary by adding values for common keys

dic1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50,
}

dic2 = {
    "a": 10,
}

for i in dic2.keys():
    if i in dic1.keys():
        dic1[i] = dic1[i] + dic2[i]
    else:
        dic1[i] = dic2[i] 

print(dic1)




