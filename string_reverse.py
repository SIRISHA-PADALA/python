def reverse_string(s):
    # Python's slicing shortcut [start:stop:step] where -1 step reverses the sequence
    return s[::-1]

# Get user input
original_string = input("Enter a string to reverse: ")

# Reverse and display the result
reversed_string = reverse_string(original_string)

print("-" * 30)
print(f"Original String: {original_string}")
print(f"Reversed String: {reversed_string}")
print("-" * 30)