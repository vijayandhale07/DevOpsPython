class computers():
	hostname = ""
	ipaddress = ""
	
	def computers_details(self):
		print("Server hostname---",self.hostname)
		print("Server ipaddress---",self.ipaddress)

class servers(computers):
	server_type = ""

	def server_details(self):
		computers.computers_details(self)
		print("Server type---",self.server_type)


server1 = servers()

server1.hostname = "APPComp1"
server1.ipaddress = "192.168.1.1"
server1.server_type = "RACK SERVER"


server1.server_details()
		