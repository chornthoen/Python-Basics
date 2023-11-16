
users = ["Dara", "Joey", "Monica"]

data = ["Thoen", 23, True]

print(users[0])
print(users.index("Joey"))
print(users.count("Dara"))
print(users[1:3])
print(users[1:])
print(users[:2])
print(len(users))
users.append("Sok")
print(users)
users.insert(1, "Dara")
users += ["Heng"]
print(users)

users.extend(["Chan", "Kong"])
print(users)
users.extend(data)
print(users)
users.remove("Dara")
print(users)
users.pop()
print(users)

data.clear()
print(data)

users.pop()
print(users)

users.sort()
print(users)

