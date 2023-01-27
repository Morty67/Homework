# Task1 Add the Group class (task in Lecture 2) with the ability to support
# iteration protocol.
# Task2 Modify the Order class (Lesson 1 assignment) by adding an implementation
# sequence protocol and iteration protocol. 
class Product:
    def __init__(self, description, price, size):
        if self.price <= 0:
            raise ValueError('Prise must be only positive')
        self.description = description
        self.price = price
        self.size = size

    def __str__(self):
        return f'Product - {self.description}, size - {self.size}, price - {self.price}'

class Buyer:
    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}. {self.phone}'

class Order:

    def __init__(self, buyer):
        self.buyer = buyer
        self.products = []
        self.total_chek = []
        self.quantity = 1
        self.index = 0

    def add_product(self, product, count):
        if product not in self.products:
            self.products.append(product)
            self.total_chek.append(count)
        else:
            product.quantity += 1
            self.products[self.products.index(product)] = product
            self.total_chek += product.price

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return self.products[self.index - 1]
        raise StopIteration


    def total(self):
        return sum(item.price * self.total_chek for item in self.products)



    def __str__(self):
        chek_list = ''
        for item, count in zip(self.products, self.total_chek):
            chek_list += f'{item} * {count} = {item.price * count} UAH\n'

        return f"{buyer_1}\n{'-' * 30}\n" + f'{chek_list}{"-" * 30}'

tea = Product('tea', 22, 'small')
coffe = Product('coffe', 44, 'big')
bread = Product('bread', 18.80, 'average')
buyer_1 = Buyer('Karabetskyi', 'Heorhii', '06776677667')
buyer_2 = Buyer('Karabetska', 'Hanna', '09887978797')
buyer_3 = Buyer('Fedorov', 'Oleksandr', '0506775567')
order = Order(buyer_1)
order.add_product(tea, 2)
order.add_product(coffe, 5)
order.add_product(bread, 2)
print(order.__next__())
print(order.__next__())
print(order.__next__())
#print(order)


for item in order:
    print(item)


class Human:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'



class Student(Human):

    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender


    def __str__(self):
        return f'{super().__str__()}, {self.gender}'


class Group:

    def __init__(self, title, max_group=10):
        self.title = title
        self.max_group = max_group
        self.students_list = []


    def add_to_group(self, student):
        if student not in self.students_list and len(self.students_list) < self.max_group:
            self.students_list.append(student)

    def remove_student(self, student):
        if student in self.students_list:
            self.students_list.remove(student)

    def search_student(self, surname):
        search = []
        for student in self.students_list:
            if student.surname == surname:
                search.append(student)
        return search

    def __getitem__(self, item_student):
        if isinstance(item_student, int):
            if item_student > self.max_group:
                raise IndexError
            return self.students_list[item_student]
        if isinstance(item_student, slice):
            res = []
            start = item_student.start or 0
            stop = item_student.stop or self.x + 1
            step = item_student.step or 1

            for item_student in range(start, stop, step):
                res.append(self.students_list[item_student])
            return res
        raise TypeError()


    def __str__(self):
        return f"{'Group:'} {self.title} \n{'-' * 30}\n" + \
           '\n'.join(map(str, self.students_list)) + '\n'


my_group = Group('PythonItGeneration')
my_group.add_to_group(Student('Heorhii', 'Karabetskyi', 'male'))
my_group.add_to_group(Student('Hanna', 'Karabetska', 'female'))
my_group.add_to_group(Student('Oleksandr', 'Fedorov', 'male'))
my_group.add_to_group(Student('Ivan', 'Stoianov', 'male'))
my_group.add_to_group(Student('Inna', 'Stoianova', 'female'))
my_group.add_to_group(Student('Marian', 'Stoianov', 'male'))
my_group.add_to_group(Student('Oleksii', 'Leemon', 'male'))
my_group.add_to_group(Student('Maria', 'Cheban', 'female'))
my_group.add_to_group(Student('Viktor', 'Dadisha', 'male'))
my_group.add_to_group(Student('Mark', 'Karabetskyi', 'male'))
my_group.add_to_group(Student('Oleksii', 'Fevrov', 'male'))
my_group.add_to_group(Student('Dmitro', 'Sezonov', 'male'))
my_group.add_to_group(Student('Vitalyina', 'Zelenska', 'female'))
print(my_group)
print('-' * 30)
for student in my_group.search_student('Stoianov'):
    print(student.name, student.surname, student.gender)

print('\n'.join(map(str, my_group[1:7])))
