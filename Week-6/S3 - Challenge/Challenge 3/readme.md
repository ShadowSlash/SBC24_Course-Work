# 🐍 **Assignment: Mastering Python Error Handling, Exceptions, Classes, and Objects**

## 🎯 **Objective**

In this assignment, you will deepen your understanding of error handling and exceptions in Python, as well as classes and objects. You will implement various techniques for managing errors, including handling multiple exceptions, utilizing `try`, `except`, `finally`, and `else` blocks, while also creating classes with attributes and methods, and employing object-oriented programming principles.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 🔍 Understand the importance of error handling and how to implement it effectively in Python.
- 🛠️ Utilize `try`, `except`, `finally`, and `else` blocks to manage exceptions and ensure code execution flow.
- 🔄 Handle multiple exceptions and understand when to catch specific exceptions.
- 💡 Raise and handle custom exceptions to enforce specific application constraints.
- 📊 Implement best practices for logging and debugging error messages.
- 🛠️ Create classes and instantiate objects with attributes and methods.
- 🔄 Utilize inheritance to create subclasses that extend the functionality of parent classes.
- 💡 Implement encapsulation to protect data and provide controlled access through methods.
- 📊 Understand the importance of constructors and destructors in managing object lifecycles.

## 👤 **User Story**

As a developer, I want to implement effective error handling and exception management in my Python applications while also utilizing classes and objects to promote code reusability and maintainability through object-oriented programming.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** YOURNAME_W6_S3_7_assignment.py.
- The script should include:
  - **✨ File Handling with Error Management**: Attempt to read a file and handle any potential `FileNotFoundError`.
  - **🔄 Multiple Exception Handling**: Create a program that accepts user input for dividing two numbers and handles both `ZeroDivisionError` and `ValueError`.
  - **📑 Using Finally and Else Blocks**: Simulate a database connection and ensure the connection closes whether an error occurs or not.
  - **🔗 Input Validation and Custom Exception**: Validate user input to ensure a positive integer is entered. Raise a custom exception if the input is negative.
  - **💾 Logging Errors**: Develop a simple logging mechanism that captures errors into a text file.
  - **✨ Class Definition**: Define a class named `Car` with attributes like `make`, `model`, and `year`, and methods for displaying car information.
  - **🔄 Inheritance**: Create a subclass named `ElectricCar` that inherits from `Car` and includes additional attributes.
  - **📦 Encapsulation**: Implement encapsulation by defining getter and setter methods for the `year` attribute in the `Car` class.
  - **🔗 Constructor and Destructor**: Use a constructor to initialize the car object and a destructor to display a message when the object is deleted.

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it YOURNAME_W6_S3_7_assignment.py.

2. **✨ File Handling with Error Management**:
   - Write code to attempt to open and read from a file named `data.txt`. Handle the `FileNotFoundError` and log the error.
   - Example:
     ```python
     try:
         with open("data.txt", "r") as file:
             content = file.read()
     except FileNotFoundError:
         print("Error: The file 'data.txt' does not exist.")
         log_error("FileNotFoundError: The file 'data.txt' does not exist.")
     ```

3. **🔄 Multiple Exception Handling**:
   - Create a function that prompts the user to enter two numbers and returns their division. Handle `ZeroDivisionError` and `ValueError`.
   - Example:
     ```python
     def divide_numbers():
         try:
             numerator = float(input("Enter the numerator: "))
             denominator = float(input("Enter the denominator: "))
             result = numerator / denominator
             print(f"The result is {result}.")
         except ZeroDivisionError:
             print("Error: Cannot divide by zero.")
             log_error("ZeroDivisionError: Cannot divide by zero.")
         except ValueError:
             print("Error: Invalid input. Please enter numeric values.")
             log_error("ValueError: Invalid input. Please enter numeric values.")
     ```

4. **📑 Using Finally and Else Blocks**:
   - Simulate a database connection and ensure that the connection closes whether an error occurs or not.
   - Example:
     ```python
     def connect_to_database():
         connection = None
         try:
             # Simulating a database connection attempt
             connection = open("database.txt", "r")  # Simulating the connection
         except FileNotFoundError:
             print("Error: Database file not found.")
             log_error("FileNotFoundError: Database file not found.")
         else:
             print("Database connected successfully.")
         finally:
             if connection:
                 connection.close()
                 print("Database connection closed.")
     ```

5. **🔗 Input Validation and Custom Exception**:
   - Write a program to validate user input for a positive integer. Raise a `ValueError` if the input is negative.
   - Example:
     ```python
     def check_positive_integer():
         try:
             user_input = int(input("Enter a positive integer: "))
             if user_input < 0:
                 raise ValueError("Input cannot be negative.")
         except ValueError as e:
             print(f"Error: {e}")
             log_error(f"ValueError: {e}")
     ```

6. **💾 Logging Errors**:
   - Implement a simple logging function that writes error messages to a file named `error_log.txt`.
   - Example:
     ```python
     from datetime import datetime

     def log_error(message):
         with open("error_log.txt", "a") as log_file:
             log_file.write(f"{datetime.now()}: {message}\n")
     ```

7. **✨ Class Definition**:
   - Define a class named `Car` with attributes: `make`, `model`, and `year`.
   - Include methods to display car information and update attributes.
   - Example:
     ```python
     class Car:
         def __init__(self, make, model, year):
             self.make = make
             self.model = model
             self.__year = year

         def display_info(self):
             print(f"Car: {self.make} {self.model}, Year: {self.__year}")

         def update_year(self, new_year):
             self.__year = new_year
     ```

8. **🔄 Inheritance**:
   - Create a subclass named `ElectricCar` that inherits from `Car`.
   - Add an attribute `battery_size` and a method to display battery information.
   - Example:
     ```python
     class ElectricCar(Car):
         def __init__(self, make, model, year, battery_size):
             super().__init__(make, model, year)
             self.battery_size = battery_size

         def display_battery_info(self):
             print(f"Battery size: {self.battery_size} kWh")
     ```

9. **📦 Encapsulation**:
   - Use getter and setter methods in the `Car` class to access and modify the private `year` attribute.

10. **🔗 Constructor and Destructor**:
    - Define a constructor that initializes a car object and a destructor that prints a message when an object is deleted.
    - Example:
      ```python
      class Car:
          def __del__(self):
              print(f"The car {self.make} {self.model} has been deleted.")
      ```

11. **📝 Test the Classes**:
    - Create instances of `Car` and `ElectricCar` and test their methods.
    - Example:
      ```python
      my_car = Car("Toyota", "Corolla", 2020)
      my_car.display_info()

      my_electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
      my_electric_car.display_info()
      my_electric_car.display_battery_info()
      ```

## 🛠️ **Additional Challenges (Optional)**

- **🌀 Advanced Logging**: Extend the logging function to capture more details.
- **⏳ Timeout Management**: Simulate a network request with a timeout.
- **🌀 Method Overriding**: Override methods in the `ElectricCar` class.
- **🛠️ Multiple Inheritance**: Demonstrate multiple inheritance with additional subclasses.

## 📎 **Additional Resources**

- [Python Exception Handling Documentation](https://docs.python.org/3/tutorial/errors.html)
- [Real Python: Python Exception Handling](https://realpython.com/python-exceptions/)
- [Python Classes and Objects Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Python Classes and Objects](https://realpython.com/python3-object-oriented-programming/)

Happy coding, and good luck techies!