import string
#Task1 Implement a function whose parameters are two numbers and a string. It returns the concatenation of the string with the sum of numbers.

def func(a, b, c):
    return str(a + b) + c
print(func(int(input('a: ')), int(input('b: ')), input('c: ')))

#Task2 Implement a function that draws a rectangle of asterisks "*" on the screen. Its parameters will be integers that describe the length and width of the rectangle.
def rectangle(height, len_of_rectangle):
    return f"{'*' * len_of_rectangle} \n" + \
    f'*{" " * (len_of_rectangle - 2)}*\n' * (height - 2) + \
    '*' * len_of_rectangle

print(rectangle((int(input('height: '))), int(input('len: '))))


#Task3 Write a function that implements a linear search for an element in a list of integers. 
# If there is such an element in the list, return the index, if not, return the number "-1".
#
def search(my_list, search):
    for _ in my_list:
        if search in my_list:
            return my_list[search]
    return -1

print(search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9))


#Task4  Write a function that returns the number of words in a text string.
def my_len(text):
    for item in string.punctuation:
        if item in text:
            text = text.replace(item, '')
    return len(text.split())
   # return len([item for item in text.split()])


print(my_len(input('Enter your text: ')))

#Task6 6 Write a function that converts an integer from Roman to decimal.
# For example: XXII -> 22
def roman(digit):
    my_dict6 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    last_digit = digit[-1]
    result = my_dict6[last_digit]
    for i in digit[-2::-1]:
        if my_dict6[i] >= my_dict6[last_digit]:
            result += my_dict6[i]
        else:
            result -= my_dict6[i]
        last_digit = i
    return f'Your roman numeral is: {result}'
print(roman(input('Enter a Roman numeral: ')))
