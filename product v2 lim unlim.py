class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product information.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0 or quantity > self.quantity:
            raise ValueError("Invalid purchase quantity.")
        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


# New class for NonStockedProduct
class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        # Always set quantity to 0 for non-stocked products
        super().__init__(name, price, 0)

    def set_quantity(self, quantity: int):
        # Override to always keep quantity at 0
        self.quantity = 0

    def buy(self, quantity: int) -> float:
        # You can buy as many licenses as you want, but quantity doesn't change
        return self.price * quantity

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited (Non-Stocked)"


# New class for LimitedProduct
class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of {self.name}.")
        return super().buy(quantity)

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Max per order: {self.maximum}, Quantity: {self.quantity}"
