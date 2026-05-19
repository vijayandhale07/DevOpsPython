# This is single line comment in python
print("Hello, world!") # This is another comment in python
"""
This is a multi-line comment in python
It can span multiple lines and is often used for documentation or to provide detailed explanations.
We can also use triple quotes for multi-line strings, which can be assigned to variables or used as docstrings in funtions and classses.
"""
'''
This is another way to write multi-line comments in python using single quotes.
It serves the same purpose as triple double quotes and can be used interchangeably.
'''
# Variables in python do not require explicit declaration of data types, as python is a dentoed language. You can simply assign a value to a variable and pyhton will infer the data type based on the value assinged to it.
x = 10 # This is an integer variable
y = 3.14 # This is a float variable
name = "John doe" # This is a string variable
is_student = True # This is a boolean variable
print(x)
print(y)
print(name)
print(is_student)
print("The value of x is:", x)
print("The value of y is:", y)
print("The name is:", name)
print("Is the person a student?", is_student)
# You can also use formatted string (f-strings) to embed expressions inside sting literals, using curly brases {}.
# This allows for more readable and concise code when you want to include variable values or expressions within a string.
print(f"The value of x is {x} and the value of y is {y}.")
print(f"The name is {name} and is the person a student? {is_student}.")

# if condition to check if x is greater than 5
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

print("This is the end of the code.")

if name == "John doe":
    print("Hello, John!")
    print("Welcome to python programming!")
    print("Have a great day!")
else:
    print("Hello, Stranger!")
    print("Welcome to python programming!")
    print("Have a great day!")
    print("This is the end of the code.")
    print("This is the end of the code.")