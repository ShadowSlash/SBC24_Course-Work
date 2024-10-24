
# String Variables / Immutable
full_name = "Leo Pereira"
print(full_name)

# Integer Variables / Immutable
days_alive = 10372
print(days_alive)

# Float Variables / Immutable
height = 6.0
print(height)

# Boolean Variables / Immutable
is_student = True
print(is_student)

# Constants / Immutable

HOUR = 60 # 60 minutes in an hour.
DAY = 24 # 24 hours in a day.
YEAR = 365.55 # 365.55 days in a year.

print(f"Minutes in a day: {HOUR}")
print(f"Hours in a day: {DAY}")
print(f"Days in a year: {YEAR}")

# Dictionary / Mutable

my_dictionary = {
    "Fullname": full_name,
    "Days Lived": days_alive,
    "Height": height,
    "Learning": is_student
}
print(my_dictionary)

# Tupple / Immutable

shopping_list = ("steak", "onions", "garlic", "cream", "mushrooms", "potatoes", "broccoli")
print(shopping_list)

# List / Mutable

my_cars = ["mercedes", "seat ibiza", "seat toca", "peugeot", "mitsubishi"]
print(my_cars)

# Modifying List

# This adds another car to the list.
my_cars.append("impala")
print(my_cars)

# This selects my favourite car from the list.
fav_car = my_cars[5]
print(f"Favourite Car: {fav_car}")

# This removes 2 items from the list.
my_cars.remove("seat toca")
my_cars.remove("peugeot")
print(my_cars)

# Modifying Integer

avg_life = 26645
print(f"Average lifespan in days: {avg_life}") # This prints the first integer value 
avg_life -= days_alive
print(f"Days left: {avg_life}") # This prints the same variable after it being modified with the value of a previous integer. Creating a new object