        # 1. Write a Python program to print the number entered by user only if the
#number entered is negative.
print(int(input('Enter your digits')) < 0)

        #2. Write a Python program to check if the value a is less than 20 or not

print(not (a := int(input('Enter digit - A: '))) >= (b := 20))


        # 3. Write a Python program to check if a given number is Zero or Not.

print(not (n := int(input('Enter your digit: '))))


        #4. Write a Python program to check if a given number is Even or Odd.

print(not (digit := int(input('Enter your digit: '))) % 2 and 'Even' or 'Odd')

        #5. Write a Python program to find largest number among three numbers
        #entered by user.

n1, n2, n3 = int(input('First digit: ')), int(input('Second digit: ')),int(input('Third digit: '))
print(max(n1, n2, n3))
