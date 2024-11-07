import random # Import the random module to generate random numbers

# Generate two sets
set1 = set(random.randint(1, 25) for _ in range(5))  # Create a set with 5 random numbers between 50 and 100
set2 = set(random.randint(15, 35) for _ in range(5))    # Create a set with 5 random numbers between 15 and 35

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Perform set operations
union_set = set1.union(set2) # Union: Combine elements from both sets, removing duplicates
intersection_set = set1.intersection(set2) # Intersection: Identify elements common to both sets
difference_set = set1.difference(set2) # Difference: Show elements in set1 that are not in set2

print(f"Union of Set 1 and Set 2: {union_set}")
print(f"Intersection of Set 1 and Set 2: {intersection_set}")
print(f"Difference (Set 1 - Set 2): {difference_set}")

# Add and remove elements
set1.add(105)  # Add the number 105 to set1
set1.remove(105)  # Remove the number 105 from set1

print(f"Set 1 after adding 105: {set1}")
print(f"Set 1 after removing 105: {set1}")

# Set comprehension
even_numbers_set = {num for num in set1 if num % 2 == 0} # Create a new set with even numbers from set1

print(f"Even numbers in Set 1: {even_numbers_set}")

# Loop through the set and dynamically add elements
for num in range(25, 50):
    set1.add(num) # Add numbers 25 to 50 to set1