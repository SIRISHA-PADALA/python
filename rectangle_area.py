def calculate_rectangle_area(length, width):
    return length * width

# Get user input
try:
    # Use float() to allow for decimal values
    rect_length = float(input("Enter the length of the rectangle: "))
    rect_width = float(input("Enter the width of the rectangle: "))

    # Calculate and display the result
    area = calculate_rectangle_area(rect_length, rect_width)
    
    print("-" * 30)
    print(f"Length: {rect_length}")
    print(f"Width: {rect_width}")
    print(f"The area of the rectangle is: {area:.2f} square units")
    print("-" * 30)

except ValueError:
    print("Invalid input. Please enter valid numbers for length and width.")