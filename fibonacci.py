num = int(input('Enter your value : '))

x = 0
y = 1
count = 2

if num <= 0:
    print('Value should be grater than 0')
elif num == 1:
    print(y)
else:
    print(x, "", y, end=" ")
    while num > count:
        z = x + y
        print(z, end=' ')
        x = y
        y = z
        count = count + 1

"""
7 - 0 1 1 2 3 5 8
"""
