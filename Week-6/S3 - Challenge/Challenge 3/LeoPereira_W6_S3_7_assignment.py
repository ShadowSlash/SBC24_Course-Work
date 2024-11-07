import logging
import time

# ✨ File Handling with Error Management
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError as e:
        log_error(e)

# Multiple Exception Handling
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print("Error: Division by zero is not allowed.")
        log_error(e)
    except ValueError as e:
        print("Error: Invalid input. Please enter numeric values.")
        log_error(e)

# Using Finally and Else Blocks
def simulate_database_connection():
    try:
        print("Connecting to the database...")
        if True:
            print("Database operation successful.")
    except Exception as e:
        print("Error occurred during database operation.")
        log_error(e)
    else:
        print("No errors occurred during database operation.")
    finally:
        print("Closing the database connection...")

# Input Validation and Custom Exception
class NegativeInputError(Exception):
    pass

def validate_positive_integer():
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            raise NegativeInputError("Negative input is not allowed.")
        print(f"Valid input: {num}")
    except NegativeInputError as e:
        print(e)
        log_error(e)
    except ValueError as e:
        print("Invalid input. Please enter an integer.")
        log_error(e)

# Logging Errors
def log_error(e):
    logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
    logging.error(f"Error occurred: {e}")

# ✨ Class Definition
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.__year = year

    def display_info(self):
        print(f"Car Information: {self.make} {self.model}, Year: {self.__year}")

    # Encapsulation
    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year > 1885:
            self.__year = year
        else:
            raise ValueError("Year must be after 1885.")

    # Constructor and Destructor
    def __del__(self):
        print(f"Car object {self.make} {self.model} is being deleted.")

# Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_battery_info(self):
        print(f"Battery Size: {self.battery_size} kWh")

# Test the Classes
if __name__ == "__main__":
    read_file("data.txt")
    divide_numbers()
    simulate_database_connection()
    validate_positive_integer()

    my_car = Car("Seat", "Ibiza", 2014)
    my_car.display_info()
    my_car.set_year(2024)
    print(f"Updated Year: {my_car.get_year()}")

    my_electric_car = ElectricCar("Polestar", "Model 2", 2024, 100)
    my_electric_car.display_info()
    my_electric_car.display_battery_info()

    del my_car
    del my_electric_car

# Bonus

# Advanced Logging
def advanced_log_error(e):
    logging.basicConfig(filename='advanced_error_log.txt', level=logging.ERROR, 
                        format='%(asctime)s %(levelname)s: %(message)s')
    logging.error(f"Error occurred: {e}")

# Update log_error function to use advanced logging
def log_error(e):
    advanced_log_error(e)

# Timeout Management

def network_request():
    try:
        print("Starting network request...")
        time.sleep(5)
        print("Network request completed successfully.")
    except TimeoutError as e:
        print("Network request timed out.")
        log_error(e)

# Method Overriding
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_info(self):
        super().display_info()
        print(f"Battery Size: {self.battery_size} kWh")

# Multiple Inheritance
class GPSMixin:
    def __init__(self, gps_enabled=True):
        self.gps_enabled = gps_enabled

    def display_gps_status(self):
        print(f"GPS Enabled: {self.gps_enabled}")

class AdvancedElectricCar(ElectricCar, GPSMixin):
    def __init__(self, make, model, year, battery_size, gps_enabled=True):
        ElectricCar.__init__(self, make, model, year, battery_size)
        GPSMixin.__init__(self, gps_enabled)