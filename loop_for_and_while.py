# Loop: For and While
"""
for i in range(5):
    print(i)


count = 0

while count < 5: 
    print(count)
    count += 1

while True:
    user_input = input("Enter 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")
"""

# Nested loops and conditional statements
"""
for i in range(1, 4):
    print(f"Outer loop iteration {i}")

    for j in range(1, 4):
        print(f" Inner loop iteration {j}")
        if j == 2:
            print(" Breaking innter loop")
            break
        else:
            print(" Continuing inner loop")

# loop with continue statement


for i in "DevOps":
    if i == "O":
        print("Skipping 'O'")
        continue
    print(i)

"""
"""
skill = ["Python", "Docker", "Kubernetes", "AWS"]

for s in skill:    
    print(f"{s.lower()} is an important skill for DevOps Engineers.")
"""
skill = ["Python", "Docker", "Kubernetes", "AWS"]

for s in skill:
    if s == "Python":
        print(f"{s.lower()} is a programming language used for automation and scripting.")
    elif s == "Docker":
        print(f"{s.lower()} is a containerization platform used for packaging applications.")
    elif s == "Kubernetes":
        print(f"{s.lower()} is an orchestration tool for managing containerized applications.")
    elif s == "AWS":
        print(f"{s.lower()} is a cloud computing platform providing various services.")
    else:
        print(f"Unknown skill: {s}")
print("All skills have been processed.")
