planet1="Closest of sun"

print("The planet is", planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])
print(planet1[3])
print(planet1[4])


print("##########################")
print("The planet is " + planet1)
print("The planet is {}".format(planet1))
print(f"The planet is {planet1}")
print("The planet is %s" % planet1)
print("The planet is " + str(planet1))
print("The planet is " + repr(planet1))

print("##########################")

print(planet1[-1])
print(planet1[-2])
print(planet1[-3])
print(planet1[-4])
print(planet1[-5])

# Slicing a string, get a substring from the string.
print(planet1[0:7])  # Output: Closest
print(planet1[8:10])  # Output: of
print(planet1[11:14])  # Output: sun
print(planet1[:7]) # Output: Closest
print(planet1[8:]) # Output: of sun
print(planet1[:]) # Output: Closest of sun
print(planet1[::2]) # Output: Clsso u
