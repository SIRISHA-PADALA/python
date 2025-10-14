def factorial(n):
    # Base Case: Factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive Step: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

number = 6
result = factorial(number)

print(f"--- Factorial Calculation ---")
print(f"The number is: {number}")
print(f"The factorial ({number}!) is: {result}")