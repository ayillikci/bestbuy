from products import Product

class Store:
    def __init__(self, products: list[Product]):
        self.products = products

    def add_product(self, product: Product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total number of items in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list[Product]:
        """Returns a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Processes an order consisting of a list of (Product, quantity) tuples.
        Buys the products and returns the total price of the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                total_price += product.buy(quantity)
            else:
                raise ValueError(f"Product {product.name} is not available or inactive.")
        return total_price