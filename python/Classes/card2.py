import random
class Card:

    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type} {self.value}"
    
class Deck:
    type = ["Spade","Heart","Diamond","Club"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):  
        self.cards = [Card(t,v) for t in Deck.type for v in Deck.values]
        # for t in type:
        #     print("************")
        #     for v in values:
        #         print(Card(t,v))  
    def dealCard(self,amount):
        card_number = self.numberOfCards()
        if card_number == 0:
            raise ValueError("There is no card at the moment")
        amount = min([card_number,amount])
        cards = self.cards[-amount:]
        self.cards = self.cards[:-amount]
        return cards

    def shuffleDeck(self):
        if (self.numberOfCards() < 52):
            raise ValueError("You can't shuffle the cards right now")
        # shuffled_deck = random.sample(self.cards, len(self.cards))
        # print(shuffled_deck)
        random.shuffle(self.cards)

    def numberOfCards(self):
        return len(self.cards)

deck1 = Deck()

deck1.shuffleDeck()
print(deck1.numberOfCards())
print(deck1.dealCard(5))
print(deck1.numberOfCards())
print(deck1.dealCard(3))
print(deck1.numberOfCards())