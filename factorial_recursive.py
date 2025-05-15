#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input number `n`.

    Raises:
        RecursionError: If the recursion depth is exceeded due to very large `n`.
        ValueError: If `n` is negative (though not explicitly handled in this code).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check if the user provided an argument
if len(sys.argv) < 2:
    print("Usage: ./factorial_recursive.py <non-negative-integer>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        raise ValueError("Number must be non-negative.")
except ValueError as e:
    print(f"Invalid input: {e}")
    sys.exit(1)

# Compute and print the factorial
f = factorial(num)
print(f)
