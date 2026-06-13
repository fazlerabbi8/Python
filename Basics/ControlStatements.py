# nums = [4, 5, 7, 2, 10, 3]
# value = 8
# # value = 7
# for i in nums:
#     if i == value:
#         print("number found.")
#         break
# else:
#     print("number not found.")



# decrement = 5
# while True:
#     print(decrement)
#     decrement -= 1
#     if decrement == 0:
#         print("condition is matched")
#         break




# break statment
matrix = [
    [5, 7, 9],
    [8, 3, 2],
    [1, 5, 6]
]

# value = 55
# found = False
#
# for i in matrix:
#     for x in i:
#         if x == value:
#             print("Found")
#             found = True
#             break
# if not found:
#     print("Not Found")

# continue statment

value = 1;
for r in matrix:
    for c in r:
        if c == value:
            continue;
        print(c, end="")


