import math

# #Task 1 A number (four digits) is given. Check if it is a "lucky ticket".
# Note: A lucky ticket is a number in which, for an even number of digits, the sum of the digits of its left half is equal to the sum of the digits of its right half.
# For example, 1322 is a lucky ticket because 1 + 3 = 2 + 2.
digits = input('Enter your ticket: ')
len_t = len(my_tuple := tuple(map(int, digits))) // 2
print(not len(digits) % 2 and sum(my_tuple[:len_t]) == sum(my_tuple[len_t:]) and 'Happy ticket' or 'Sorry, next time')
# or
digit = input('Enter your ticket: ')
print(not len(digit) % 2 and int(digit[0]) + int(digit[1]) == int(digit[2]) + int(digit[3])
      and 'Happy ticket' or 'Sorry, next time')

# #Task2 
# Enter a number (six digits) from the keyboard. Check if it is a palindrome.
# Note: A palindrome is a number, word, or text that reads the same from left to right and right to left.
# For example, these are the numbers 143341, 5555, 7117, etc.
print((text := list(input('Enter your word: ').lower())) == (copy := text[::-1]) and 'Palindrome' or 'NO')

# #Task3
# Given a circle with center at the origin and radius 4. The user enters the coordinates of the point x and y from the keyboard.
# Write a program to determine whether this point is inside the circle or not.
x, y = float(input('x point: ')), float(input('y point: '))
print((hypotenuse := math.sqrt(x ** 2 + y ** 2)) <= 4 and 'Yes' or 'No')



