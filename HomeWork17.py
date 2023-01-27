# Task1  Implement a generator function that returns one term of a geometric progression with the specified multiplier.
# The generator should stop its work either when it reaches the specified element or when a command is passed to end.

def my_progression_fucn(item: int, mul: int, stop: int):
    while item < stop:
        yield item
        item *= mul

result = my_progression_fucn(1, 3, 777)
for item_func in result:
    print(item_func)


# Task2 Implement your own analog of the range() generator function.
def range_func(start: int, stop: int, step: int) -> list:

    res = []
    if not isinstance(start, int):
        raise TypeError('Start must be only int item')
    if not isinstance(stop, int):
        raise TypeError('Stop must be only int item')
    if not isinstance(step, int):
        raise TypeError('Step must be only int item')
    while start < stop:
        res.append(start)
        if step:
            start += 1
        start += step
    return res


print(range_func(-2, 27, 3))


# Task 3 Write a generator function that returns prime numbers. The upper bound of the range must be specified by a parameter of this function.

def gen_func(item_stopped: int):
    for item in range(2, item_stopped + 1):
        for j in range(2, item):
            if not item % j:
                break
        else:
            yield item


for i in gen_func(27):
    print(i)


# Task 4  Write a generator expression to fill the list. The list should be filled with cubes of numbers from 2 to the value you specify.

print(*(gener_list := list(item ** 3 for item in range(1, 23))))
