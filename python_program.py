# Python join method is used to concatenate the elements of a list or any iterable into a single string, with a specified separator between the elements.

skills = ["Python", "Docker", "Kubernetes", "AWS"]
# Using join to concatenate the skills into a single string
skills_string = ", ".join(skills)
print(f"Skills for DevOps Engineers: {skills_string}")

# tuple of numbers
Ip_addresses = ("192.168.1.1", "192.168.1.2", "192.168.1.3")

# Using join to concatenate the IP addresses into a single string
ip_string = " ".join(Ip_addresses)
print(f"IP Addresses: {ip_string}")

# Python inbuilt functions and methods

#inbuilt functions

# Python inbuilt functions and methods

# inbuilt functions
print(len(skills))  # Output: 4
print(max(skills))  # Output: 'Python' (lexicographically largest)
print(min(skills))  # Output: 'AWS' (lexicographically smallest)
print(sum([1, 2, 3, 4]))  # Output: 10
print(sorted(skills))  # Output: ['AWS', 'Docker', 'Kubernetes', 'Python']      
print(type(skills))  # Output: <class 'list'>
print(type(Ip_addresses))  # Output: <class 'tuple'>    
print(type(skills_string))  # Output: <class 'str'>
print(type(ip_string))  # Output: <class 'str'>
