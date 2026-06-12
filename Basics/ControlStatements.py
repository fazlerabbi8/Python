nums = [4, 5, 7, 2, 10, 3]
value = 8
# value = 7
for i in nums:
    if i == value:
        print("number found.")
        break
else:
    print("number not found.")