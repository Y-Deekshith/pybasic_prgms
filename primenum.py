num = int(input("Enter your number :"))

if num <= 0:
    print('Value should be grater than 0')
elif num == 2:
    print("%d is prime number" % num)
else:
    for i in range(2, num):
        if num%i == 0:
            print("%d is not a prime number" % num)
            break
    else:
        print("%d is prime number" % num)

"""
2 3 5 7 11 13 17 19 23 29
"""