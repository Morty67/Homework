import math

#Task 1
digits = input('Enter your ticket: ')
len_t = len(my_tuple := tuple(map(int, digits))) // 2
print(not len(digits) % 2 and sum(my_tuple[:len_t]) == sum(my_tuple[len_t:]) and 'Happy ticket' or 'Sorry, next time')
# or
digit = input('Enter your ticket: ')
print(not len(digit) % 2 and int(digit[0]) + int(digit[1]) == int(digit[2]) + int(digit[3])
      and 'Happy ticket' or 'Sorry, next time')

# #Task2
print((text := list(input('Enter your word: ').lower())) == (copy := text[::-1]) and 'Palindrome' or 'NO')

# #Task3

x, y = float(input('x point: ')), float(input('y point: '))
print((hypotenuse := math.sqrt(x ** 2 + y ** 2)) <= 4 and 'Yes' or 'No')



