# Create a nested dictionary
people = {
    "person1": {"name": "Leo", "age": 28, "email": "leo@example.com"},
    "person2": {"name": "Vitor", "age": 35, "email": "vitor@example.com"},
    "person3": {"name": "Jason", "age": 28, "email": "jason@example.com"},
    "person4": {"name": "Sai", "age": 32, "email": "sai@example.com"}
}

# Initial dictionary
print("Initial dictionary:")
print(people)
# 'person1': {'name': 'Leo', 'age': 28, 'email': 'leo@example.com'} 
# 'person2': {'name': 'Vitor', 'age': 35, 'email': 'vitor@example.com'}
# 'person3': {'name': 'Jason', 'age': 28, 'email': 'jason@example.com'}
# 'person4': {'name': 'Sai', 'age': 32, 'email': 'sai@example.com'}

# Dynamically add key-value pairs using a loop
for i, person in enumerate(people.values(), start=1):
    person["id"] = i  # Add a unique ID to each person

# Dictionary after adding unique IDs
print("\nAfter adding unique IDs:")
print(people)
# 'person1': {'name': 'Leo', 'age': 28, 'email': 'leo@example.com', 'id': 1}
# 'person2': {'name': 'Vitor', 'age': 35, 'email': 'vitor@example.com', 'id': 2
# 'person3': {'name': 'Jason', 'age': 28, 'email': 'jason@example.com', 'id': 3
# 'person4': {'name': 'Sai', 'age': 32, 'email': 'sai@example.com', 'id': 4}

# Merge dictionaries
additional_people = {
    "person5": {"name": "Eve", "age": 29, "email": "eve@example.com"},
    "person6": {"name": "Frank", "age": 33, "email": "frank@example.com"}
}

# If a key exists in both dictionaries, decide how to handle the conflict (update in this case)
people.update(additional_people)  # Merge the additional_people dictionary into the people dictionary

# Dictionary after merging
print("\nAfter merging with additional_people:")
print(people)
# Previous persons +
# 'person5': {'name': 'Eve', 'age': 29, 'email': 'eve@example.com'}
# 'person6': {'name': 'Frank', 'age': 33, 'email': 'frank@example.com'}

# Conditional updates
for person in people.values():
    if person["age"] > 30:  # Only update if the person's age is greater than 30
        person["status"] = "Senior"  # Add a status key with the value "Senior"

# Dictionary after conditional updates
print("\nAfter conditional updates (age > 30):")
print(people)
# 'person1': {'name': 'Leo', 'age': 28, 'email': 'leo@example.com', 'id': 1}
# 'person2': {'name': 'Vitor', 'age': 35, 'email': 'vitor@example.com', 'id': 2, 'status': 'Senior'}
# 'person3': {'name': 'Jason', 'age': 28, 'email': 'jason@example.com', 'id': 3}
# 'person4': {'name': 'Sai', 'age': 32, 'email': 'sai@example.com', 'id': 4, 'status': 'Senior'}
# 'person5': {'name': 'Eve', 'age': 29, 'email': 'eve@example.com'}
# 'person6': {'name': 'Frank', 'age': 33, 'email': 'frank@example.com', 'status': 'Senior'}