str1 = "alpha"
str2 = "beta"
str3 = 'gamma'
str4 = '''gamma string'''
str5 = """delta string"""


# Numbers
num = 123
flt1 = 2.0
flt2 = 3.14
# Booleans
bool1 = True
bool2 = False
# lists
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = ["alpha", "beta", "gamma", "delta"]
# List Collection of multi datatype, enclosed in square brackets.

first_list = [1, 2.0, "three", True, [4, 5, 6], {"key": "value"}]
print(first_list)
print(first_list[4])  # Output: 1
print("")

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)

print(num)
print(flt1)
print(flt2)

print(bool1)
print(bool2)
print(list1)
print(list2)

print(type(list1))
print(type(list2))

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[9])

print("##########################")

# Tuples Collection of multi datatype, enclosed in round brackets.

tuple1 = (1, 2.0, "three", True, [1, 3, 4])

print(tuple1)
print(tuple1[0])    
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])

# dictionaries Collection of multi datatype, enclosed in curly brackets.
dict1 = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(dict1)
print(dict1["key1"])
print(dict1["key2"])
print(dict1["key3"])
