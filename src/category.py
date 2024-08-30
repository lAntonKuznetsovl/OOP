class Category:
    """Класс предоставляющий информацию о категории товара, количестве товаров в категории и количестве категорий"""

    name: str
    description: str
    products: list
    categories_counter = 0
    products_counter = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.products_counter = len(products)
        Category.categories_counter += 1
