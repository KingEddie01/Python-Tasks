def check(input):
    s = {name: input.count(name) for name in input if name.startswith('S')}
    return s


names = ["Joe", "Daniel", "Seyi", "Kelvin", "Muhammed", "Segun", "Hakimi", "Segun", "Ashley", "Seyi"]
new_name = check(names)
print(new_name)




