class NewDict(dict):
	def __repr__(self):
		print('there is a message from repr method')
		return super().__repr__()

	def __missing__(self,key):
		print("you want non-existent key information")

	def __getitem__(self,key):
		print("you want the key information")
		return super().__getitem__(key)

	def __setitem__(self,key,value):
		print("you are adding a value")
		super().__setitem__(key,value)
	
	def __contains__(self,item):
		# print("you can't search an item")
		# return False # if we want to no search
		print("there is a item you have been looking for")
		return super().__contains__(item)
data = NewDict({"First":"John","Last":"Doe"})


data["First"]
data["Age"]
data["First"] = "Kaan" # changing the name John to Kaan with setitem method
print(data) # printing the last dict

print("First" in data)

