from math import*
print("this is a simple calculator")
num1 =float(input("please enter first number: "))
op =input("enter operator")
num2 =float(input("enter you second number: "))
if op =="+":
    print(num1 +num2)
elif op== "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op== "*":
    print(num1 * num2)
elif op == "^":
    print(pow(num1,num2))
else:
    print("invalid operator")
