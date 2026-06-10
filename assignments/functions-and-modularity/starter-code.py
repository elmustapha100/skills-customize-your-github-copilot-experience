# math_utils.py - Utility module with reusable functions

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide a by b and return the result. Avoid division by zero."""
    if b == 0:
        return None
    return a / b

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def find_max_min(numbers):
    """Find and return the maximum and minimum values in a list."""
    if len(numbers) == 0:
        return None, None
    return max(numbers), min(numbers)


# main.py - Main script using the utility module

# TODO: Import the math_utils module

# TODO: Task 1 - Create functions with no params, with params, and with return values
def greet():
    """Function with no parameters."""
    pass

def greet_person(name):
    """Function with parameters."""
    pass

def add_numbers(a, b):
    """Function that returns a value."""
    pass

# TODO: Task 2 - Function with default parameters
def calculate_tax(amount, tax_rate=0.08):
    """Calculate tax on an amount with a default tax rate."""
    pass

# TODO: Task 3 - Demonstrate scope
global_var = 10

def demonstrate_scope():
    """Show local vs global scope."""
    pass

# TODO: Task 4 - Main function orchestrating everything
def main():
    """Main function to orchestrate the program."""
    # Call Task 1 functions
    # Call Task 2 functions
    # Call Task 3 functions
    # Call functions from the math_utils module
    pass

if __name__ == "__main__":
    main()
