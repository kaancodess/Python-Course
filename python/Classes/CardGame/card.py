class Card:
    # type = ["Spade","Heart","Diamond","Club"] # clubs => sinek diamond => maca Spade => as
    # values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __repr__(self): # changing ram memory address
        return f"{self.type} {self.value}"
    
spade5 = Card("Spade","5") # as 5

print(spade5)