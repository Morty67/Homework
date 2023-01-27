#Task1 Using a dictionary, write a program that displays the name of the day of the week by number.
# For example, 1 is "Monday".
weeks = {
         1: 'Monday',
         2: 'Tuesday',
         3: 'Wednesday',
         4: 'Thusday',
         5: 'Friday',
         6: 'Saturday',
         7: 'Sunday',
         }
print(weeks.get((x := int(input('What day you need:? '))), 'Error, only 1-7'))
 
#Task2 Describe a cat (pet) using a dictionary.

my_cat = {
    'name': 'Snuffles',
    'breed': 'scottish fold',
    'looks like':'predator',
    'characteristic': {
        'body size': 'tiny',
        'upbringing': 'tame',
        'hair color': 'gray',
        'character': 'independent',
    }
}

#Task3  Write a program that reads a string of text from the keyboard and displays statistics on how many times each letter appears in this string.
# For example, for the string "Hello world" this statistics looks like this: "H" - 1, "e" - 1, "l" - 3, etc.

text = 'Hello, World'
print(res := {i: text.count(i) for i in text if i.isalpha()})

#Task4 Write a program that reads two lines of text from the keyboard and displays the letters that appear simultaneously in the first and second lines. 
# For example, for the strings "Hello" and "World", the letters "l" and "o" should appear on the screen.
print(set(s := (input('Enter your string: '))) & (set(s1 := input('Enter your 2 string: '))))

#Task5 Write a program that will generate two lists. One with numbers in multiples of 3, the other with numbers in multiples of 5.

list_for3 = []
list_for5 = []
for i in range(3, 50):
    if not i % 3:
        list_for3.append(i)
    if not i % 5:
        list_for5.append(i)
print(list_for3, list_for5)
# #Task6 Create a list with numbers that appear in both lists.
print(res := set(list_for3) & set(list_for5))
