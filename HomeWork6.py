from math import pi
import string
import re
# #
# # #Task1 Write a program that counts the number of letters "b" in the given line of text.

s = 'abcbbbasasbbsdsdsbbbscvbb'
total = 0
for item in s:
    if 'b' in s:
        total += 1
print(total)
#
# #Task2 The user enters a person's name from the keyboard. Write a program to check the entered name for validity (it means that,
# for example, a person's name cannot contain numbers, it must begin with a capital letter followed by lowercase letters).

name = input("What's your name?: ")
print(name.isalpha() and name.istitle() and name.capitalize() and 'Yes' or 'No')
#
# #Task3 Write a program that calculates the sum of all character codes of a string.
my_str = 'Hi, how are you?'
print(sum([ord(i) for i in my_str]))
#
# #Task4 Print 10 lines with the value of Pi. The first line should have 2 decimal places, the second line should have 3 decimal places, and so on.
print(*(round(pi, i) for i in range(2, 12)), sep='\n')

#
# #Task5 The user enters text from the keyboard. Find the longest word in it and display it on the screen.
task5_str = input('Enter your string: ')
print(max(task5_str.split(), key=len))

# #Task6
# Vovochka, sitting in class, wrote the same words in a row (a word can consist of one letter). When Maria Ivanovna took away his notebook, there was only one line of text.
# Write a program that will determine the shortest word Vovochka wrote. For example:
# aaaaaaa - Vovochka wrote the word "a"
# ititititit - Vovochka wrote the word "it"
# catcatcatcat - Vovochka wrote the word "cat"

res = len(re.match(r'(.+?)\1*$', (s := input('What Vova wrote?: ').lower())).group(1))
print(s[:res])


#Task7

text = """<div> <h1>Hi</h1><p> Phyton </p><a href="">how are you? </a></div>"""
print(re.sub(r'<.*?>', '', text))
