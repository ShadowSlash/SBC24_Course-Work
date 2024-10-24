# 🐍 **Assignment: Advanced Python Sets Operations**

## 🎯 **Objective**

Your task is to create a Python program that demonstrates advanced usage of sets in Python. This assignment will challenge you to apply the set operations covered in the previous examples and enhance your understanding of set theory in Python.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 🧩 Understand how to use **sets** effectively for managing unique collections of data.
- 🔄 Practice performing **set operations** like union, intersection, and difference.
- 🚀 Learn to dynamically create sets and manipulate them programmatically.
- 🎛️ Explore advanced set functions, such as **adding and removing** elements, and working with **set comprehension**.

## 👤 **User Story**

As a developer, I want to manipulate sets to handle collections of unique data and perform operations like union, intersection, and difference so that I can work with sets efficiently in Python.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** `YOURNAME_W6S2_3_A_assignment.py`.
- The script should demonstrate the following:
  - ✨ **Dynamically generate two sets** with random numbers or a range of integers.
  - ➕ **Perform set operations**:
    - **Union**: Combine elements from both sets, removing duplicates.
    - **Intersection**: Identify elements common to both sets.
    - **Difference**: Show elements in the first set that are not in the second.
  - ➕ **Modify the sets** by adding and removing elements.
  - ✨ **Set Comprehension**: Use a set comprehension to generate a new set that contains only even numbers from the first set.
  - 🔄 **Loop** through one of the sets and dynamically add elements.
  - 📏 Ensure proper **set operations syntax** and code structure are followed.
  - 💬 The code must be properly commented and organized for clarity.

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it `YOURNAME_W6S2_3_A_assignment.py`.
2. **🖊️ Generate two sets**:
   - Create two sets using either `range()` or random numbers using Python’s `random` module.
   - Example: 
     ```python
     import random
     set1 = set(random.randint(1, 10) for _ in range(5))
     set2 = set(random.randint(5, 15) for _ in range(5))
     ```
3. **🔄 Perform set operations**:
   - Use union, intersection, and difference to manipulate the sets.
   - Print the results for each operation.
4. **➕ Add and remove elements**:
   - Add a new number to one of the sets using `.add()`.
   - Remove a number from one of the sets using `.remove()` (ensure the element exists).
5. **✨ Use set comprehension**:
   - Generate a new set containing only **even numbers** from one of the original sets using set comprehension.
6. **📤 Print the output**:
   - Use `print()` to show the result of each operation and the final state of your sets.
7. **💬 Comment your code**: Ensure that each section of the script is properly commented for clarity.

## 📝 **Example Output**

The output should look something like this:

```python
Set 1: {1, 3, 5, 6, 8}
Set 2: {8, 9, 5, 6, 7}
Union of Set 1 and Set 2: {1, 3, 5, 6, 7, 8, 9}
Intersection of Set 1 and Set 2: {8, 5, 6}
Difference (Set 1 - Set 2): {1, 3}
Set 1 after adding 10: {1, 3, 5, 6, 8, 10}
Set 1 after removing 10: {1, 3, 5, 6, 8}
Even numbers in Set 1: {6, 8}
```

## 📎 **Additional Resources**

- [Python Sets Documentation](https://www.w3schools.com/python/python_variables.asp)
- [Python Set Comprehension Explained](https://www.geeksforgeeks.org/set-comprehension-in-python-with-examples/)
- [Python Random Module](https://realpython.com/python-random/)

Happy coding, and good luck Geeks!