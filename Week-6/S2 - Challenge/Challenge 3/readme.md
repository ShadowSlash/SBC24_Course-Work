# 🐍 Advanced Python JSON Assignment

## 🎯 Challenge

Your challenge is to create a Python script that demonstrates advanced handling of JSON data. This includes not only parsing and modifying JSON, but also deeply nested structures, complex data types, and integrating exception handling for robust file operations. Additionally, you will implement dynamic manipulation of the JSON structure by adding, updating, deleting, and querying specific elements in deeply nested objects.

## 📚 Key Learnings

By completing this exercise, you will learn:

- Advanced parsing and manipulation of JSON data.
- Handling deeply nested JSON objects and arrays.
- Working with complex data structures in JSON.
- Exception handling with file operations for reading and writing JSON data.
- Best practices for JSON validation and error handling.

## 👤 User Story

As an advanced Python developer, I want to work with complex JSON objects, handle nested data structures, and dynamically update JSON files. Additionally, I want to ensure that my code can handle unexpected file and data errors.

## ✅ Acceptance Criteria

- The Python script is named `YOURNAME_W6S2_3_C_assignment.py`.
- The script demonstrates:
  - Parsing deeply nested JSON data from a file or string.
  - Accessing and modifying nested JSON elements.
  - Adding and removing elements from both top-level and nested structures.
  - Validating the structure of JSON files before reading or writing.
  - Handling exceptions for file operations (e.g., file not found, file permissions, invalid JSON).
  - Writing the modified JSON back to a file in a formatted way.
  - Dynamic querying of JSON data based on user input (e.g., retrieve values by keys).

## 🛠️ Steps to Complete

### Part 1: Working with Complex JSON Structures

1. **📁 Create a new Python file**: Name the file `YOURNAME_W6S2_3_C_assignment.py`.

2. **🖊️ Initialize Complex JSON Data**: 
    - Use a JSON string that includes multiple levels of nested objects and arrays.
    - Example JSON structure:
      ```json
      {
          "company": {
              "name": "TechCorp",
              "departments": [
                  {
                      "name": "Engineering",
                      "employees": [
                          {"name": "Alice", "role": "Engineer", "skills": ["Python", "C++"]},
                          {"name": "Bob", "role": "Engineer", "skills": ["JavaScript", "Node.js"]}
                      ]
                  },
                  {
                      "name": "Sales",
                      "employees": [
                          {"name": "Charlie", "role": "Sales Manager", "skills": ["Negotiation", "Communication"]},
                          {"name": "Dana", "role": "Sales Associate", "skills": ["Customer Service", "CRM"]}
                      ]
                  }
              ]
          }
      }
      ```

3. **🔍 Parse the JSON Data**: 
    - Parse this JSON string into a Python dictionary using `json.loads()`.
    - Print specific elements, like all employee names under the "Engineering" department.

4. **✏️ Modify Nested JSON**:
    - Add a new employee under the "Engineering" department with their skills.
    - Update an existing employee's role or skill set dynamically (e.g., ask the user for an employee name and update their role or skills).
    - Remove an employee from the "Sales" department using a nested key lookup.

5. **🔄 Query JSON by User Input**:
    - Create a function that allows the user to input a department name and retrieve all employee names within that department.
    - If the department doesn’t exist, handle it gracefully by providing an appropriate message.

### Part 2: File Handling and Error Management

6. **📖 Read Nested JSON Data from a File**:
    - Read a complex JSON structure from a file (`input_complex.json`). Ensure the file is properly formatted, and if not, handle the `json.JSONDecodeError`.
    - If the file doesn’t exist, handle the `FileNotFoundError` and print an error message.
    - Check if the JSON data conforms to the expected structure (e.g., check if "departments" exists).

7. **✏️ Modify and Validate JSON Data**:
    - Before making changes, validate that the key fields (e.g., "company", "departments", "employees") exist in the JSON structure.
    - Use `try-except` blocks to catch any issues while accessing nested elements (e.g., trying to access an employee that doesn’t exist).

8. **📤 Write Modified JSON to a File**:
    - Write the modified dictionary back to a new file (`output_complex.json`), ensuring the JSON is properly formatted using `indent=4`.
    - If the file cannot be written (e.g., due to permissions issues), handle the exception and inform the user.

### Part 3: Dynamic Interaction with the JSON Structure

9. **🔄 Implement Dynamic Querying**:
    - Allow the user to input a key path (e.g., `"company > departments > Engineering > employees > Alice > skills"`) and retrieve or update the value at that path.
    - If the path doesn’t exist, handle it gracefully and provide a clear error message.

10. **📤 JSON Validation**:
    - Before writing JSON data to the file, create a function that checks whether the modified JSON conforms to the expected structure. If the structure is invalid, print an error message and prevent writing to the file.

## 🚩 Bonus Challenges

- **Exception Handling for Edge Cases**: 
    - Handle cases where the JSON is too deeply nested or where arrays have unexpected data types.
    - Raise custom exceptions if the JSON structure does not meet expectations.

- **Dynamic Modification of JSON**: 
    - Create a feature where the user can add new departments, employees, or skills dynamically via input and have it reflected in the final JSON file.

- **Custom JSON Validation Function**:
    - Implement a custom validation function that ensures the JSON file matches a specific schema. If the structure is invalid, print the issues and prevent any further modifications.

## Tips

- Utilize Python’s `json` module to manage JSON efficiently.
- Use exception handling (`try-except`) to catch and handle errors when accessing or modifying nested data.
- JSON objects can store arrays, dictionaries, and other complex types, so make sure your code can handle these nested structures.
- Use recursion for dynamic querying or modification of deeply nested JSON elements.

## Additional Resources

- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Working with Nested JSON in Python](https://realpython.com/python-json/)
- [Best Practices for Handling JSON in Python](https://www.geeksforgeeks.org/python-json/)
- [Validating JSON Structures](https://json-schema.org/)

## Submission

Once you complete the task, submit the `YOURNAME_W6S2_3_C_assignment.py` and `output_complex.json` files.

Good luck, and happy coding techies! 🚀