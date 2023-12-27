class Film:
	def __init__(self,title,director,time):
		self.title = title
		self.director = director
		self.time = time

	def __str__(self):
		return f"{self.title} directed by {self.director}"

	def __repr__(self):	
		return f"{self.title} directed by {self.director}"
	
	def __len__(self):
		return self.time
	
	def __del__(self):
		print("Film object is deleted")

f = Film("Oppenheimer","Christopher Nolan",120)

print(type(f))
print(len(f))

# del f  # deleting the film object 
