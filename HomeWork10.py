# 1. Create a class to describe the product. As product attributes, you can use the values of the product price, product description, product dimensions.
# Create a couple of instances of your class and test their work.

# 2. Create the "Customer" class. As attributes, you can use the last name, first name, patronymic, cell phone, etc.

# 3. Create the class "Order". An order can contain several items of a certain quantity. The order must contain information about the user who placed it.
# Implement a method for calculating the total cost of the order. Define the str() method to correctly display information about this order.
class Product:
    def __init__(self, description, price, size):
        self.description = description
        self.price = price
        self.size = size

    def __str__(self):
        return f'Product - {self.description}, size - {self.size}, price - {self.price}'
tea = Product('tea', 44.20, 'small')
coffe = Product('coffe', 290.50, 'big')
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


