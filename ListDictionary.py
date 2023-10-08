register = [{
    "name": "Eddie",
    "age": 30,
    "height": 5.6,
    "hobbies": ("money", "enjoy")
},
    {"name": "Joy",
     "age": 25,
     "height": 6,
     "hobbies": "reading"
     },
    {"name": "Jane",
     "age": "37",
     "height": 6.0,
     "hobbies": "travelling"}

]
register[0]["name"] = "King"

register[0]["gender"] = "Male"

print(register[0])

book = {
    "title": "The tortoise and the snail",
    "author": "Tomide",
    "isbn": 1212112222,
    "price": 1000

}
print('i' not in 'hi')
print("title" in book.keys())
print("Tomide" in book.values())
#
for keys, values in book.items():
    for value in book.keys():
        print(keys, values)

book2 = book.copy()
book.clear()
print(book2)
book.update({"title": "Sophie", "colour": "brown"})
print(book)
