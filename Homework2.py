        ##Exercise 1
my_string = '123'
my_int = int(my_string)

        ## Exercise 2
my_float = float(my_int)

        ## Exercise 3
my_int = int(12.345)

        ## Exercise 4
last_four_difit = int(input('Enter a digits of a credit card: '))
print('Your last four digits: ', last_four_difit % 10000)

        ## Exercise 5
all_three_digits = 123
print('Sum: ', all_three_digits // 100 + all_three_digits // 10 % 10 + all_three_digits % 10)
        ## Exercise 6
side1, side2, side3 = 3, 4, 5
half_perimeter = int((side1 + side2 + side3) / 2)
print('Area: ', int((half_perimeter * (half_perimeter - side1) *(half_perimeter - side2) * (half_perimeter - side3)) ** 0.5))
        ## Exercise 7 - 9
#Завдання 7 я би скопіював як завдання № 5, сенс той самий.
print('Len: ', len(str(all_three_digits)), 'Digits in reverse order:', str(all_three_digits)[::-1], sep='\n')


