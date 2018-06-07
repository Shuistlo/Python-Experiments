"""
Defines class Card and tests it by creating four Card objects and calling methods on them
class Card handles errors such as
incorrect Type for rank and suit
"""

class Card:
        """
        one object of this class stores one Card's rank and suit
        """
        def __init__(self, rank, suit):
                """
                Sets the rank and suit of the Card based on function parameters 
                """
                suitList = ['s', 'h', 'c', 'd']
                if suit not in suitList:
                        raise ValueError()
                if type(rank) != int:
                    raise TypeError()
                if type(suit) != str:
                        raise TypeError()
                if rank < 0 or rank > 13:
                        raise ValueError()
                self.rank = rank
                self.suit = suit
                
        def getRank(self):
                """
                gets the rank of the card
                """
                return self.rank
        
        def getSuit(self):
                """
                gets the suit of the card
                """
                return self.suit
        
        def bjValue(self):
                """
                returns the blackjack value of the card
                """
                if self.rank > 10:
                        f = 10
                else:
                        f = self.rank
                return f
        
        def __str__(self):
                """
                returns a string interpretation of the card object
                """
                rankDict = {1:'Ace', 2:'Two', 3:'Three', 4:'Four', 5:'Five',6:'Six', 7:'Seven',8:'Eight', 9:'Nine', 10:'Ten', 11:'Jack', 12:'Queen', 13:'King'}
                suitDict = {'d':'Diamonds', 'c':'Clubs', 'h':'Hearts', 's':'Spades'}
                strName = ""
                if self.rank in rankDict:
                        strName = rankDict[self.rank] + " of "
                if self.suit in suitDict:
                        strName = strName + suitDict[self.suit]
                return strName

c = Card(None, None)
print(c)

'''
print("Creating card with an improper rank value - rank value out of range")
print("Card(15, 'd')")
try:
        a = Card(15, 'd')
        print(a)
        print("Printing rank of 5 of Spades")
        print(a.getRank())
except ValueError:
        print("Error : improper rank value")

print("Creating card with improper suit value - suit out of range")
print("Card(2, 'f')")
try:
    b = Card(2, 'f')
    print(b)
    print("Printing suit of 2 of Diamonds")
    print(b.getSuit())
except ValueError:
        print("Error : improper suit value") 

print("Creating card with an improper rank value - incorrect type")
print("Card(True, 's')")
try:
        c = Card(True, 's')
        print(c)
        print("Getting BlackJack value of Card")
        print(c.bjValue())
except TypeError:
        print("Error : improper rank value")

print("Creating card with improper suit value - incorrect type")
print("Card(5,5)")
try:
        d = Card(5,5)
        print(d)
        print("Getting BlackJack value of Card")
        print(d.bjValue())
except ValueError:
        print("Error : improper suit value")
'''

'''
Creating card with an improper rank value - rank value out of range
Card(15, 'd')
Error : improper rank value
Creating card with improper suit value - suit out of range
Card(2, 'f')
Error : improper suit value
Creating card with an improper rank value - incorrect type
Card(True, 's')
Error : improper rank value
Creating card with improper suit value - incorrect type
Card(5,5)
Error : improper suit value
'''
