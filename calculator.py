a = int(input("Enter number: "))
b = int(input("Enter Second Number: "))
operator = input("Enter operator: ")

match (operator):
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        raise ValueError("Invalid operator: must be '+', '-', '*', or '/'")
