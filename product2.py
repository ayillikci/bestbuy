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
        """Returns quantity of the product"""
        return self.quantity

    def set_quantity(self, quantity:int):
        """Sets a quantity for the product"""

        if quantity < 0 : # checks if the product quantity available
            raise ValueError("Product quantity can not be below 0")

        """Sets a quantity for the product"""
        self.quantity = quantity

        if quantity == 0 : # If product quantity reached 0, sets product to deactive
            self.deactive()

    def is_active(self) -> bool:
        """Checks status of the product"""
        return self.active

    def activate(self):
        """Sets availablity to product"""
        self.active = True

    def deactivate(self):
        """Sets status of the product to inactive"""
        self.active = False

    def show(self)-> str:
        """Returns product name, price and the quantity of the product"""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity:int) -> float:
        """checks buy request if it is a valid purchase"""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        """checks if requested amount is exist in the inventory"""
        if quantity > self.quantity:
            raise ValueError("Not enough stock to complete the purchase.")

        """calculates the total price of the purchase"""
        total_price = quantity * self.price
        """Recalculates the inventory"""
        self.quantity -= quantity

        """If quantity reaches to 0 after sale, deactivates product"""
        if self.quantity == 0:
            self.deactivate()

        """returns the total value of the purchase"""
        return total_price

