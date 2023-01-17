# Task1

def my_progression_fucn(item: int, mul: int, stop: int):
    while item < stop:
        yield item
        item *= mul

result = my_progression_fucn(1, 3, 777)
for item_func in result:
    print(item_func)


# Task2
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


# Task3

def gen_func(item_stopped: int):
    for item in range(2, item_stopped + 1):
        for j in range(2, item):
            if not item % j:
                break
        else:
            yield item


for i in gen_func(27):
    print(i)


# Task4
print(*(gener_list := list(item ** 3 for item in range(1, 23))))