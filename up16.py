# print elements divisible with all 1 to 20 
while True:
    for j in range(1 , 100000):
        for i in range(2, 10):
            if j % i != 0:
                break
        else:    
            print(j)
            exit()
