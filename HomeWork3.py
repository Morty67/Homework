#Task 1.
# There is a nine-story building with 4 entrances. The entrance number starts with one. There are 4 apartments on one floor. 
# Write a program that receives the apartment number from the user and displays the entrance number, floor and number on the floor for a given apartment. 
# If there is no such apartment in this building, then you must inform the user about it.
# ( do not use if )

n = int(input('Apartment number: '))
entrance = (n + 35) // 36
floor = ((n - 1) // 4 + 1) % 9 or 9
flat_number = n % 4 or 4
print(res := n <= 144 and f'Apartment number: {n}, Entrance:  {entrance} Floor: {floor}, ' \
                    f'and Room on the floor:  {flat_number}' or 'Error')

# #Task 2
# Write a program that will return the number of days for a given year. 
# The year is a leap year if it is a multiple of 4, but not a multiple of 100, and also if it is a multiple of 400

year = int(input('Enter, your year: '))
print('Leap year - 366 days' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else '365 - days')


# # Task 3
# A triangle exists only if the sum of any two sides is greater than the third. Given: A, B, C are the sides of a triangle. 
# Write a program that indicates whether such a triangle exists.

a, b, c = int(input('First digit: ')), int(input('Second digit: ')), int(input('Third digit: '))
print('Exist' if a < b + c and b < a + c and c < a + b else "Doesn't exist")

