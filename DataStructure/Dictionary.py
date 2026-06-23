d = {"name" : "Rabbi", "age" : 22,}
# print(d)

# print(d["age"])
# print(d.get("name"))


# d2 = {"name": "ali"}
# d2["age"] = 22
# d2["name"] = "sakib"
# print(d2)


# d = {"a": 1, "b": 2}
#
# val = d.pop("a")
# print(d)

# Iterating Through a Dictionary

for key in d:
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)