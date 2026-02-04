class computers: 
	hostname = ""
	ipadderss = ""

server1 = computers()

server1.hostname = "MyCompluter1"
server1.ipaddress = "192.168.1.1"

server2 = computers()

server2.hostname = "MyCompluter2"
server2.ipaddress = "192.168.1.2"

print("Server-1 Hostname---",server1.hostname)
print("Server-1 Ipaddress---",server1.ipaddress)

print("Server-2 Hostname---",server2.hostname)
print("Server-2 Ipaddress---",server2.ipaddress)

