        ##Exercise 1 Construct an integer from the string "123"
my_string = '123'
my_int = int(my_string)

        ## Exercise 2 Construct a float from the integer 123
my_float = float(my_int)

        ## Exercise 3 Construct an integer from the float 12.345
my_int = int(12.345)

        ## Exercise 4 Write a Python-script that detects the last 4 digits of a credit card
last_four_difit = int(input('Enter a digits of a credit card: '))
print('Your last four digits: ', last_four_difit % 10000)

        ## Exercise 5 Write a Python-script that calculates the sum of the digits of a three-digit
# number
all_three_digits = 123
print('Sum: ', all_three_digits // 100 + all_three_digits // 10 % 10 + all_three_digits % 10)
        ## Exercise 6 Write a program that calculates and displays the area of a triangle if its sides
# are known
side1, side2, side3 = 3, 4, 5
half_perimeter = int((side1 + side2 + side3) / 2)
print('Area: ', int((half_perimeter * (half_perimeter - side1) *(half_perimeter - side2) * (half_perimeter - side3)) ** 0.5))
        ## Exercise 7 - 9 *Write a Python-script that calculates the sum of the digits of a number 
        #*Determine the number of digits in a number *Print the digits in reverse order

print('Len: ', len(str(all_three_digits)), 'Digits in reverse order:', str(all_three_digits)[::-1], sep='\n')


