# 🐍 **Assignment: Mastering Python Regular Expressions with Comprehensive Text Processing**

## 🎯 **Objective**

Your task is to create a Python program that demonstrates your advanced understanding of regular expressions (regex) for complex text processing and validation. This assignment will challenge you to utilize various regex functions, string manipulations, and user input validations, incorporating learned concepts from previous topics.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 🔍 Understand how to define and use regex patterns in Python for various applications.
- 🕵️ Learn to search for, find, and validate patterns in strings effectively.
- 🔄 Practice replacing text and formatting strings using regex.
- 📞 Validate multiple string formats using regex (e.g., phone numbers, emails).
- 🔗 Implement dictionaries and user input to dynamically validate and process text.
- 📊 Explore capturing groups in regex for data extraction and manipulation.
- 🌐 Discover and utilize all regex methods available in Python, including `re.search()`, `re.match()`, `re.fullmatch()`, `re.findall()`, `re.finditer()`, `re.sub()`, `re.subn()`, `re.split()`, `re.compile()`, `re.escape()`, and more.

## 👤 **User Story**

As a developer, I want to validate and manipulate text data using regular expressions and other string techniques so that I can ensure the correctness of user inputs and perform complex text transformations efficiently.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** `YOURNAME_W6S2_4_B_assignment.py`.
- The script should demonstrate the following:
  - ✨ Definition of regex patterns for multiple scenarios (e.g., digits, phone numbers, email addresses).
  - 🚩 Searching for the first occurrence of a pattern in a string using `re.search()`.
  - 🌀 Finding all matches of a pattern within a given text using `re.findall()` and `re.finditer()`.
  - 🔄 Replacing text using `re.sub()` and demonstrating the count of replacements with `re.subn()`.
  - 💡 Tokenizing strings using `re.split()`.
  - 📞 Validating multiple formats (e.g., phone numbers and email addresses) using `re.match()`, `re.fullmatch()`, and providing meaningful feedback.
  - ✍️ Compiling regex patterns for efficient reuse using `re.compile()`.
  - 📝 Using `re.escape()` to safely escape special characters in strings.
  - 🧩 Demonstrating capturing groups for data extraction and manipulation.
  - 🛠️ Storing extracted and validated information in a dictionary for further processing.
  - 💬 The code must be well-commented and organized for clarity.

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it `YOURNAME_W6S2_4_B_assignment.py`.
2. **🔍 Define regex patterns**:
   - Create a regex pattern to match one or more digits (`\d+`).
   - Define a regex pattern to validate a phone number format (e.g., `(123) 456-7890`).
   - Create a regex pattern for validating email addresses (e.g., `username@example.com`).
   - Include patterns for additional scenarios such as:
     - URLs (e.g., `https?://[^\s]+`)
     - Dates (e.g., `\d{2}/\d{2}/\d{4}` or `\d{4}-\d{2}-\d{2}`)
3. **🔎 Search for patterns**:
   - Use `re.search()` to find the first occurrence of the digit pattern in a given text and print the result along with the entire matching string.
4. **🔍 Find all matches**:
   - Use `re.findall()` to extract all occurrences of the digit pattern from a longer text (e.g., prices in a sentence) and handle potential edge cases (e.g., negative numbers, decimals).
   - Demonstrate `re.finditer()` to iterate over all matches and print each match along with its position in the string.
5. **🔄 Replace text**:
   - Use `re.sub()` to replace all occurrences of the digit pattern with a dynamic value provided by the user (e.g., replace prices with a user-specified amount) and print the updated text.
   - Explore `re.subn()` to see how many replacements were made and print the count along with the updated text.
6. **🔗 Tokenize strings**:
   - Use `re.split()` to tokenize a sentence into words, using regex to specify delimiters (e.g., spaces, punctuation).
   - Print the list of tokens and demonstrate how to clean the tokens by removing any unwanted characters.
7. **📞 Validate user input**:
   - Prompt the user to input a phone number and an email address. Use `re.fullmatch()` to check if the inputs match their respective regex patterns. Provide detailed feedback indicating whether the inputs are valid or invalid.
   - Validate other formats, such as URLs or dates, based on the patterns you defined.
8. **🔄 Compile patterns**:
   - Use `re.compile()` to compile your regex patterns and reuse them in your search and validation functions. This will improve efficiency and clarity in your code.
9. **🔄 Escape special characters**:
   - Use `re.escape()` to demonstrate how to handle strings with special regex characters by escaping them properly.
10. **📚 Store validated information**:
   - Create a dictionary to store the validated phone number, email, and any other relevant extracted information (e.g., name, age). Format the values using string methods (e.g., convert to uppercase, strip whitespace).
11. **💬 Comment your code**: Ensure that each section of the script is properly commented for clarity.

## 📎 **Additional Resources**

- [Python Regular Expressions Documentation](https://docs.python.org/3/library/re.html)
- [Regular Expressions Cheat Sheet](https://www.rexegg.com/regex-quickstart.html)
- [Regex101: Online Regex Tester](https://regex101.com/)
- [Python String Methods](https://www.programiz.com/python-programming/methods/string)
- [Python Dictionaries Documentation](https://www.w3schools.com/python/python_dictionaries.asp)

## 💡 **Bonus Challenges (Optional)**

- **📊 Advanced Pattern Matching**: Explore regex patterns to extract and format dates from strings in various formats (e.g., `MM/DD/YYYY`, `YYYY-MM-DD`).
- **📃 Log File Analysis**: Create a small function that reads a log file and extracts all IP addresses using regex, storing them in a list or dictionary.
- **🔍 Create a Function Library**: Develop a library of functions that encapsulate common regex operations (e.g., validation functions for phone numbers, emails, and custom formats) and demonstrate their usage in your main script.

Happy coding, and good luck, folks guys!