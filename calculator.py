#!/usr/bin/env python3
"""
Simple Calculator with intentional bugs for testing GitFixer.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    # BUG: Returns wrong result (swapped operands)
    return b - a

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    # BUG: No zero division check
    return a / b

def calculate(operation, a, b):
    """Perform the specified operation."""
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        # BUG: Returns None instead of raising an error
        return None

def main():
    print("Simple Calculator")
    print("-" * 20)
    
    # Test cases
    print(f"10 + 5 = {add(10, 5)}")           # Expected: 15, Actual: 15
    print(f"10 - 5 = {subtract(10, 5)}")     # Expected: 5, Actual: -5 (BUG!)
    print(f"10 * 5 = {multiply(10, 5)}")     # Expected: 50, Actual: 50
    print(f"10 / 5 = {divide(10, 5)}")       # Expected: 2, Actual: 2.0
    print(f"10 / 0 = {divide(10, 0)}")       # Will crash! (BUG!)

if __name__ == "__main__":
    main()
