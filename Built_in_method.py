# String Built in methods/ Functions

message = "DevOps is the best career option in 2026 and beyound for IT professionals"

print(message)
print(message.upper())
print(message.lower())
print(message.capitalize())
Message = message.title()
print(Message)

# dir function is used to find the built in methods of a data type

print(message.count("e"))
print(message.count("e", 0, 20))
print(message.find("career"))
print(message.find("career", 0, 30))
print(message.index("career"))

"""
print(dir(message))
print("#############")
print(dir(str))
print("#############")
print(dir(int))
print("#############")
print(dir(list))
print("#############")
print(dir([]))
print("#############")
print(dir(()))
print("#############")
print(dir({}))
"""

print(message.split())
print(message.split(" "))
print(message.split(" ", 3))
print(message.isupper())
print(message.islower())
print(message.isalpha())
print(message.isdigit())
print(message.isalnum())
print(message.startswith("DevOps"))
print(message.endswith("professionals"))
print(message.replace("DevOps", "Cloud"))
print(message.replace(" ", "_"))

message1 = "    DevOps is the best career    "
print(message1)
print(message1.strip()) # removes leading and trailing spaces
print(message1.strip("D")) # removes leading and trailing D
