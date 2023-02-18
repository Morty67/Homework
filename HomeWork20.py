# Task 1 Create a decorator that registers the class to be decorated in the
# class list.
def class_reg(cls):
    classes = getattr(class_reg, "classes", [])
    classes.append(cls)
    setattr(class_reg, "classes", classes)
    return cls


@class_reg
class Example:
    pass


#

# Task2 Create a class decorator with a parameter. The parameter should be
# a string which should be appended (on the left) to the result of
# __str__.


class ClassDecorator:
    def __init__(self, string):
        self.string = string

    def __call__(self, item):
        item.__str__ = self.decorate(item.__str__)
        return item

    def decorate(self, func):
        def wrapper(*args, **kwargs):
            return self.string + func(*args, **kwargs)

        return wrapper


@ClassDecorator("Hi,")
class Example:
    def __str__(self):
        return " Prog"


print(Example())


# Task 3 For the Box class, write a static method that will calculate
# the total volume of two boxes, which will be its parameters.
#
class Box:
    def __init__(self, box1, box2):
        self.box1 = box1
        self.box2 = box2
        self.box_volume = self.total_volume(box1, box2)

    @staticmethod
    def total_volume(box1, box2):
        return box1 + box2

    def __str__(self):
        return f"{self.box1} + {self.box2}"


box1 = Box(3, 5)
print(box1)
print(box1.total_volume(10, 15))


# Task 4 Create a descriptor that will make the fields of the class it manages
# Read-only fields of the class it manages.
class Example:
    def __init__(self):
        self.__only_read = "only for read"

    @property
    def read_only(self):
        return self.__only_read


x = Example()
print(x.read_only)

# Task 5 Implement a functionality that will prohibit setting the class fields
# with any values other than integers. That is, if one or another field
# for example, a string, an exception should be thrown.
# exception.


class Example:
    def __init__(self, item):
        self.item = item

    def __setattr__(self, key, value):
        if not isinstance(value, int):
            raise AttributeError("Must be only int")
        else:
            self.__dict__[key] = value

    def __str__(self):
        return f"{self.item}"


res = Example(1)
res_failed = Example(1.5)
print(res)
print(res_failed)

# Task 6 Implement a class property that has the following
# functionality: when you set the value of this property to a file with a predefined name
# file with a predefined name, the time (when you set
# value of the property) and the set value should be saved.
import datetime


class Exp:
    def __init__(self, item, key):
        self.item = item
        self.key = key

    def get_item(self):
        return self.item

    def set_item(self, item):
        with open("time_rec.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} \n")
        self.item = item

    def __str__(self):
        return f"{self.item}"

    my_prop = property(get_item, set_item)


exp_example = Exp(1, 2)
exp_example.my_prop = 10


# Task 7 Implement a metaclass that has the following functionality: when
# It is used to save the class name to a file with a predefined name.
# The name of the class and the list of its fields should be saved to a file with a predefined name.


class SaveMeta(type):
    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        return new_class

    def __init__(cls, name, bases, dct) -> None:
        with open("metaone.txt", "w") as file_writer:
            file_writer.write(f"{name} {dct}")
        super().__init__(name, bases, dct)


class ABC(metaclass=SaveMeta):
    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age


# 8 Create an ABC class with an abstract method for checking an integer for
# simplicity. That is, if the parameter of this method is an integer and it
# simple, then the method should return True, otherwise it should return False.


from abc import ABC, abstractmethod


class IsPrime(ABC):
    @abstractmethod
    def prime_validate(self, value):
        """Validate integer prime number"""


class NumberValidator(IsPrime):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def prime_validate(self, value):
        if not isinstance(value, int):
            return False
        for num in range(2, (value // 2) + 1):
            if not value % num:
                return False
        return True

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.integer_prime_validate(value):
            self._value = value
        else:
            raise ValueError("Value should be a prime number")


# #9 Create a class that inherits it
#
import abc


class Animal(abc.ABC):
    pass


class Cat(Animal):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    def __str__(self):
        return f"{self.nickname}"


# 10 Create a class that does not inherit a custom ABC class, but
# has the required method. Register it as a virtual
# subclass.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def my_method(self):
        pass


class Car:
    def my_method(self):
        print("Car.my_method() called")


Car.register(Vehicle)

example = Car()
example.my_method()
