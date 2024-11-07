import re  # Import the re module for regex operations

# Define regex patterns for multiple scenarios
digit_pattern = r'\d+'  # Regex pattern to match one or more digits
phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'  # Regex pattern to validate phone number format (e.g., (123) 456-7890)
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Regex pattern to validate email address
url_pattern = r'https?://[^\s]+'  # Regex pattern to match URLs
date_pattern = r'\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}'  # Regex pattern to match dates (MM/DD/YYYY or YYYY-MM-DD)

# Search for the first occurrence of a pattern in a string using re.search()
sample_text = "The price is 100 dollars."  # Sample text to search within
search_result = re.search(digit_pattern, sample_text)  # Search for the first occurrence of the digit pattern in the sample text
if search_result:
    print(f"First occurrence of digit pattern: {search_result.group()}")  # Print the first occurrence of the digit pattern

# Find all matches of a pattern within a given text using re.findall() and re.finditer()
long_text = "Prices: 100, 200, and 300 dollars."  # Text with multiple digit patterns
all_digits = re.findall(digit_pattern, long_text)  # Find all occurrences of the digit pattern in the long text
print(f"\nAll digits found: {all_digits}")  # Print all occurrences of the digit pattern

# Iterate over all matches and print each match along with its position in the string
for match in re.finditer(digit_pattern, long_text):
    print(f"Match {match.group()} found at position {match.start()}")  # Print each match and its position

# Replace text using re.sub() and demonstrate the count of replacements with re.subn()
replacement_value = "XXX"  # Value to replace the digit patterns with
replaced_text = re.sub(digit_pattern, replacement_value, long_text)  # Replace all occurrences of the digit pattern
print(f"\nText after replacement: {replaced_text}")  # Print the text after replacements

# Replace and return both the new string and the number of replacements made
replaced_text_with_count = re.subn(digit_pattern, replacement_value, long_text)
print(f"Text after replacement with count: {replaced_text_with_count[0]} (Replacements made: {replaced_text_with_count[1]})")

# Tokenize strings using re.split()
sentence = "Hello, world! Welcome to advanced regex."  # Sample sentence for tokenization
tokens = re.split(r'\W+', sentence)  # Split the sentence into tokens using regex to specify non-word characters as delimiters
print(f"\nTokens: {tokens}")  # Print the list of tokens

# Validate user input for phone numbers and emails
user_phone = input("\nEnter a phone number (e.g., (123) 456-7890): ")  # Prompt the user to input a phone number
user_email = input("Enter an email address: ")  # Prompt the user to input an email address

# Validate the phone number using re.fullmatch() and provide feedback
if re.fullmatch(phone_pattern, user_phone):
    print("Valid phone number.")
else:
    print("Invalid phone number.")

# Validate the email address using re.fullmatch() and provide feedback
if re.fullmatch(email_pattern, user_email):
    print("Valid email address.")
else:
    print("Invalid email address.")

# Validate other formats like URLs or dates
user_url = input("Enter a URL: ")  # Prompt the user to input a URL
user_date = input("Enter a date (MM/DD/YYYY or YYYY-MM-DD): ")  # Prompt the user to input a date

# Validate the URL using re.fullmatch() and provide feedback
if re.fullmatch(url_pattern, user_url):
    print("Valid URL.")
else:
    print("Invalid URL.")

# Validate the date using re.fullmatch() and provide feedback
if re.fullmatch(date_pattern, user_date):
    print("Valid date.")
else:
    print("Invalid date.")

# Compile regex patterns for efficient reuse
compiled_digit_pattern = re.compile(digit_pattern)  # Compile the digit pattern for efficient reuse
compiled_phone_pattern = re.compile(phone_pattern)  # Compile the phone pattern for efficient reuse

# Use compiled patterns to search for the first occurrence of the digit pattern
compiled_search_result = compiled_digit_pattern.search(sample_text)
if compiled_search_result:
    print(f"First occurrence using compiled pattern: {compiled_search_result.group()}")

# Use re.escape() to handle special characters
special_string = "This is a test string with special characters: .^$*+?{}[]()"  # String with special regex characters
escaped_string = re.escape(special_string)  # Escape the special characters in the string
print(f"\nEscaped string: {escaped_string}")  # Print the escaped string

# Store validated information in a dictionary
validated_info = {
    "phone": user_phone.upper(),  # Store the phone number in uppercase
    "email": user_email.strip(),  # Strip any extra spaces from the email address
    "url": user_url,  # Store the URL as provided
    "date": user_date  # Store the date as provided
}

# Dictionary with validated information
print("\nValidated information:")
print(validated_info)



# Bonus Challenge 

# Advanced Pattern Matching

# Function to extract and format dates from strings in various formats (e.g., MM/DD/YYYY, YYYY-MM-DD)
def extract_dates(text):
    date_pattern = r'(\d{2}/\d{2}/\d{4})|(\d{4}-\d{2}-\d{2})'
    dates = re.findall(date_pattern, text)
    formatted_dates = [date[0] if date[0] else date[1] for date in dates]
    return formatted_dates

# Test the function with a sample text
sample_text = "Important dates are 01/15/2023, 2023-02-16, and 12/25/2023."
extracted_dates = extract_dates(sample_text)
print("Extracted dates:", extracted_dates)  # Print extracted dates

# Log File Analysis

# Function to read a log file and extract all IP addresses using regex
def extract_ip_addresses(log_text):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ip_addresses = re.findall(ip_pattern, log_text)
    return ip_addresses

# Test the function with a sample log text
log_text = """
192.168.1.1 - - [10/Jan/2023:13:55:36 +0000] "GET / HTTP/1.1" 200 612
172.16.0.5 - - [11/Jan/2023:14:56:37 +0000] "POST /data HTTP/1.1" 200 1024
"""
extracted_ips = extract_ip_addresses(log_text)
print("Extracted IP addresses:", extracted_ips)  # Print extracted IP addresses

# Create a Function Library

# Function to validate phone numbers
def validate_phone(phone):
    phone_pattern = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
    return bool(phone_pattern.fullmatch(phone))

# Function to validate emails
def validate_email(email):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    return bool(email_pattern.fullmatch(email))

# Function to validate URLs
def validate_url(url):
    url_pattern = re.compile(r'https?://[^\s]+')
    return bool(url_pattern.fullmatch(url))

# Function to validate dates
def validate_date(date):
    date_pattern = re.compile(r'\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}')
    return bool(date_pattern.fullmatch(date))

# Demonstrate usage of the function library
phone = "(123) 456-7890"
email = "test@example.com"
url = "https://example.com"
date = "2023-02-16"

print(f"Is the phone number {phone} valid? {validate_phone(phone)}")  # Validate phone number
print(f"Is the email address {email} valid? {validate_email(email)}")  # Validate email address
print(f"Is the URL {url} valid? {validate_url(url)}")  # Validate URL
print(f"Is the date {date} valid? {validate_date(date)}")  # Validate date