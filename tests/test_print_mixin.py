from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_print_mixin_smartphone_class(capsys):
    """Тест корректности вывода сообщения"""
    Smartphone.new_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "efficiency": "3.4 Ггц",
        "model": "Galaxy C23 Ultra",
        "memory": "256Gb",
        "color": "Серый"
    })
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Smartphone, Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера', 180000.0, 5")


def test_print_mixin_lawn_grass_class(capsys):
    """Тест корректности вывода сообщения"""
    LawnGrass.new_product({
                "name": "Lawngrass",
                "description": "Lawngrass small size",
                "price": 1500.0,
                "quantity": 5,
                "country": "Russia",
                "germination_period": "2 month",
                "color": "Зелёный"
            })
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass, Lawngrass, Lawngrass small size', 1500.0, 5"


def test_print_mixin_product_class(capsys):
    """Тест корректности вывода сообщения"""
    Product.new_product({
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            })
    message = capsys.readouterr()
    assert message.out.strip() == "Product, Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера', 180000.0, 5"
