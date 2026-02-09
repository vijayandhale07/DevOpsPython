# Working with files/logs 


with open("/var/log/syslog") as f:
	for line in f:
		if "error" in line.lower():
			print(line)