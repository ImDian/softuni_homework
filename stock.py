elements = input().split()
check_for = input().split()

products = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    products[key] = int(value)

for product in check_for:
    if product in products.keys():
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")