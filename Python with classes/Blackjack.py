from hand import Hand

if(__name__ == "__main__"):
    print("creating Hand object with 5 cards")
    a = Hand(5)
    print("printing hand object")
    print(a)
    print("getting black jack value of Hand")
    print(a.bjValue())
    print("adding a card to the hand")
    a.hitMe()
    print("printing hand object")
    print(a)

'''
creating Hand object with 5 cards
printing hand object
Two of Diamonds
Six of Hearts
Three of Spades
Queen of Hearts
Queen of Diamonds

getting black jack value of Hand
31
adding a card to the hand
printing hand object
Two of Diamonds
Six of Hearts
Three of Spades
Queen of Hearts
Queen of Diamonds
Six of Clubs
'''
