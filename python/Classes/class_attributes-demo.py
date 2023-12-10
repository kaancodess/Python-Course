class Pet:
    pets = ["dog","cat","bird"]
    def __init__(self,name,breed):
        if breed not in Pet.pets:
            raise ValueError(f"{breed} is not a pet")
        self.name = name
        self.breed = breed

john = Pet("John","cat")
rachel  = Pet("John","bird")
maggie = Pet("John","dog")

Pet.pets.append("fish")

print(Pet.pets)