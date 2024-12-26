from products import Product
from store import Store


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

store = Store(product_list)
products = store.get_all_products()

print(f"Total quantity: {store.get_total_quantity()}")
print(f"Order cost: {store.order([(products[0], 1), (products[1], 2)])} dollars.")


"""
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.show())
print(mac.show())

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

print(bose.show())
print(mac.show())

print(bose.set_quantity(1000))
print(bose.show())

print(bose.get_quantity())
"""







