
## Exercise 1
# Write a Python-script that displays the message “Hello world

print('Hello, World')

## Exercise 2 Rewrite the first script to display three any messages.

print('Hello, i will learn Python')

### Exercise 3 Write a Python-script to reads values for the length and width of a
# rectangle and returns the area of the rectangle.

len_rec = int(input('Please, enter the length: '))
width_rec = int(input('Please, enter the width: '))
print('Square =', len_rec * width_rec)

## Exercise 4 Write a program that requests the user to enter two numbers and
# prints the sum, product, difference and quotient of the two numbers.


calc1 = int(input('Enter the first number: '))
calc2 = int(input('Enter the second number: '))
print('Sum = ', calc1 + calc2, 'Product = ', calc1 * calc2,
      'Difference = ', calc1 - calc2, 'Quotient =', calc1 / calc2)

## Exercise 5 Write a program that reads in the radius of a circle and prints the
# circle’s diameter, circumference and area. Use the constant value 3.14159 for π.
# Do these calculations in output statements.
rad_circle = int(input('Enter the radius of a circle: '))
pi = 3.14159
print('Сircle’s diameter: ', 2 * rad_circle, 'Circumference: ', 2 * pi * rad_circle,
      'Area: ', pi * rad_circle ** 2)


