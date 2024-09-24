
# Import the Product class from the products module
from products import Product

# Main function to run the program
def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  # Expected: 12500.0
    print(mac.buy(100))  # Expected: 145000.0
    print(mac.is_active())  # Expected: False (since quantity should be 0 after purchase)

    print(bose.show())  # Expected: "Bose QuietComfort Earbuds, Price: 250, Quantity: 450"
    print(mac.show())   # Expected: "MacBook Air M2, Price: 1450, Quantity: 0"

    bose.set_quantity(1000)
    print(bose.show())  # Expected: "Bose QuietComfort Earbuds, Price: 250, Quantity: 1000"

# Execute the main function
if __name__ == "__main__":
    main()
