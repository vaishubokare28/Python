"""User defined exception

# How to Define a User-Defined Exception in Python
To define a user-defined exception:

Create a Class: You need to create a class that inherits from Python's built-in Exception class (or a subclass like ValueError, TypeError, etc.).

Initialize the Class: You can define an init method to handle custom error messages or any other parameters that are useful.

Optional: You can override the str method to customize how the exception message will be displayed."""

#Step 1: Define the custom exception class

class InvalidAgeError (Exception):
   """Exception raised for invalid age input."""

   def __init__(self, message="Age cannot be negative or zero"):
     self.message=message
     super().__init__(self.message)


#Step 2: Use the exception in code
def check_age(age):
   if age <= 0:
     raise InvalidAgeError("Age must be a positive number.")
   print (f"Your age is {age}")


#Step 3: Handle the exception


try:
 check_age(-5)
except InvalidAgeError as e:
 print(f"Error: {e}")