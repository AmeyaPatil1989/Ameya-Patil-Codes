# # Example # 1

# def main():
#     print("Hello, World!")

# if __name__ == '__main__':
#     main()

# # Exdample # 2

# import sys

# # Accessing command-line arguments
# print("Command-line arguments:", sys.argv)

# # Printing Python version
# print("Python version:", sys.version)

# # Exiting the program
# # sys.exit("Exiting the program")

# # Example # 3

# import sys

# def main():
#     if len(sys.argv) > 1:
#         print("Arguments:", sys.argv[1:])
#     else:
#         print("No arguments provided.")

# if __name__ == '__main__':
#     main()

# # Example # 4
# # Basic Main Function

# def main():
#     print("Hello, World!")

# if __name__ == '__main__':
#     main()

# # Example # 5
# # Main Guard Check

# def main():
#     print("Running as a standalone program.")

# if __name__ == '__main__':
#     main()

# Example # 6
# Calling Sub-Functions Within Main

# def greet():
#     print("Hello from greet()!")

# def main():
#     greet()

# if __name__ == '__main__':
#     main()

# # Example # 7
# # Multiple Sub-function Calls

# def greet():
#     print("Hello!")

# def farewell():
#     print("Goodbye!")

# def main():
#     greet()
#     farewell()

# if __name__ == '__main__':
#     main()

# # Example # 8
# #Error Handling in Main

# def main():
#     try:
#         result = 10 / 0
#     except ZeroDivisionError:
#         print("Error: Division by zero occurred.")

# if __name__ == '__main__':
#     main()

# Example # 9
#Parameter Passing in Main


# def main(x, y):
#     print("Sum:", x + y)

# if __name__ == '__main__':
#     main(x = int(input()), y=int(input()))

# # Example # 10
# # Default Parameter Values

# def main(x=10, y=20):
#     print("Sum with defaults:", x + y)

# if __name__ == '__main__':
#     main()


# # Example # 11
# # Using Environment Variables in Main

# import os

# def main():
#     home = os.getenv("HOME", "Not Set")
#     print("HOME directory:", home)

# if __name__ == '__main__':
#     main()

# # Example # 12
# #Multiprocessing Task

# import multiprocessing

# def worker(num):
#     print(f"Worker processing number: {num}")

# def main():
#     p = multiprocessing.Process(target=worker, args=(42,))
#     p.start()
#     p.join()

# if __name__ == '__main__':
#     main()


# List Example # 1
# Creating a List

# my_list = [1, 2, 3, 4, 5]
# print(my_list)

# # List Example # 2
# #Creating a List of Strings

# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# # List Example # 3
# # Iteration Using a For Loop

# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# for fruit in fruits:
#     print(fruit)

# # List Example # 4
# #Generate a list of squares from 1 to 5

# squares = [x**2 for x in range(1, 6)]
# print(squares)

# # List Example # 5
# #Modifying Lists (Adding)

# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# print(fruits)

# # List Example # 6
# #  Inserting an Element at a Specific Index

# fruits = ["apple", "banana", "cherry"]
# fruits.insert(1, "kiwi")
# print(fruits)

# # List Example # 7
# # Removing Elements from a List
# # Removing an Element by Value

# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)

# # List Example # 8
# # Removing an Element by Index

# fruits = ["apple", "banana", "cherry"]
# fruits.pop(0)
# print(fruits)

# # List Example # 9
# # Sorting a List

# fruits = ["banana", "apple", "cherry"]
# fruits.sort()
# print(fruits)

# # List Example # 10
# # Reversing a List

# fruits = ["banana", "apple", "cherry"]
# fruits.reverse()
# print(fruits)

# # List Example # 11
# # List Length

# fruits = ["banana", "apple", "cherry"]
# print("Length of list:", len(fruits))

# # List Example # 12
# # List Slicing

# fruits = ["banana", "apple", "cherry", "orange", "kiwi"]
# print("Sliced list:", fruits[1:4])  # Output: ['apple', 'cherry', 'orange']

# # List Example # 13
# # finding the Index of an Element

# fruits = ["banana", "apple", "cherry"]
# index = fruits.index("cherry")
# print("Index of 'cherry':", index)  # Output: 2

# # List Example # 14
# # creating a nested list

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("Nested list:", nested_list)

# # List Example # 15
# #assesing elements in a nested list

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("Element at [1][2]:", nested_list[1][2])  # Output: 6

# # Tuple Example # 1
# # Creating a Tuple

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)

# # Tuple Example # 2
# # Creating a Tuple with Mixed Data Types

# mixed_tuple = (1, "apple", 3.14, True)
# print(mixed_tuple)

