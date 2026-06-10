# age = int(input("What is your age? "))
#
# if age <= 15:
#     print("child")
# elif age <= 19 :
#     print("Teenager")
# elif age <= 25:
#     print("Younger")
# else:
#     print("Adult")
#


# Conditional Expression (Ternary Operator)
age = int(input("What is your age? "))
s = "voter" if age >= 20 else "not voter"
print(s)