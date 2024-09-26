# Import the Product class from the products module
from products import Product
from store import Store


# Main function to run the program
def main():
    product_list = [
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    store = Store(product_list)

    """Get all active products"""
    products = store.get_all_products()

    """Print the total quantity of items in the store"""
    print(f"Total quantity in store: {store.get_total_quantity()}")

    """Create an order"""
    try:
        order_price = store.order([(products[0], 1), (products[1], 2)])
        print(f"Order cost: {order_price} dollars.")
    except ValueError as e:
        print(e)

    """Adding products"""
    pixel = Product("Google Pixel 7", price=500, quantity=250)
    store.add_product(pixel)

    print(f"Total quantity in store after adding Pixel: {store.get_total_quantity()}")

    """Removing products"""
    store.remove_product(pixel)
    print(f"Total quantity in store after removing Pixel: {store.get_total_quantity()}")

    """ STEP 1 Part"""
    """print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()"""


# Execute the main function
if __name__ == "__main__":
    main()
