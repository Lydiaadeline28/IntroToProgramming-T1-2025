try:
    # Code that may raise an exception
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Cannot divide by zero.")
try:
    # Code that may raise different exceptions
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
def divide(numerator, denominator):
    if denominator == 0:
        raise ValueError("Error: Cannot divide by zero.")
    return numerator / denominator

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)


