#Task1

# There are the following sequences of numbers:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Implement a program that displays the next member of this sequence (or similar) on the screen.
# The user enters the sequence from the keyboard as a string. For example, the user enters the string 0,5,10,15,20,25 and the program should respond with the number 30.
def dif(ls):
    diff = ls[1] - ls[0]
    for i in range(len(ls)):
        if ls[i] - ls[i - 1] == diff and i == len(ls) - 1:
            return ls[i] + diff

def x2(ls):
    plural = ls[0] * 2
    for i in range(len(ls)):
        if ls[i] / ls[i - 1] == plural and i == len(ls) - 1:
            return ls[i] * plural

def x3(ls):
    for i in range(len(ls) - 1):
        if ls[i] * 3 == ls[i + 1] and i == len(ls) - 2:
            return ls[i + 1] * 3


def xx2(ls):
    for i in range(len(ls)):
        if (i + 1) ** 2 == ls[i] and i == len(ls) - 1:
            return (i + 2) ** 2


def xx3(ls):
    for i in range(len(ls)):
        if (i + 1) ** 3 == ls[i] and i == len(ls) - 1:
            return (i + 2) ** 3

def main_func(dif,x2, x3, xx2,xx3, ls):
    return dif(ls) or x2(ls) or x3(ls) or xx2(ls) or xx3(ls) or f'Your subsequence is wrong ' \
                                                                f'or I have to make new variations'

ls = list(map(int, list(input('Enter your subsequence: ').replace(',', ' ').split())))

print(main_func(dif,x2,x3,xx2,xx3,ls))
# Task2
# A palindrome number is read the same on both sides (right and left).
# The largest palindrome number obtained by multiplying two two-digit numbers: 9009 = 91 × 99. 
# Find the largest palindrome obtained by multiplying two three-digit numbers.
# Print the value of this palindrome and the vyj;tyyzv of which numbers it is.

first_digit = 0
second_digit = 0
maximum = 0
def my_palindrom(s):
    return str(s) == str(s)[::-1]

def max_palindroms():
    maximum = 0
    for i in range(900, 1000):
        for j in range(900, 1000):
            if my_palindrom((mult := i * j)) and mult > maximum:
                first_digit, second_digit, maximum = i, j, mult
    return f"{first_digit} * {second_digit} = {maximum} is your answer"
print(max_palindroms())
