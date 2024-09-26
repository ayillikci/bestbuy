import pytest
from store import Store
from products import Product


def test_product_valid():  # Normal product creation
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100



def test_product_empty_name():  # Empty name
    with pytest.raises(ValueError):
        product = Product("", price=1450, quantity=100)



def test_product_negative_price():
    with pytest.raises(ValueError):
        product = Product("MacBook Air M2", price=-10, quantity=100)

def test_product_negative_quantity():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=10, quantity=-100)

def test_product_quantity_0():  # when a product reaches 0 quantity, it becomes inactive.
    product = Product("MacBook Air M2", price=1450, quantity=100)
    product.buy(100)
    assert product.is_active() == False
   # with pytest.raises(ValueError):
       # product.buy(1000)

def test_product_quantity_reduction():  # product quantity will decrease.
    product = Product("MacBook Air M2", price=1450, quantity=100)
    product.buy(30)
    assert product.quantity == 70

def test_product_purchase_large_quantity():  # sale can not be done if purchase quanity is bigger than stock.
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        product.buy(101)
