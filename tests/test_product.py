def test_product_init(data_for_products):
    """Тест проверяющий корректность инициализации в классе Product"""
    assert data_for_products.name == "Samsung Galaxy C23 Ultra"
    assert data_for_products.description == "256GB, Серый цвет, 200MP камера"
    assert data_for_products.price == 180000.0
    assert data_for_products.quantity == 5
