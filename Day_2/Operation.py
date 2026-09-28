n1 = int(input("Enter first positive integer: "))
n2 = int(input("Enter second positive integer: "))
operation = input("Enter operator (+, -, *, /): ")
if operation == "+":
    print("Result =", n1 + n2)
elif operation == "-":
    print("Result =", n1 - n2)

elif operation == "*":
    print("Result =", n1 * n2)

elif operation == "/":
    if n2 != 0:
        print("Result =", n1 / n2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")