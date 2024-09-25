from src.custom_error import ZeroQuantityError
from src.base_category import BaseCategory


class Order(BaseCategory):

    def __init__(self, product_name_in_order, quantity_of_goods_sold, price_per_piece):
        self.product_name_in_order = product_name_in_order
        if quantity_of_goods_sold <= 0:
            raise ZeroQuantityError
        else:
            self.quantity_of_goods_sold = quantity_of_goods_sold
        self.price_per_piece = price_per_piece

    def __str__(self):
        return f'Ваш заказ: {self.product_name_in_order} в количестве  {self.quantity_of_goods_sold} шт. Цена заказа: {self.quantity_of_goods_sold * self.price_per_piece} руб.'

    def counting_total_products_price(self):
        """Подсчёт общей суммы заказа"""
        return self.quantity_of_goods_sold * self.price_per_piece


# if __name__ == '__main__':
#     try:
#         order1 = Order("Samsung Galaxy C23 Ultra", 2, 180000)
#     except ZeroQuantityError as e:
#         print(e)
#         print('Укажите корректное количетсво товара ')
#     else:
#         print(order1)
#     finally:
#         print('Обработка заказа завершена успешно')
    # print(order1.counting_total_products_price())
