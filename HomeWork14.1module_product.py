class Product:
    def __init__(self, description: str, price: int, size: str):
        self.description = description
        self.price = price
        self.size = size
        if self.price <= 0:
            raise ValueError('Prise must be only positive')

    def __str__(self):
        return f'Product - {self.description}, size - {self.size}, price - {self.price}'