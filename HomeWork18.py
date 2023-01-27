# Task1 Implement a generator function that will return one member of a numerical sequence, the law of which is specified using a user function.
# In addition, the parameters of the generator function must be the value of the first term of the progression and the number of terms produced by the sequence.
# The generator must stop its work either when the nth term is reached or when the command to end is sent.

def my_gen_func(num: int = 1, count: int = 5, func_from_user: object = None):

    index = 1
    while index <= count:
        yield func_from_user(num)
        num += 1
        index += 1


def func_from_user(num):
    return num ** 3


for item in my_gen_func(1, 15, func_from_user):
    print(item)



# Task2 Using closures, implement such a programming technique as Memoization
# Use the resulting mechanism to speed up the function of recursively calculating the nth term of the Fibonacci series.
# Compare the speed of execution with a simple recursive approach.

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


# Task3 Write a function that applies an arbitrary user-defined function to a list of numbers and returns the sum of the elements of the resulting list.

def seq(my_list: list, user_func):
    res = (item for item in my_list if user_func(item))
    return sum(res)


my_seq = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

print(seq(my_seq, lambda x: not x % 2))




