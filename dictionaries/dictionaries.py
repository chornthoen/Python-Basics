
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2024
}
cars = dict(brand="BMW", model="i8", year=2024)
print("Dictionary".center(60, "="))
print(car)
print(len(car))
print(type(car))
print(cars)
print(len(cars))
print(type(cars))
# access item
print(car["brand"])
print(car.get("model"))

print(car.keys())
print(car.values())
print(car.items())

print('brand' in car)
print('brand' not in car)
# add item
car["color"] = "red"
print(car)
# update value
car.update({"color": "blue"})
print(car)
# change value
car["brand"] = "Nissan"
print(car)
# remove item
car.pop("color")
print(car)

cars.clear()
print(cars)

# copy dictionary
print()
print("Copy dictionary".center(60, "="))
cars = car
print(car)
print(cars)

cars["color"] = "red"
print(car)
print(cars)

cars = car.copy()
cars["price"] = "100000$"
print(car)
print(cars)


car2 = dict(car)
print(car2)


# nested dictionary
print()
print("Nested dictionary".center(60, "="))
member1 = {
    "id": 1,
    "name": "Dara",
    "age": 24
}
member2 = {
    "id": 2,
    "name": "Sok",
    "age": 25
}

group = {
    "member1": member1,
    "member2": member2
}
print(group)
print(group["member1"]["name"])

# set
print()
print("Set".center(60, "="))
set1 = {"apple", "banana", "cherry"}
print(type(set1))
print(len(set1))
print(set1)
set1.add("orange")
print(set1)
set1.update(["mango", "grapes"])
print(set1)
set1.remove("banana")
print(set1)
set1.discard("grapes")
print(set1)





