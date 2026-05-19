with open("application.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())
# This code reads an application log file and prints out any lines that contain the word "ERROR".
