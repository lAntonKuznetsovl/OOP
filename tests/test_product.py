from src.product import Product


def test_product_init(data_for_products):
    """Тест проверяющий корректность инициализации в классе Product"""
    assert data_for_products.name == "Samsung Galaxy C23 Ultra"
    assert data_for_products.description == "256GB, Серый цвет, 200MP камера"
    assert data_for_products.price == 180000.0
    assert data_for_products.quantity == 5


def test_classmethod_new_product():
    new_product = Product.new_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    })
    assert new_product.name == "Samsung Galaxy C23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_price_setter(capsys, monkeypatch):
    new_product = Product.new_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    })
    new_product.price = 200000
    assert new_product.price == 200000
    new_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == 'Цена не должна быть нулевая или отрицательная'
    assert new_product.price == 200000
    monkeypatch.setattr('builtins.input', lambda _: "y")
    new_product.price = 100
    assert new_product.price == 100