# Separate the classes used to solve the ordering task and the group of students by module. Make sure the projects are working properly.

import module_product
import module_buyer
import module_order


tea = module_product.Product('tea', 0, 'small')
coffe = module_product.Product('coffe', -1, 'big')
bread = module_product.Product('bread', 18.80, 'average')


buyer_1 = module_buyer.Buyer('Karabetskyi', 'Heorhii', '06776677667')
buyer_2 = module_buyer.Buyer('Karabetska', 'Hanna', '09887978797')
buyer_3 = module_buyer.Buyer('Fedorov', 'Oleksandr', '0506775567')


order = module_order.Order(buyer_1)
order.add_product(tea, 2)
order.add_product(coffe, 5)
order.add_product(bread, 2)
print(order)
