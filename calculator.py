def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def power(a, b):
    return a ** b
def modulus(a, b):
    return a % b
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "%": modulus
}
def calculator():
    print("Python Calculator")
    print("Available operations:")
    for op in operations:
        print(op)
    num1 = float(input("Enter first number: "))
    while True:
        operator = input("Pick an operation: ")
        num2 = float(input("Enter next number: "))
        calculation = operations[operator]
        result = calculation(num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        choice = input(
            "Type 'y' to continue with result, "
            "'n' for new calculation, "
            "'q' to quit: "
        ).lower()
        if choice == 'y':
            num1 = result
        elif choice == 'n':
            calculator()
            break
        else:
            print("Calculator closed.")
            break

calculator()
