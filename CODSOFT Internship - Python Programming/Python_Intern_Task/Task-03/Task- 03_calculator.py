def calculator():
    """Performs basic arithmetic operations."""

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ValueError("Cannot divide by zero")
                result = num1 / num2
            else:
                print("Invalid operation")
                continue

            print("Result:", result)
            break  # Exit the loop after a successful calculation

        except ValueError:
            print("Invalid input. Please enter numbers only.")

        try_again = input("Do you want to perform another calculation? (y/n): ")
        if try_again.lower() != "y":
            break

calculator()  # Call the function to start the calculator
