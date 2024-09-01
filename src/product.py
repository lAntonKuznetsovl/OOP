class Product:
    """Класс предоставляющий информацию о продукте"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_params: dict):
        return cls(**product_params)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
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
