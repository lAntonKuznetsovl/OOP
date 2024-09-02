from src.product import Product


class Category:
    """Класс предоставляющий информацию о категории товара, количестве товаров в категории и количестве категорий"""

    name: str
    description: str
    products_list: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products_list):
        self.name = name
        self.description = description
        self.__products = products_list if products_list else []
        Category.product_count = len(products_list) if products_list else 0
        Category.category_count += 1

    @property
    def products(self):
        products_str = ''
        for product in self.__products:
            products_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return products_str

    def add_product(self, product: dict):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_in_list(self):
        return self.__products


if __name__ == '__main__':
    cat = Category("Смартфоны",
                   "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для " "удобства жизни",
                   [

                       {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},

                       {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0,
                        "quantity": 14},
                   ])
    print(cat.name)
    print(cat.description)
    print(cat.products_in_list)
    print(cat.product_count)
    cat.add_product({"name": "Samsung Galaxy C23 Ultra",
                     "description": "256GB, Серый цвет, 200MP камера",
                     "price": 180000.0,
                     "quantity": 5})
    print(cat.products_in_list)
    print(cat.product_count)