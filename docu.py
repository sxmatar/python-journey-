import random
def my_function():
    """Demonstrates triple quotes docstring and does nothing."""
    return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help():")
help(my_function)
help(random)