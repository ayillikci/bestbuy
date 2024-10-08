# Import the Product class from the products module
from products import Product, NonStockedProduct, LimitedProduct
from store import Store
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount


def run_store(store):
    while True:
        print("\nWelcome to the store! Please choose an option:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_quantity(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Thank you for using the store. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a valid choice (1-4).")


def list_products(store):
    """Lists all active products in the store."""
    available_products = store.get_all_products()
    if available_products:
        for product in available_products:
            print(product.show())
    else:
        print("No active products in the store.")


def show_total_quantity(store):
    """Shows the total quantity of products in the store."""
    total_quantity = store.get_total_quantity()
    print(f"Total quantity of all products in the store: {total_quantity}")


def make_order(store):
    """Allows the user to make an order by selecting products and quantities."""
    try:
        products = store.get_all_products()
        if not products:
            print("No active products available for ordering.")
            return

        order_list = []
        print("Please enter the product numbers and the quantity to order.")
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product.show()}")

        while True:
            product_choice = input("Enter product number to order (or 'done' to finish): ").strip()
            if product_choice.lower() == 'done':
                break

            try:
                product_choice = int(product_choice) - 1
                if 0 <= product_choice < len(products):
                    product = products[product_choice]
                    quantity = int(input(f"Enter quantity for {product.name}: "))
                    order_list.append((product, quantity))
                else:
                    print("Invalid product number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if order_list:
            total_price = store.order(order_list)
            print(f"Total price of the order: {total_price:.2f}")
        else:
            print("No products were ordered.")
    except ValueError as e:
        print(f"Order error: {e}")


def main():
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half Price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)  # MacBook Air M2
    product_list[1].set_promotion(third_one_free)  # Bose QuietComfort Earbuds
    product_list[3].set_promotion(thirty_percent)  # Windows License

    best_buy = Store(product_list)

    # Start the interactive menu (replace run_store with your existing function)
    run_store(best_buy)

if __name__ == "__main__":
    main()