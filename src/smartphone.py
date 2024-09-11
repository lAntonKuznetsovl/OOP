from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


# if __name__ == "__main__":
#     phone1 = Smartphone.new_product({
#         "name": "Samsung Galaxy C23 Ultra",
#         "description": "256GB, Серый цвет, 200MP камера",
#         "price": 180000.0,
#         "quantity": 5,
#         "efficiency": "3.4 Ггц",
#         "model": "Galaxy C23 Ultra",
#         "memory": "256Gb",
#         "color": "Серый"
#     })
#
#     phone2 = Smartphone.new_product({
#         "name": "Samsung Galaxy M33",
#         "description": "128GB, Синий цвет, 1500MP камера",
#         "price": 110000.0,
#         "quantity": 15,
#         "efficiency": "2.6 Ггц",
#         "model": "Galaxy M33",
#         "memory": "128Gb",
#         "color": "Синий"
#     })
#
#     prod1 = Product.new_product({
#         "name": "Samsung Galaxy C23 Ultra",
#         "description": "256GB, Серый цвет, 200MP камера",
#         "price": 180000.0,
#         "quantity": 5
#     })

    # print(phone2.name)
    # print(phone2.description)
    # print(phone2.price)
    # print(phone2.quantity)
    # print(phone2.efficiency)
    # print(phone2.model)
    # print(phone2.memory)
    # print(phone2.color)
    # print(prod1.name)
    #     print(prod3)
    #     print(prod1 + prod2)
    # print(phone1 + prod1)