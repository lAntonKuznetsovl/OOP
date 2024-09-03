from src.product import Product


class Category:
    """Класс предоставляющий информацию о категории товара, количестве товаров в категории и количестве категорий"""

    name: str
    description: str
    products_list: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products_list):
        """Инициализация объекта"""
        self.name = name
        self.description = description
        self.__products = products_list if products_list else []
        Category.product_count = len(products_list) if products_list else 0
        Category.category_count += 1

    def __str__(self):
        return f'{self.name}, количество продуктов: {cat.counting_total_quantity} шт.'

    @property
    def products(self):
        products_str = ''
        for product in self.__products:
            products_str += f'{str(product)}\n'
        return products_str

    def add_product(self, product: dict):
        """Метод добавления нового продукта в список"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_in_list(self):
        return self.__products

    @property
    def counting_total_quantity(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return total_quantity


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
#     print(cat.products)
#     print(cat)
