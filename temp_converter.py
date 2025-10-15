def convert_f_to_c():
    """
    Prompts the user for a temperature in Fahrenheit and converts it to Celsius.
    """
    print("--- Fahrenheit to Celsius Converter ---")
    
    try:
        # Get the temperature input from the user
        f_input = input("Enter temperature in Fahrenheit (e.g., 77): ")
        
        # Convert the input to a floating-point number
        fahrenheit = float(f_input)
        
        # --- Conversion Formula ---
        # Celsius = (Fahrenheit - 32) * 5/9
        celsius = (fahrenheit - 32) * (5 / 9)
        
        # Display the result, formatted to one decimal place
        print(f"\n{fahrenheit:.1f} °F is equal to {celsius:.1f} °C")
        
        # Example output for key temperatures
        if fahrenheit == 32:
            print("(This is the freezing point of water!)")
        elif fahrenheit == 212:
            print("(This is the boiling point of water!)")

    except ValueError:
        # Handle cases where the user enters non-numeric input
        print("Error: Invalid input. Please enter a number for the temperature.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    convert_f_to_c()