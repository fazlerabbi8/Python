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
# age = int(input("What is your age? "))
# s = "voter" if age >= 20 else "not voter"
# print(s)


# Multiple Conditions with If Statement

a  = int(input("number 1: "))
b = int(input("number 2: "))
c = int(input("number 3: "))

if a > b and a > c:
    print("a is largest")
elif b > a and b > c:
    print("b is largest")
elif c > a and c > b:
    print("c is largest")
else:
    print("all numbers are equal")