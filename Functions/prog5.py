# pass a list in function...

def server_demo(list2):
	list2[1] = "Dell"
	return(list2[1])


list1 = ['IBM','HP','DELL']
y = server_demo(list1)

print(y)