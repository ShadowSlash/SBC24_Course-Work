import re
import time
from functools import wraps

# Basic Function
def greet():
    return "Hello, Freelancer!"
print(greet())

# Function with Parameters
def create_message(name, age):
    return f"Meet {name}, who is {age} years old."
print(create_message("Leo", 28))

# Function with Default Arguments
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet("Vitor"))

# Regular Expression Function
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False
print(validate_email("leopereira@example.com"))

# Function Handling a Dictionary
user_data = {'name': 'Leo', 'email': 'Leo@example.com', 'phone': '1234567890'}

def process_user_info(user_data):
    valid_email = validate_email(user_data['email'])
    valid_phone = re.match(r'^\d{10}$', user_data['phone']) is not None
    if valid_email and valid_phone:
        return f"User {user_data['name']} has valid information."
    return "Invalid user information."
print(process_user_info(user_data))

# Basic Lambda Function
square = lambda x: x ** 2

# Using `map()`
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# Using `filter()`
strings = ['apple', 'banana', 'cherry', 'date']
strings_with_a = list(filter(lambda s: 'a' in s, strings))
print(strings_with_a)

# Sorting with Lambda
tuples_list = [(2, 'two'), (1, 'one'), (3, 'three')]
sorted_tuples = sorted(tuples_list, key=lambda x: x[0])
print(sorted_tuples)

# Decorators
def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

def param_logging_decorator(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if level > 0:
                print(f"Logging at level {level}: {func.__name__} called with {args}, {kwargs}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Applying decorators
@logging_decorator
@timing_decorator
def multi_function(x):
    return x * x
print(multi_function(10))

@timing_decorator
@param_logging_decorator(2)
def add_function(x):
    return x + x
print(add_function(5))