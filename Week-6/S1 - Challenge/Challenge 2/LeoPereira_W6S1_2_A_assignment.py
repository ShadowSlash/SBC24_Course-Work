# List
# Creating and giving value to the list (Array).
type_animals = ["cat", "dog", "hamster", "fish"]
print(type_animals) # = ['cat', 'dog', 'hamster', 'fish']

# Accessing a specific element.
fav_animal = type_animals[0]
print(fav_animal) # = cat

# Updating an element to a different value.
type_animals[2] = "platypus"
print(type_animals) # = ['cat', 'dog', 'platypus', 'fish']

# Creating a sub-array by slicing.
least_fav = type_animals[2:4]
print(least_fav) # = ['platypus', 'fish']

# Adding a new element to the end of the array.
type_animals.append("python")
print(type_animals) # = ['cat', 'dog', 'platypus', 'fish', 'python']

# Removing an element from the array.
type_animals.remove("fish")
print(type_animals) # = ['cat', 'dog', 'platypus', 'python']


# Utilize all array methods
type_trees = ["oak", "birch", "cedar", "cherry", "pine", "redwood", "birch", "oak", "cherry", "oak"]

# pop()
type_trees.pop(2)
print(type_trees) # = ["oak", "birch", "cherry", "pine", "redwood", "birch", "oak", "cherry", "oak"]

# Insert()
type_trees.insert(0, "alder")
print(type_trees) # = ['alder', 'birch', 'birch', 'cherry', 'cherry', 'oak', 'oak', 'oak', 'pine', 'redwood']

# Extend()
type_trees.extend("mapple")
print(type_trees) # = ['alder', 'oak', 'birch', 'cherry', 'pine', 'redwood', 'birch', 'oak', 'cherry', 'oak', 'm', 'a', 'p', 'p', 'l', 'e']

# Index()
index_num = type_trees.index("pine")
print(index_num) # = [4]

# Sort()
type_trees.sort()
print(type_trees) # = ['birch', 'birch', 'cherry', 'cherry', 'oak', 'oak', 'oak', 'pine', 'redwood']

# Reverse()
type_trees.reverse()
print(type_trees) # = ['redwood', 'pine', 'oak', 'oak', 'oak', 'cherry', 'cherry', 'birch', 'birch']

# Count()
num_of = type_trees.count("cherry")
print(num_of) # = 2

# Clear()
type_trees.clear()
print(type_trees) # = []