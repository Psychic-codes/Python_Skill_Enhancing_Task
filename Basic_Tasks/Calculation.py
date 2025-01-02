class calculate:   
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ").strip()

        match operation:
            case '+':
                result = a + b
            case '-':
                result = a - b
            case '*':
                result = a * b
            case '/':
                if b == 0:
                    print("Error: Division by zero is not allowed.")
                result = a / b
            case _:
                print("Error: Invalid operation entered. Please enter +, -, *, or /.")
                
        print(f"The result of {a} {operation} {b} is = {result}")

    except ValueError:
        print("Error: Please enter valid numeric values.")

calculate()

