from abc import ABC, abstractmethod
from products import Product

# Abstract base class for promotions
class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        pass


# Promotion: Second item at half price
class SecondHalfPrice(Promotion):
    def apply_promotion(self, product: Product, quantity: int) -> float:
        # Every second item is half price
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        total_price = (full_price_items * product.price) + (half_price_items * product.price * 0.5)
        return total_price


# Promotion: Buy 2, get 1 free
class ThirdOneFree(Promotion):
    def apply_promotion(self, product: Product, quantity: int) -> float:
        # For every three items, one is free
        full_price_items = quantity - (quantity // 3)
        total_price = full_price_items * product.price
        return total_price


# Promotion: Percentage discount
class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        # Apply percentage discount
        total_price = quantity * product.price * (1 - self.percent / 100)
        return total_price
