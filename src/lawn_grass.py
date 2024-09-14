from src.product import Product


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


# if __name__ == "__main__":
#     grass1 = LawnGrass.new_product({
#         "name": "Lawngrass",
#         "description": "Lawngrass small size",
#         "price": 1500.0,
#         "quantity": 5,
#         "country": "Russia",
#         "germination_period": "2 month",
#         "color": "Зелёный"
#     })
#
#     print(grass1.name)
#     print(grass1.description)
#     print(grass1.price)
#     print(grass1.quantity)
#     print(grass1.country)
#     print(grass1.germination_period)
#     print(grass1.color)
