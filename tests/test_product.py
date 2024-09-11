import pytest
from src.product import Product


def test_product_init(product1):
    """Тест проверяющий корректность инициализации в классе Product"""
    assert product1.name == "Samsung Galaxy C23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_classmethod_new_product():
    """Создание нового продукта из словаря"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy C23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_price_setter(capsys, monkeypatch):
    """Проверка замены цены"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    new_product.price = 200000
    assert new_product.price == 200000
    new_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert new_product.price == 200000
    monkeypatch.setattr("builtins.input", lambda _: "y")
    new_product.price = 100
    assert new_product.price == 100


def test_product_str(product1):
    assert str(product1) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product(product1, product2):
    assert product1 + product2 == 1334000
    with pytest.raises(TypeError):
        product1 + 1
