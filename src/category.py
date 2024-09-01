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

    @products.setter
    def products(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products_in_list(self):
        return self.__products
