num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

operator = str(input("Operation:"))

if operator == "add":
    x = str("+")
    print(f"{num1} {x} {num2} = {num1 + num2}")

if operator == "multiply":
    x = str("*")
    print(f"{num1} {x} {num2} = {num1 * num2}")

if operator == "subtract":
    x = str("-")
    print(f"{num1} {x} {num2} = {num1 - num2}")