# # Tuple Example # 3
# # Accessing Tuple Elements

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[0])  # Output: 1
# print(my_tuple[2])  # Output: 3

# # Tuple Example # 4
# # Iterating Through a Tuple

# my_tuple = (1, 2, 3, 4, 5)
# for item in my_tuple:
#     print(item)

# # Tuple Example # 5
# # Tuple Length

# my_tuple = (1, 2, 3, 4, 5)
# print("Length of tuple:", len(my_tuple))

# # Tuple Example # 6
# # Tuple Slicing

# my_tuple = (1, 2, 3, 4, 5)
# print("Sliced tuple:", my_tuple[1:4])  # Output: (2, 3, 4)

# # Tuple Example # 7
# # Nested Tuple
# nested_tuple = ((1, 2), (3, 4), (5, 6))
# print("Nested tuple:", nested_tuple)

# # Tuple Example # 8
# # Unpacking a Tuple

# my_tuple = (1, 2, 3)
# a, b, c = my_tuple
# print("Unpacked values:", a, b, c)  # Output: 1 2 3

# # Tuple Example # 9
# # Tuple with One Element

# single_element_tuple = (1,)
# print("Single element tuple:", single_element_tuple)  # Output: (1,)

# # Tuple Example # 10
# # Concatenating Tuples

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# concatenated = tuple1 + tuple2
# print("Concatenated tuple:", concatenated)  # Output: (1, 2, 3, 4, 5, 6)

# # Tuple Example # 11
# #enumerate a tuple
# my_tuple = ("apple", "banana", "cherry")
# for index, value in enumerate(my_tuple):
#     print(index, value)

# # Tuple Example # 12
# # Tuple Methods
# my_tuple = (1, 2, 3, 2, 1)
# count_of_1 = my_tuple.count(1)
# index_of_2 = my_tuple.index(2)
# print("Count of 1:", count_of_1)  # Output: 2
# print("Index of 2:", index_of_2)  # Output: 1

# #tuple Example # 13
# #tuplle in functions
# def add_numbers(numbers):
#     return sum(numbers)
# numbers_tuple = (1, 2, 3, 4, 5)
# result = add_numbers(numbers_tuple)
# print("Sum of tuple elements:", result)  # Output: 15

# # Dictionary Example # 1   
# # Creating a Dictionary

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# print(my_dict)

# # Dictionary Example # 2
# # Accessing Dictionary Values

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# print(my_dict["name"])  # Output: Alice
# print(my_dict["age"])   # Output: 30

# # Dictionary Example # 3
# # Adding Key-Value Pairs
# my_dict = {"name": "Alice", "age": 30}
# my_dict["city"] = "New York"
# print(my_dict)

# # Dictionary Example # 4
# # Modifying Values
# my_dict = {"name": "Alice", "age": 30}
# my_dict["age"] = 31
# print(my_dict)

# # Dictionary Example # 5
# # Removing Key-Value Pairs
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# del my_dict["age"]
# print(my_dict)

# # Dictionary Example # 6
# # Iterating Through a Dictionary

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# for key, value in my_dict.items():
#     print(key, ":", value)

# # Dictionary Example # 7
# # Dictionary Length

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# print("Length of dictionary:", len(my_dict))

# # Dictionary Example # 8
# # Checking if a Key Exists

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# if "name" in my_dict:
#     print("Key 'name' exists in the dictionary.")
# else:
#     print("Key 'name' does not exist in the dictionary.")

# # Dictionary Example # 9    
# # Dictionary with Mixed Data Types
# mixed_dict = {"name": "Alice", "age": 30, "is_student": False}
# print(mixed_dict)

# # Dictionary Example # 10
# # Nested Dictionary
# nested_dict = {"person": {"name": "Alice", "age": 30}, "city": "New York"}
# print(nested_dict)

# # Dictionary Example # 11
# # Dictionary Methods
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# keys = my_dict.keys()
# values = my_dict.values()
# items = my_dict.items()
# print("Keys:", keys)    # Output: dict_keys(['name', 'age', 'city'])
# print("Values:", values)  # Output: dict_values(['Alice', 30, 'New York'])
# print("Items:", items)    # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# # Dictionary Example # 12
# # Merging Two Dictionaries
# dict1 = {"name": "Alice", "age": 30}
# dict2 = {"city": "New York", "country": "USA"}
# merged_dict = {**dict1, **dict2}

# print("Merged dictionary:", merged_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

# # Dictionary Example # 13
# # Dictionary Comprehension
# squared_dict = {x: x**2 for x in range(5)}
# print("Squared dictionary:", squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# # Dictionary Example # 14
# # Dictionary with Default Values

# from collections import defaultdict
# default_dict = defaultdict(int)
# default_dict["a"] += 1
# default_dict["b"] += 2
# print("Default dictionary:", default_dict)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})

