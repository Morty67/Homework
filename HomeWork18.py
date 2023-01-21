# Task1

def my_gen_func(num: int = 1, count: int = 5, func_from_user: object = None):

    index = 1
    while index <= count:
        yield func_from_user(num)
        num += 1
        index += 1
    return


def func_from_user(num):
    return num ** 3


for item in my_gen_func(1, 15, func_from_user):
    print(item)



# Task2

from timeit import timeit

temp1_rec = """
def fib_rec(num_rec: int):
    if num_rec in (1, 2):
        return 1
    return fib_rec(num_rec - 1) + fib_rec(num_rec - 2)
"""


temp2_mem = """
def fib_mem(num_mem):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = num_mem(*args)
            return cache[args]
    return decorate

"""
print(f'Time for recursion - {timeit(temp1_rec, number=20)}')
print(f'Time for memoization - {timeit(temp2_mem, number=20)}')


# Task3

def seq(my_list: list, user_func):
    res = []
    for_res = [res.append(item) for item in my_list if user_func(item)]
    return sum(res)


my_seq = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

print(seq(my_seq, lambda x: not x % 2))




