# --- Simple Calculator ---
# This program demonstrates basic arithmetic operations and user input.

def calculator():
    """
    Performs a simple calculation based on user input for two numbers
    and an operation (+, -, *, /).
    """
    print("Welcome to the Simple Python Calculator!")
    
    try:
        # Get the first number from the user
        num1 = float(input("Enter the first number: "))
        
        # Get the desired operation
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Get the second number from the user
        num2 = float(input("Enter the second number: "))

        result = 0

        # Perform the calculation based on the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            # Check for division by zero
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            print(f"Error: Invalid operation '{operation}'.")
            return

        # Display the result
        print(f"\nResult: {num1} {operation} {num2} = {result}")

    except ValueError:
        # Handle cases where the user enters non-numeric input
        print("Error: Invalid number input. Please enter digits only.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()
