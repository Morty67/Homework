# Task 1 Create decorators to count how many times function was called and decorator to register function

def counter_call(func):

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(f'{func.__name__} was called {wrapper.count} times.')
        return res
    wrapper.count = 0
    return wrapper

@counter_call
def my_example1(a: int, b: int):
    return a * b


@counter_call
def my_example2(a: int, b: int):
    return a + b


my_example1(15, 97)
my_example1(17,99)
my_example2(16, 9)
my_example2(76,55)


# Task 2 Create a decorator that will register the function to be decorated in
# list of functions to process the sequence.
#
def my_register(func):
    seq = []
    def decorator():
        seq.append(func)
        return func
    return decorator

@my_register
def res_seq(sequence):
    return sequence

res = my_register(res_seq)

print(res)


# Task 3  Suppose a class has a str method that returns
# a string based on the class. Create a decorator for this method,
# so that the resulting string is saved to a text file whose name is
# matches the name of the class whose method you decorated.

def decor_save_file_to_str(method):

    def wrapper(*args, **kwargs):
        file = f"{method.__qualname__.split('.')[0]}.txt"
        print("create record in", file)
        result = method(*args, **kwargs)
        with open(file, 'a') as f:
            f.write(f'{result}\n')
        return result

    return wrapper


class Family:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @decor_save_file_to_str
    def __str__(self):
        return f'{self.name}  {self.surname}'


husband = Family("Heorhii", "Karabetskyi")
wife = Family("Hanna", "Karabetska")
print(husband)
print(wife)


# Task 4   Create a decorator with parameters to time the job
# one function or another. The parameters should be how many times you need
# run the decorated function and in which file to save the results
# timing. The goal is to time the decorated function.



import time

def time_it(func, run_times: int = 5, file_name: str = "time_example.txt"):
    def wrapper(*args, **kwargs):
        total = 0
        for i in range(run_times):
            start = time.time()
            func(*args, **kwargs)
            finish = time.time()
            total += finish - start
        with open(file_name, 'a') as f:
            f.write(f"{total}")
    return wrapper

@time_it
def add(a: int, b: int):
    return a + b

add(15, 55)
