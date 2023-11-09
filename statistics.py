command = input()
products = {}

while command != "statistics":
    key, value = command.split(": ")
    value = int(value)

    if key in products:
        products[key] += value
    else:
        products[key] = value

    command = input()

print("Products in stock:")

for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")