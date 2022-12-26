class Order:

    def __init__(self, buyer: str):
        self.buyer = buyer
        self.products = []
        self.total_chek = []

    def add_product(self, product: str, count: int):
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