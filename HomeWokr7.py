#Task1
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

#Task2

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

#Task3

text = 'Hello, World'
print(res := {i: text.count(i) for i in text if i.isalpha()})

#Task4
print(set(s := (input('Enter your string: '))) & (set(s1 := input('Enter your 2 string: '))))

#Task5

list_for3 = []
list_for5 = []
for i in range(3, 50):
    if not i % 3:
        list_for3.append(i)
    if not i % 5:
        list_for5.append(i)
print(list_for3, list_for5)
# #Task6
print(res := set(list_for3) & set(list_for5))