# # Dictionary Example # 15
# # Dictionary with Tuple Keys

# tuple_dict = {("x", "y"): 1, ("a", "b"): 2}
# print("Dictionary with tuple keys:", tuple_dict)  # Output: {('x', 'y'): 1, ('a', 'b'): 2}

# # Dictionary Example # 16
# # Dictionary with List Values

# list_dict = {"fruits": ["apple", "banana"], "vegetables": ["carrot", "broccoli"]}
# print("Dictionary with list values:", list_dict)  # Output: {'fruits': ['apple', 'banana'], 'vegetables': ['carrot', 'broccoli']}

# # Dictionary Example # 17
# # Dictionary with Set Values

# set_dict = {"fruits": {"apple", "banana"}, "vegetables": {"carrot", "broccoli"}}
# print("Dictionary with set values:", set_dict)  # Output: {'fruits': {'banana', 'apple'}, 'vegetables': {'carrot', 'broccoli'}}

# #String Example # 1
# # Creating a String

# my_string = "Hello, World!"
# print(my_string)

# # String Example # 2
# # Accessing String Characters

# my_string = "Hello, World!"
# print(my_string[0])  # Output: H

# # String Example # 3
# # String Length

# my_string = "Hello, World!"
# print("Length of string:", len(my_string))

# # String Example # 4
# # String Slicing
# my_string = "Hello, World!"
# print("Sliced string:", my_string[0:5])  # Output: Hello

# # String Example # 5
# # String Concatenation
# string1 = "Hello"
# string2 = "World"
# concatenated = string1 + ", " + string2 + "!"
# print("Concatenated string:", concatenated)  # Output: Hello, World!

# # String Example # 6
# # String Repetition

# my_string = "Hello"
# repeated = my_string * 3
# print("Repeated string:", repeated)  # Output: HelloHelloHello

# # String Example # 7
# # String Methods

# my_string = "Hello, World!"
# print("Uppercase:", my_string.upper())  # Output: HELLO, WORLD!
# print("Lowercase:", my_string.lower())  # Output: hello, world!
# print("Title Case:", my_string.title())  # Output: Hello, World!
# print("Split:", my_string.split(", "))  # Output: ['Hello', 'World!']
# print("Join:", ", ".join(['Hello', 'World!']))  # Output: Hello, World!
# print("Replace:", my_string.replace("World", "Python"))  # Output: Hello, Python!
# print("Find:", my_string.find("World"))  # Output: 7
# print("Count:", my_string.count("o"))  # Output: 2
# print("Starts with 'Hello':", my_string.startswith("Hello"))  # Output: True
# print("Ends with '!':", my_string.endswith("!"))  # Output: True

# # String Example # 8
# # String Formatting
# name = "Alice"
# age = 30
# formatted_string = f"My name is {name} and I am {age} years old."
# print("Formatted string:", formatted_string)  # Output: My name is Alice and I am 30 years old.

# # String Example # 9
# # String Escape Characters
# escaped_string = "Hello, \"World\"!\nNew line here."
# print("Escaped string:", escaped_string)

# # String Example # 10
# # String Comparison
# string1 = "apple"
# string2 = "banana"
# if string1 < string2:
#     print(f"{string1} is less than {string2}")
# else:
#     print(f"{string1} is greater than or equal to {string2}")

# # String Example # 11
# # String Iteration

# my_string = "Hello"
# for char in my_string:
#     print(char)

# # String Example # 12
# #multiple line string

# multi_line_string = """This is a string
# that spans multiple lines.  
# It can be useful for documentation."""
# print(multi_line_string)

# # String Example # 13  
# # String to List Conversion

# my_string = "apple,banana,cherry"
# my_list = my_string.split(",")

# print("List from string:", my_list)  # Output: ['apple', 'banana', 'cherry']

# # String Example # 14
# # List to String Conversion

# my_list = ['apple', 'banana', 'cherry']
# my_string = ", ".join(my_list)
# print("String from list:", my_string)  # Output: apple, banana, cherry

# # String Example # 15
# # String to Integer Conversion

# my_string = "123"
# my_integer = int(my_string)
# print("Integer from string:", my_integer)  # Output: 123

# # String Example # 16
# # Integer to String Conversion

# my_integer = 123
# my_string = str(my_integer)
# print("String from integer:", my_string)  # Output: '123'

# # String Example # 17
# # String to Float Conversion
# my_string = "123.45"
# my_float = float(my_string)
# print("Float from string:", my_float)  # Output: 123.45

# # String Example # 18
# # Float to String Conversion
# my_float = 123.45
# my_string = str(my_float)
# print("String from float:", my_string)  # Output: '123.45'


