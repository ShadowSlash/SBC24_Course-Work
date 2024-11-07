# Advanced Python Iterators

# Custom Iterator Class
class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Test CustomIterator
custom_iter = CustomIterator([1, 2, 3, 4])
for item in custom_iter:
    print(item)

# Complex String Iterator
class UppercaseIterator:
    def __init__(self, string, stop_char):
        self.string = string
        self.stop_char = stop_char
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.string):
            char = self.string[self.index]
            if char == self.stop_char:
                raise StopIteration
            self.index += 1
            return char.upper()
        else:
            raise StopIteration

# Test UppercaseIterator
upper_iter = UppercaseIterator("hello world!", " ")
for char in upper_iter:
    print(char)

# StopIteration Handling
def handle_stop_iteration(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
            print(item)
        except StopIteration:
            break

# Test StopIteration Handling
handle_stop_iteration([1, 2, 3])

# Built-in Functions with Iterators
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for index, (item1, item2) in enumerate(zip(list1, list2)):
    print(f"Index: {index}, List1: {item1}, List2: {item2}")

# Chained Iterators
import itertools

iter1 = iter([1, 2, 3])
iter2 = iter([4, 5, 6])
chained_iter = itertools.chain(iter1, iter2)
for item in chained_iter:
    print(item)

# Python Comprehensions for Data Manipulation

# Advanced List Comprehension
odd_squares = [x**2 for x in range(1, 21) if x % 2 != 0]
print(odd_squares)

# Nested List Comprehension
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)

# Set Comprehension with Conditions
set_comp = {x**2 for x in range(10) if x % 2 == 0}
print(set_comp)

# Complex Dictionary Comprehension
dict_comp = {x: x**2 for x in range(10) if x % 2 != 0}
print(dict_comp)

# Real-World Scenario: Processing Log Data
log_data = [
    "INFO: This is an info message",
    "ERROR: This is an error message",
    "DEBUG: Debugging message",
    "ERROR: Another error message",
]

error_entries = [entry for entry in log_data if "ERROR" in entry]
print(error_entries)

# Mastering Python Loops

# List Manipulation with Loops
students = [{"name": "Alice", "grade": 90}, {"name": "Bob", "grade": 85}]
for student in students:
    print(f"Name: {student['name']}, Grade: {student['grade']}")

# Nested Loops: Multiplication Table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()

# Break and Continue Statements
valid_entries = 0
inputs = ['123', 'abc', '456', 'def', '789']
for input_str in inputs:
    if not input_str.isdigit():
        continue
    valid_entries += 1
    if valid_entries == 3:
        break
print(f"Valid entries counted: {valid_entries}")

# Looping Through a Dictionary
stock_prices = {"AAPL": 150, "GOOG": 2800, "TSLA": 700}
threshold = 1000
for stock, price in stock_prices.items():
    if price > threshold:
        print(f"{stock}: {price}")

# Data Filtering with Loops
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 != 0:
        print(number)

# Bonus

# Infinite Custom Iterator
class InfiniteIterator:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

# Test InfiniteIterator
infinite_iter = iter(InfiniteIterator())
for _ in range(10):  # print first 10 natural numbers
    print(next(infinite_iter))

# Complex Chaining
chained_iter = itertools.chain([x**2 for x in range(5)], [y**3 for y in range(3)])
for item in chained_iter:
    print(item)

# Performance Benchmark
import time

large_list = list(range(1000000))

# List comprehension
start_time = time.time()
squared_list_comp = [x**2 for x in large_list]
print("List comprehension time:", time.time() - start_time)

# For loop
start_time = time.time()
squared_list_loop = []
for x in large_list:
    squared_list_loop.append(x**2)
print("For loop time:", time.time() - start_time)

# Advanced Input Validation
user_inputs = ['123', 'abc', '456', 'def', '789']
even_count = 0
odd_count = 0
for input_str in user_inputs:
    if input_str.isdigit():
        num = int(input_str)
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")

# Time-Based Filtering
import random

stock_prices = {f"Stock{i}": random.randint(50, 2000) for i in range(20)}
filtered_stocks = {stock: price for stock, price in stock_prices.items() if price > threshold}
print(filtered_stocks)
