str1 = str(input("enter your 1st string : "))
str2 = str(input("enter your 2st string : "))

print('Strings before swapping : ' + str1 + " " + str2)

str1 = str1 + str2

str2 = str1[0:(len(str1)) - (len(str2))]

str1 = str1[len(str2):]

print('Strings after swapping : ' + str1 + " " + str2)

"""
Swap 2 strings without 3rd variable
"""