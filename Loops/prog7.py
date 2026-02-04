# dictionary

comp1 = {"OS":"Windows 10",
	"AntiVirus":"Installed",
	"IP":"10.124.19.1",
	"Patched":"No"

}
if comp1["OS"] == "Windows 10" and comp1["Patched"] == "Yes":
	print("Host computer with IP:", comp1["IP"],"is pathced system")
else: 
	print("Host computer with IP:",comp1["IP"], "is not pathced system.")
	