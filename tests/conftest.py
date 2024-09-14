import pytest

from src.category import Category
from src.product import Product
from src.product_iteration import ProductIteration
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


@pytest.fixture
def product1():
    """Данные для теста класса Product"""
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    """Данные для теста класса Product"""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def data_for_categories():
    """Данные для теста класса Category для проверки корректности инициализации"""
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    )


@pytest.fixture
def data_for_counters_categories():
    """Данные для теста класса Category"""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для " "удобства жизни",
        [
            Product.new_product(
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
            ),
            Product.new_product(
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}
            ),
        ],
    )


@pytest.fixture
def new_product():
    """Новый продукт для теста Category - добавление нового продукта в список"""
    return Product.new_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    })


@pytest.fixture
def data_for_err():
    """Для проверки возбуждения ошибки при добавлении нового токара в список """
    return "Новый продукт"


@pytest.fixture
def product_iterator(data_for_counters_categories):
    """Данные для теста перебора продуктов"""
    return ProductIteration(data_for_counters_categories)


@pytest.fixture
def smartphone():
    """Данные для теста Smartphone"""
    return Smartphone.new_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "efficiency": "3.4 Ггц",
        "model": "Galaxy C23 Ultra",
        "memory": "256Gb",
        "color": "Серый"
    })


@pytest.fixture
def lawngrass():
    """Данные для теста lawngrass"""
    return LawnGrass.new_product({
        "name": "Lawngrass",
        "description": "Lawngrass small size",
        "price": 1500.0,
        "quantity": 5,
        "country": "Russia",
        "germination_period": "2 month",
        "color": "Зелёный"
    })


@pytest.fixture
def category_with_empty_product_list():
    """Тест Category с пустым списком продуктов"""
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для " "удобства жизни",
                    [])
