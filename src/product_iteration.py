from src.product import Product
from src.category import Category


class ProductIteration:
    def __init__(self, category_object):
        self.category = category_object
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


# if __name__ == '__main__':
#     prod1 = Product("Samsung Galaxy C23 Ultra",
#                     "256GB, Серый цвет, 200MP камера",
#                     180000.0,
#                     5)
#
#     prod2 = Product(
#         "Iphone 15",
#         "512GB, Gray space",
#         210000.0,
#         8)
#
#     prod3 = Product(
#         "Xiaomi Redmi Note 11",
#         "1024GB, Синий",
#         31000.0,
#         14)
#
#     cat = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
#         [prod1, prod2, prod3])
#
#     iterator = ProductIteration(cat)
#
#     for product in iterator:
#         print(product)
#     for product in iterator:
#         print(product)
