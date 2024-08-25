str1 = input("Enter your string : ")


def reverse(str1):
    str2 = ""
    for i in str1:
        str2 = i + str2
    return str2


print(reverse(str1))

"""
or 
str1 = input("Enter your string : ")

def reverse(str1):
    return str1[::-1]

print(reverse(str1))
"""