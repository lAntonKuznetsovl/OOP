from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс предоставляющий информацию о продукте"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_params: dict):
        """Метод добавляющий новый продукт в список"""
        return cls(**product_params)

    @property
    def price(self):
        """Метод волзвращающий цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Метод меняющий цену продукта в зависимости от условия"""
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        elif new_price > self.__price:
            self.__price = new_price
        else:
            while True:
                answer = input('Введите ответ на понижение цены - y/n: ')
                if answer.lower() == 'y':
                    self.__price = new_price
                    break
                elif answer.lower() == 'n':
                    break


# if __name__ == '__main__':
#     prod1 = Product.new_product({
#         "name": "Samsung Galaxy C23 Ultra",
#         "description": "256GB, Серый цвет, 200MP камера",
#         "price": 180000.0,
#         "quantity": 5
#     })
# prod2 = Product(
#     "Iphone 15",
#     "512GB, Gray space",
#     210000.0,
#     8)
#
# prod3 = Product(
#     "Xiaomi Redmi Note 11",
#     "1024GB, Синий",
#     31000.0,
#     14)

# print(prod1.name)
# print(prod1.description)
# print(prod1.price)
# print(prod1.quantity)
# print(prod2)
# print(prod3)
# print(prod1 + prod2)
