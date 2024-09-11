from src.product import Product


class Category:
    """Класс предоставляющий информацию о категории товара, количестве товаров в категории и количестве категорий"""

    name: str
    description: str
    products_list: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация объекта"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count = len(products) if products else 0
        Category.category_count += 1

    def __str__(self):
        """Метод отображающий строку в заданном формате"""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    @property
    def products(self):
        """Отображение продукта в заданном формате"""
        products_str = ''
        for product in self.__products:
            products_str += f'{str(product)}\n'
        return products_str

    def add_product(self, product: dict):
        """Метод добавления нового продукта в список"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products


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
#     prod4 = Product("55\" QLED 4K",
#                     "Фоновая подсветка",
#                     123000.0,
#                     7)
#
#     cat = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
#         [prod1, prod2, prod3])
#
#     cat2 = Category("Телевизоры",
#                     "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#                     [prod4])
#
#     print(cat.products)
#     print(Category.product_count)
#     print(Category.category_count)
#     # print(cat)
#     # print(cat2)
#     prod5 = Product.new_product({
#         "name": "Samsung Galaxy M33",
#         "description": "128GB, Синий цвет, 1500MP камера",
#         "price": 110000.0,
#         "quantity": 15,
#     })
#     cat.add_product(prod5)
#     print(cat.products)
#     print(Category.product_count)
#     print(Category.category_count)
