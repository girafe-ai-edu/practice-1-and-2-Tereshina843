# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
number = input('Write an integer 4-digit number: ')
sum = 0
for num in number:
    sum += int(num)
print(sum)
