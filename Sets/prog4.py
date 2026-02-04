#Python union function 

os = {"Linux", "Windows Server", "Fedora",'Suse Linux', "AIX Linux", "RedHat Linux" }

os1 = {'Ubuntu','Suse Linux'}

os2 = os.union(os1)

print(os2)