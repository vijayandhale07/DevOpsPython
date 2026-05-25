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

print(message1.find("career"))
print(message1[23:29])

print(message1.find("career", 0, 20)) # returns -1 if not found

seq1= ("192", "168", "1", "1")
print(".".join(seq1)) # joins the sequence with a dot 
print("-".join(seq1)) # joins the sequence with a dash
print("".join(seq1)) # joins the sequence without any separator
print("/".join(seq1)) # joins the sequence with a slash

mountains = ["Everest", "Himalayas", "k2", "Kangchenjunga"]
print(mountains)
print(", ".join(mountains)) # joins the list with a comma and space

mountains.append("Lhotse")
print(mountains)
# Combining the list into a string with a separator
print(", ".join(mountains)) # joins the list with a comma and space

mountains.extend(["Mt Rainer", "Satpuda"])
print(mountains)
print(", ".join(mountains)) # joins the list with a comma and space

# insert method is used to inset an element at a specfic index in the list
mountains.insert(2, "Annapurna")
print(mountains)

# delete method pops method is used to delete an element 

mountains.pop() # deletes the last element in the list
print(mountains)
mountains.pop() 
print(mountains) 
mountains.pop()
print(mountains)

mountains.pop(2)
print(mountains)

mountains.remove("Himalayas") # removes the first occurrence of the element
print(mountains)