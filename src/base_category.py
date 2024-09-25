from abc import ABC, abstractmethod


class BaseCategory(ABC):

    @abstractmethod
    def counting_total_products_price(self, *args, **kwargs):
        pass
