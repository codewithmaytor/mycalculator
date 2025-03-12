def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")

        # Perform calculation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error")
                return
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            return

        # Display result
        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the calculator
if __name__ == "__main__":
    calculator()