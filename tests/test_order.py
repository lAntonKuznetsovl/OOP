import pytest
from src.custom_error import ZeroQuantityError
from src.order import Order


def test_order_init(order_init):
    """Тест инициализации заказа"""
    assert order_init.product_name_in_order == "Samsung Galaxy C23 Ultra"
    assert order_init.quantity_of_goods_sold == 2
    assert order_init.price_per_piece == 180000


def test_order_init_with_zero_quantity():
    """Тест ошибки инициализации при нулевом количестве товара"""
    with pytest.raises(ZeroQuantityError):
        Order("Samsung Galaxy C23 Ultra", 0, 180000)


def test_counting_total_products_price(order_init):
    """Тест подсчёта общей стоимости заказа"""
    assert order_init.counting_total_products_price() == 360000
