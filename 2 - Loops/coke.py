sum = 0
while(sum<50):

    while True:
        print("Amount due: ", 50-sum)
        coin = int(input("Insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            break

    sum += coin 

print("You are due: ", sum-50)
