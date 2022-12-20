#  Модифікуйте Перше домашнє завдання так,
# щоб при спробі встановити від'ємну або нульову вартість товару викликалася виняткова ситуація\
# (тип виняткової ситуації треба самостійно реалізувати).
class Product:
    def __init__(self, description, price, size):
        self.description = description
        self.price = price
        self.size = size
        if self.price <= 0:
            raise ValueError('Prise must be only positive')

    def __str__(self):
        return f'Product - {self.description}, size - {self.size}, price - {self.price}'
tea = Product('tea', 0, 'small')
coffe = Product('coffe', -1, 'big')
bread = Product('bread', 18.80, 'average')


class Buyer:
    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}. {self.phone}'

buyer_1 = Buyer('Karabetskyi', 'Heorhii', '06776677667')
buyer_2 = Buyer('Karabetska', 'Hanna', '09887978797')
buyer_3 = Buyer('Fedorov', 'Oleksandr', '0506775567')


class Order:

    def __init__(self, buyer):
        self.buyer = buyer
        self.products = []
        self.total_chek = []

    def add_product(self, product, count):
        if product not in self.products:
            self.products.append(product)
            self.total_chek.append(count)


    def total(self):
        return sum(item.price * self.total_chek for item in self.products)



    def __str__(self):
        chek_list = ''
        for item, count in zip(self.products, self.total_chek):
            chek_list += f'{item} * {count} = {item.price * count} UAH\n'

        return f"{buyer_1}\n{'-' * 30}\n" + f'{chek_list}{"-" * 30}'

order = Order(buyer_1)
order.add_product(tea, 2)
order.add_product(coffe, 5)
order.add_product(bread, 2)
print(order)


