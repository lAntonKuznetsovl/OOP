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
        self.__products = products_list
        Category.product_count = len(products_list)
        Category.category_count += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_str = ''
        for product in self.__products:
            products_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return products_str


if __name__ == '__main__':
    prod1 = Product("Iphone 15",
                    "512GB, Gray space",
                    210000.0,
                    8)

    prod2 = Product("Samsung Galaxy C23 Ultra",
                    "256GB, Серый цвет, 200MP камера",
                    180000.0,
                    5)

    cat = Category("Смартфоны",
                   "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
                   [{prod1, prod2}])
    #
    # prod = {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    # print(prod1.name)
    # print(prod1.description)
    print(cat.products)
