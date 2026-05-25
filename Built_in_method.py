# String Built in methods/ Functions

message = "DevOps is the best career option in 2026 and beyound for IT professionals"

print(message)
print(message.upper())
print(message.lower())
print(message.capitalize())
Message = message.title()
print(Message)

# dir function is used to find the built in methods of a data type
print(dir(message))
print(dir(str))

print(message.count("e"))
print(message.count("e", 0, 20))
print(message.find("career"))
print(message.find("career", 0, 30))
print(message.index("career"))