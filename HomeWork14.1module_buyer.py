class Buyer:
    def __init__(self, surname: str, name: str, phone: str):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}. {self.phone}'