from src.product import Product
from src.base_category import BaseCategory
from src.custom_error import ZeroQuantityError


class Category(BaseCategory):
    """Класс предоставляющий информацию о категории товара, количестве товаров в категории и количестве категорий"""

    name: str
    description: str
    products: list
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
        """Отображение приватного параметра списка продуктов"""
        return self.__products

    def avg_price(self):
        """Подсчёт средней цены товаров"""
        total_price = 0
        for product in self.__products:
            total_price += product.price
        try:
            avg_price = round(total_price / len(self.__products), 2)
            return avg_price
        except ZeroDivisionError:
            return 0

    def counting_total_products_price(self):
        """Подсчёт общей стоимости товаров в категории"""
        total_price = 0
        for product in self.__products:
            total_price += product.price * product.quantity
        return total_price


# if __name__ == '__main__':
#     try:
#         prod1 = Product("Samsung Galaxy C23 Ultra",
#                         "256GB, Серый цвет, 200MP камера",
#                         180000.0,
#                         5)
#
#         prod2 = Product(
#             "Iphone 15",
#             "512GB, Gray space",
#             210000.0,
#             8)
#
#         prod3 = Product(
#             "Xiaomi Redmi Note 11",
#             "1024GB, Синий",
#             31000.0,
#             14)
#
#         prod4 = Product("55\" QLED 4K",
#                         "Фоновая подсветка",
#                         123000.0,
#                         3)
#
#         cat = Category(
#             "Смартфоны",
#             "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
#             [prod1, prod2])
#
#         cat2 = Category("Телевизоры",
#                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#                         [prod4])
#
#         print(cat.products)
#         cat.add_product(Product.new_product({
#             "name": "Xiaomi Redmi Note 11",
#             "description": "1024GB, Синий",
#             "price": 31000.0,
#             "quantity": 3
#         }))
        # print(cat.products)
        #
        # print(cat.avg_price())
        # print(Category.product_count)
        # print(Category.category_count)
        # print(cat)
        # print(cat2)
        # prod5 = Product.new_product({
        #     "name": "Samsung Galaxy M33",
        #     "description": "128GB, Синий цвет, 1500MP камера",
        #     "price": 110000.0,
        #     "quantity": 15,
        # })
        # cat.add_product(prod5)
        # print(cat.products)
        # print(Category.product_count)
        # print(Category.category_count)
        # print(cat.counting_total_products_price())
    # except ZeroQuantityError as e:
    #     print(e)
    #     print('Введите корректное количество товара')
