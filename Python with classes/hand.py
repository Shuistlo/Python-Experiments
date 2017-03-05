from card import Card
import random

class Hand (Card):
    def __init__(self, numCardsInHand):
        """
        one object of this class stores a number of Card objects
        this number is specified by numCardsInHand
        """
        self.handList = list()
        self.suitList = ['s', 'h', 'c', 'd']
        self.numCardsInHand = numCardsInHand
        for i in range(numCardsInHand):
            suitIndex = random.randint(0,3)
            self.handList.append(Card(random.randint(0,13), self.suitList[suitIndex]))
    def bjValue(self):
        """
        returns the blackjack value of all the cards in the Hand
        """
        acc = 0
        for i in range(self.numCardsInHand):
            acc = self.handList[i].bjValue() + acc
        return acc
    def __str__(self):
        """
        returns a string interpretation of the Hand object
        """
        fullStr = ""
        for i in range(self.numCardsInHand):
            fullStr = fullStr + self.handList[i].__str__() + "\n"
        return fullStr
    def hitMe(self):
        '''
        adds another Card object to the Hand
        '''
        self.numCardsInHand = self.numCardsInHand +1
        suitIndex = random.randint(0,3)
        self.handList.append(Card(random.randint(0,13), self.suitList[suitIndex]))


