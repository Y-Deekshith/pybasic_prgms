num = int(input('Enter your number : '))
fact = 1

if num < 0:
    print("Value cannot be less than 0")
elif num == 0:
    print("Value cannot be 0")
else:
    for i in range(1, num + 1):
        fact = fact * i

print("Factorial of ", num, " is : ", fact)

# 5 - 5*4*3*2*1
