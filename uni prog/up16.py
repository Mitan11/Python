# print elements divisible with all 1 to 20 
num = 1
while True:
        for i in range(2, 10):
            if num % i != 0:
                # print(num)
                break
            else:    
                print(num)
                exit()
        num += 1