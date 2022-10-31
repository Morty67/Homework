#Task 1
n = int(input('Apartment number: '))
entrance = (n + 35) // 36
floor = ((n - 1) // 4 + 1) % 9 or 9
flat_number = n % 4 or 4
print(res := n <= 144 and f'Apartment number: {n}, Entrance:  {entrance} Floor: {floor}, ' \
                    f'and Room on the floor:  {flat_number}' or 'Error')

# #Task 2

year = int(input('Enter, your year: '))
print('Leap year - 366 days' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else '365 - days')


# # Task 3
a, b, c = int(input('First digit: ')), int(input('Second digit: ')), int(input('Third digit: '))
print('Exist' if a < b + c and b < a + c and c < a + b else "Doesn't exist")

