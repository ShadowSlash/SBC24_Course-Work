# Initialize strings using different quoting methods
single_quote_string = 'Hello, world!'  # String created using single quotes
double_quote_string = "Python is fun!"  # String created using double quotes
triple_quote_string = """This is a string
that spans multiple
lines."""  # String created using triple quotes, spanning multiple lines

# Initialized strings
print(f"Single quote string: {single_quote_string}") # = Single quote string: Hello, world!
print(f"Double quote string: {double_quote_string}") # = Double quote string: Python is fun!
print(f"Triple quote string: {triple_quote_string}") 
# = Triple quote string: This is a string
# that spans multiple
# lines.

# Concatenate strings using the `+` operator and formatted strings (f-strings)
name = "Alice"  # Example name for concatenation
greeting = "Hello, " + name + "!"  # Concatenate using `+` operator
formatted_greeting = f"Hello {name}!"  # Concatenate using f-string

# Concatenated strings
print(f"\nGreeting using `+` operator: {greeting}") # = Greeting using `+` operator: Hello, Alice!
print(f"Greeting using f-string: {formatted_greeting}") # = Greeting using f-string: Hello Alice!

# Demonstrate string slicing to extract specific parts of a string
slice_example = "Advanced Python Strings"
sliced_string = slice_example[9:15]  # Extract the substring "Python" using slicing

# Sliced string
print(f"\nSliced string: {sliced_string}") # = Sliced string: Python

# Apply common string methods and print results
sample_string = "  hello, Python!  "  # Example string with extra spaces

upper_string = sample_string.upper()  # Convert the string to uppercase
strip_string = sample_string.strip()  # Remove leading and trailing spaces
replace_string = sample_string.replace("Python", "world")  # Replace "Python" with "world"
find_string = sample_string.find("Python")  # Find the position of "Python" in the string

# Results of string methods
print(f"\nUppercase string: {upper_string}") # = Uppercase string:   HELLO, PYTHON!
print(f"Stripped string: {strip_string}") # = Stripped string: hello, Python!
print(f"Replaced string: {replace_string}") # = Replaced string:   hello, world!
print(f"Position of 'Python': {find_string}") # = Position of 'Python': 9

# Prompt the user to input their name, age, and favorite color
user_name = input("\nEnter your name: ")  # Get user's name
user_age = input("Enter your age: ")  # Get user's age
favorite_color = input("Enter your favorite color: ")  # Get user's favorite color

# Store the user information in a dictionary
user_info = {
    "name": user_name,
    "age": user_age,
    "favorite_color": favorite_color
}

# Initial user information
print("\nInitial user information:")
print(user_info) # = e.g {'name': 'Leo', 'age': '28', 'favorite_color': 'Orange'}

# Manipulate the dictionary values
user_info["name"] = user_info["name"].upper()  # Convert the user's name to uppercase
user_info["favorite_color"] = user_info["favorite_color"].strip()  # Remove any extra spaces from the favorite color

# Updated dictionary
print("\nUpdated user information:")
print(user_info) # = e.g {'name': 'LEO', 'age': '28', 'favorite_color': 'Orange'}