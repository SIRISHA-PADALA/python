def fibonacci(n):
    # Base cases for the sequence
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive step: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Calculate the 10th Fibonacci number
n_value = 10
result = fibonacci(n_value)

print(f"--- Recursive Fibonacci Sequence ---")
print(f"The first 10 numbers are:")

# Print the sequence up to the Nth term
sequence = [fibonacci(i) for i in range(n_value)]
print(sequence)

print(f"The {n_value}th Fibonacci number is: {result}")