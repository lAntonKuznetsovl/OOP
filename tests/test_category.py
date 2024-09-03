def test_category_init(data_for_categories):
    """Тест проверяющий корректоность инициализации в классе Category"""
    assert data_for_categories.name == "Телевизоры"
    assert (
            data_for_categories.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert data_for_categories.products_in_list == [
        {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    ]


def test_categories_counters(data_for_counters_categories):
    """Тест проверяющий правильность работы счётчиков в классе Category"""
    assert data_for_counters_categories.product_count == 2
    assert data_for_counters_categories.category_count == 1


def test_category_products_property(data_for_counters_categories):
    """Проверка корректности вывода строки"""
    assert data_for_counters_categories.products == (
        'Iphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')


def test_category_add_product(data_for_categories, new_product):
    """Проверка добавления нового продукта в список"""
    assert len(data_for_categories.products_in_list) == 1
    data_for_categories.add_product(new_product)
    assert len(data_for_categories.products_in_list) == 2


def test_category_str(data_for_counters_categories):
    assert str(data_for_counters_categories) == 'Телевизоры, количество продуктов: 7 шт.'
