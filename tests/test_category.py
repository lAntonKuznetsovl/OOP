def test_category_init(data_for_categories):
    """Тест проверяющий корректоность инициализации в классе Category"""
    assert data_for_categories.name == "Телевизоры"
    assert (
            data_for_categories.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert data_for_categories.products == [
        {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    ]


def test_categories_counters(data_for_counters_categories):
    """Тест проверяющий правильность работы счётчиков в классе Category"""
    assert data_for_counters_categories.product_count == 3
    assert data_for_counters_categories.category_count == 1


def test_category_property(data_for_products):
    print(data_for_products.products)
    # assert data_for_products.products == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
