class computers:
	hostname = ""
	ipaddress = ""
	dbname = ""
	def server_details(self):
		print("Server hostname---",self.hostname)
		print("Server Ipaddress---",self.ipaddress)
		print("Server DB Name--",self.dbname)

server1 = computers()

server1.hostname = "APPServer1"
server1.ipaddress = "192.168.19.1"
server1.dbname = "Oracle 11g"

server2 = computers()

server2.hostname = "APPServer2"
server2.ipaddress = "192.168.19.2"
server2.dbname = "Cassandra DB"

server1.server_details()
server2.server_details()
