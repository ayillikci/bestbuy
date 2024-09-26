# Class for defining a product
class Product:
    def __init__(self, name:str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0 :
            raise ValueError("Product can price can not be below 0")
        if quantity < 0 :
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
            """
            if not type(self) == int:
                raise ValueError("Product quantity needs to be an integer number")
            """
            return self.quantity

    def set_quantity(self, quantity:int):
        if quantity < 0 :
            raise ValueError("Product quantity can not be below 0")

        self.quantity = quantity

        if quantity == 0 :
            self.deactive()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self)-> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity:int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock to complete the purchase.")

        total_price = quantity * self.price
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()
        return total_price

