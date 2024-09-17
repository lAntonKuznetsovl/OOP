class QuantityError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неверно указанно количество товара'

    def __str__(self):
        return self.message


class ZeroQuantityError(QuantityError):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Количество товара не может быть меньше или равным нулю'


class ExceedingTheQuantity(QuantityError):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Количество товара в заказе превышает количество товара на складе'
