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
    assert data_for_counters_categories.products_counter == 3
    assert data_for_counters_categories.categories_counter == 1
