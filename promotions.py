from abc import ABC, abstractmethod

from products import Product

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        pass

    def __str__(self):
        return self.name


# Promotion for percentage discount
class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: int):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity


# Promotion for second item at half price
class SecondHalfPrice(Promotion):
    def apply_promotion(self, product: Product, quantity: int) -> float:
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        total_price = (full_price_items * product.price) + (half_price_items * product.price * 0.5)
        return total_price


# Promotion for buy 2 get 1 free
class ThirdOneFree(Promotion):
    def apply_promotion(self, product: Product, quantity: int) -> float:
        paid_items = quantity - (quantity // 3)
        total_price = paid_items * product.price
        return total_price
