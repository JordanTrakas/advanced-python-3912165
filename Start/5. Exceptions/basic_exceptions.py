# Example file for Advanced Python by Joe Marini
# Working with basic exception handling

# Try to execute some code that might cause an exception:
try:
    n = int(input("Enter the first number: "))
    d = int(input("Enter the second number: "))
    result = n/d
except ZeroDivisionError as e:
    print("Cannot divide by zero")
    print(f"Exception: {e}")
except ValueError as e:
    print("Did not receive a valid number")
    print(f"Exception: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Thanks for playing!")
