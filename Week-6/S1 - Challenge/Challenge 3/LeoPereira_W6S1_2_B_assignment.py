
# Initialize tuples
person_info = ("Leo", "Pereira", 28, "Sandown")
coordinates = (50.6517, -1.1610)  # Coordinates for Sandown
print(f"Person info: {person_info}") # = Person info: ('Leo', 'Pereira', 28, 'Sandown')
print(f"Coordinates: {coordinates}") # = Coordinates: (50.6517, -1.161)

# Access and unpack elements
first_name, last_name, age, city = person_info
print(f"Unpacked elements: {first_name, last_name, age, city}") # = Unpacked elements: Leo Pereira 28 Sandown

# Slice the tuple
person_info_slice = person_info[:2]  # First two elements
print(f"Tuple slice: {person_info_slice}") # = Tuple slice: ('Leo', 'Pereira')

# Concatenate and repeat tuples
combined_tuple = person_info + coordinates
repeated_tuple = coordinates * 3
print(f"Concatenated tuple: {combined_tuple}") # = Concatenated tuple: ('Leo', 'Pereira', 28, 'Sandown', 50.6517, -1.161)
print(f"Repeated tuple: {repeated_tuple}") # = Repeated tuple: (50.6517, -1.161, 50.6517, -1.161, 50.6517, -1.161)

# Use tuple methods
trees = ("oak", "pine", "maple", "oak", "birch")
oak_count = trees.count("oak")
index_of_maple = trees.index("maple")
print(f"Count of 'oak': {oak_count}") # = Count of 'oak': 2
print(f"Index of 'maple': {index_of_maple}") # = Index of 'maple': 2

# Real-world application: Return multiple values
def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

rectangle_result = rectangle_properties(5, 3)
print(f"Rectangle area and perimeter: {rectangle_result}") # = Rectangle area and perimeter: (15, 16)