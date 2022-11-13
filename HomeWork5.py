from random import randint
#Exercise 1

print([i for i in range(1, 101) if not i % 7])

#Exercise 2

f = 1
for i in range(1, (n := int(input('Digit for factorial: ')) + 1)):
    f *= i
print(f'Factorial of {n} is {f}')
#Exercise 3

for i in range(1, 6):
    print(f'{i} x 5 = {i * 5}')
#Exercise 4
#
height = int(input())
len_of_rectangle = int(input())

for i in range(1, height + 1):
    if i == 1 or i == height:
        print('*' * len_of_rectangle)
    else:
        print('*' + ' ' * (len_of_rectangle - 2) + '*')
#Exercise 5

count = 0
len_list = []
for i in (my_list := [0, 5, 2, 4, 7, 1, 3, 19]):
    if i % 2:
        len_list.append(i)
print(len_list, len(len_list))

#Exercise 6

lst = [randint(1, 10) for i in range(4)]
my_lst = []
for i in lst:
    my_lst.append(i * 2)
print(new_list := lst + my_lst)

#Exercise 7
salary_lst = [randint(20_000, 25_000) for i in range(12)]
print(int(sum(salary_lst) / len(salary_lst)))

# #Exercise 8
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

#Exercise 9
my_list9 = [7, 2, 9, 4]
for i in reversed(my_list9):
    print(i, end=' ')
#
# #Exercise 10
my_list10 = []
for i in range(2, 101):
    for j in range(2, i):
        if not i % j:
            break
    else:
        my_list10.append(i)
print(*my_list10)

# #Exercise 11
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
