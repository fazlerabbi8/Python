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

# for key in d:
#     print(key)
#
# for value in d.values():
#     print(value)
#
# for key, value in d.items():
#     print



# Creating a Nested Dictionary
students = {}

students["student1"] = {"name": "Rabbi", "age" : 22, "grade" : 'A+'}
students["student2"] = {"name": "ali", "age" : 21, "grade" : 'B+'}
students["student3"] = {"name": "sakib", "age" : 20, "grade" : 'C+'}

# Adding Elements to a Nested Dictionary
students["student1"]["id"] = '47014'
students["student2"]["id"] = '47015'
students["student3"]["id"] = '47016'


# Accessing elements
v1 = students["student1"]["age"]
v2 = students["student1"]["id"]

print("age : ", v1)
print("id : ", v2)

# print(students)