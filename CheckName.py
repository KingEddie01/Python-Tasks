names = ["Joe", "Daniel", "Seyi", "Kelvin", "Muhammed", "Segun", "Hakimi", "Segun", "Ashley", "Seyi"]
new_names = {items: names.count(items) for items in names if items.capitalize().startswith("S")}
print(new_names)
