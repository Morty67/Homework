from math import pi
import string
import re
# #
# # #Task1
s = 'abcbbbasasbbsdsdsbbbscvbb'
total = 0
for item in s:
    if 'b' in s:
        total += 1
print(total)
#
# #Task2
#
name = input("What's your name?: ")
print(name.isalpha() and name.istitle() and name.capitalize() and 'Yes' or 'No')
#
# #Task3
#
my_str = 'Hi, how are you?'
print(sum([ord(i) for i in my_str]))
#
# #Task4
print(*(round(pi, i) for i in range(2, 12)), sep='\n')

#
# #Task5
task5_str = input('Enter your string: ')
print(max(task5_str.split(), key=len))

# #Task6

res = len(re.match(r'(.+?)\1*$', (s := input('What Vova wrote?: ').lower())).group(1))
print(s[:res])


#Task7

text = """<div> <h1>Hi</h1><p> Phyton </p><a href="">how are you? </a></div>"""
print(re.sub(r'<.*?>', '', text))
