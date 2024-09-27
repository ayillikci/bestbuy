# discount_manager.py
from products import Product
from promotions import Promotion, PercentDiscount, SecondHalfPrice, ThirdOneFree

class DiscountManager:
    def __init__(self):
        self.product_promotions = {}

    def add_discount(self, product: Product, promotion: Promotion):
        """Pairs a product with a promotion."""
        if product.is_active():
            product.set_promotion(promotion)
            self.product_promotions[product.name] = promotion
            print(f"Promotion '{promotion.name}' applied to {product.name}.")
        else:
            print(f"Cannot apply promotion. The product '{product.name}' is inactive.")

    def remove_discount(self, product: Product):
        """Removes the promotion from a product."""
        if product.name in self.product_promotions:
            product.set_promotion(None)
            del self.product_promotions[product.name]
            print(f"Promotion removed from {product.name}.")
        else:
            print(f"No promotion found for {product.name}.")

    def list_discounts(self):
        """Lists all products with active promotions."""
        if self.product_promotions:
            print("Current discounts and promotions:")
            for product_name, promotion in self.product_promotions.items():
                print(f"Product: {product_name}, Promotion: {promotion.name}")
        else:
            print("No discounts or promotions currently applied.")
