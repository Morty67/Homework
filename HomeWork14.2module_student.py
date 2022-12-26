class Student:

    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender


    def __str__(self):
        return f'{self.name} {self.surname},- {self.gender}'