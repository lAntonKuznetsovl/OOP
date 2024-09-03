def test_product_iteration(product_iterator):
    assert product_iterator.index == 0
    assert next(product_iterator).name == 'Samsung Galaxy C23 Ultra'