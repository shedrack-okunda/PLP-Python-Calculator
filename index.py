num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Error: Division by zero is not allowed.'
else:
    result = "Error: Invalid operator."

if isinstance(result, str):
    print(result)
else:
    print(f"{num1} {operator} {num2} = {result}")