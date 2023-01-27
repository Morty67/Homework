from random import randint
#Exercise 1 Write a Python script that displays all numbers in the range from 1 to 100 multiples of 7.

print([i for i in range(1, 101) if not i % 7])

#Exercise 2 Write a Python script that calculates the factorial of the number n (n is entered from the keyboard) using a loop.

f = 1
for i in range(1, (n := int(input('Digit for factorial: ')) + 1)):
    f *= i
print(f'Factorial of {n} is {f}')
#Exercise 3  Write a Python script that displays the multiplication table by 5. Preferably print 1 x 5 = 5, 2 x 5 = 10, not just 5, 10, ...

for i in range(1, 6):
    print(f'{i} x 5 = {i * 5}')
#Exercise 4 Write a Python script that displays a rectangle with '*' on the screen. The height and width of the rectangle are entered from the keyboard.  For example, below is a rectangle with a height of 4 and a width of 5.
# *****
# *   *
# *   *
# *****
#
height = int(input())
len_of_rectangle = int(input())

for i in range(1, height + 1):
    if i == 1 or i == height:
        print('*' * len_of_rectangle)
    else:
        print('*' + ' ' * (len_of_rectangle - 2) + '*')
#Exercise 5 You have a list [0,5,2,4,7,1,3,19]. Write a Python script to count the odd digits in it.

count = 0
len_list = []
for i in (my_list := [0, 5, 2, 4, 7, 1, 3, 19]):
    if i % 2:
        len_list.append(i)
print(len_list, len(len_list))

#Exercise 6
# Create a list of random numbers (4 elements long). Create a second list twice as large as the first, where the first 4 elements should be equal to the elements of the first list, and the remaining elements should be twice the value of the original ones.
# For example,
# Was → [1,4,7,2]
# Became → [1,4,7,2,2,8,14,4]

lst = [randint(1, 10) for i in range(4)]
my_lst = []
for i in lst:
    my_lst.append(i * 2)
print(new_list := lst + my_lst)

#Exercise 7
# Create a list of 12 items. Each item in this list is the employee's salary for the month. Display this list on the screen and calculate the average monthly salary of this employee.

salary_lst = [randint(20_000, 25_000) for i in range(12)]
print(int(sum(salary_lst) / len(salary_lst)))

# #Exercise 8
# Given a matrix
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [9,10, 11, 12]
# [13,14, 15, 16]
# Write a Python script that displays this matrix on the screen, calculates and prints the sum of the elements of this matrix.
my_matrix = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
total_of_matrix = 0
for i in range(len(my_matrix)):
    for j in range(len(my_matrix[i])):
        total_of_matrix += my_matrix[i][j]
        print(my_matrix[i][j], end=' ')
    print()
print(total_of_matrix)

#Exercise 9 Write a code to mirror the list [7,2,9,4] -> [4,9,2,7].
# The list can be of any length.
my_list9 = [7, 2, 9, 4]
for i in reversed(my_list9):
    print(i, end=' ')
# 
# #Exercise 10  Use loops to print all primes from 1 to 100.
my_list10 = []
for i in range(2, 101):
    for j in range(2, i):
        if not i % j:
            break
    else:
        my_list10.append(i)
print(*my_list10)

# #Exercise 11 

# Display an hourglass with the maximum width read from the keyboard (odd number). In the example, the width is 5.
# *****
#  ***
#   *
#  ***
# *****
n = int(input('Digit: '))
if not n % 2:
    print('Only Odd')
else:
    for i in range(n, 0, -2):
        empty = n - i
        print(' ' * ((n - i) // 2), '*' * i)
    for j in range(3, n + 1, 2):
        empty = n - j
        print(' ' * ((n - j) // 2), '*' * j)
