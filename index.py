num = input("Enter a number: ")
operator = input("Enter an operator: ")
num1 = input("Enter another number: ")

print(f"{num} {operator} {num1} = {eval(num + operator + num1)}")