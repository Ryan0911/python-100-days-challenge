# pylint: disable=C0103, C0114, C0301, W0718
from calculator import Calculator

calculator = Calculator()
print("Welcome to the Calculator")

operations = {
    '+': calculator.add,
    '-': calculator.subtract,
    '*': calculator.multiply,
    '/': calculator.divide
}
num1 = 0
num2 = 0
operation = ''

while True:
    operation = input("Enter an operation (+, -, *, /), or 'r' to reset, or 'q' to quit: ").strip().lower()
    if operation == "q":
        break
    if operation == "r":
        calculator.reset()
        num1 = 0
        num2 = 0
        print("Calculator reset.")
        continue
    if operation not in operations:
        print("Invalid operation. Try again.")
        continue

    while True:
        try:
            print(f"Current result: {calculator.get_result()}")
            if calculator.get_result() == 0:
                num1 = float(input("Enter the first number: "))
            else:
                num1 = calculator.get_result()
            num2 = float(input("Enter the second number: "))
            if operation == '/' and num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    try:
        operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {calculator.get_result()}")
    except Exception as e:
        print(f"An error occurred: {e}")

print("-" * 20)
print(f"The final result is: {calculator.get_result()}")
