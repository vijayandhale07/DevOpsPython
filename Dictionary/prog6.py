# Dictionary in python 

group1 =  {
		"name":"IBM Server",
		"OS":"AIX Unix",
		"Processor":"Power Processor"
	  }

#to get the key value using get function 

x = group1["OS"]

print(x)

y = group1.get("Processor")
print(y)
print(group1)
print(type(group1))
print(type(x))
print(type(y))