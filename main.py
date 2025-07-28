import random


# UserInfo holds user inputted information
class UserInfo:
    # Constructor
    def __init__(self, setName, setType, unitCost, floorPrice, numToOpen):
        self.setName = setName # Name of the MTG set (TDM, INR, etc...)
        self.setType = setType # Play booster, Collector, Set, etc... (Ask for first letter instead of word?)
        self.unitCost = unitCost # Individual cost of a pack / box (may limit to opening packs)
        self.floorPrice = floorPrice # Lowest priced card that can be sold to break even / turn a profit ($1.00, $.20, etc...)
        self.numToOpen = numToOpen # How many packs to simulate opening (only whole numbers)
        self.totalUnitCost = unitCost * numToOpen # Total cost of products

# MTGPack holds the info for each pack that was opened and calculates grossProfits for each pack, if any
class MTGPack:
    def __init__(self, fPrice):
        self.cardList = [] # List holding each card drawn for the pack
        self.packGrossProfit = 0.00
        self.floorPrice = fPrice

    # addCard adds the currently draw card to the card list
    def addCard(self, card):
        self.cardList.append(card)

    # totalGrossProfit calculates total gross profits of all openings
    def totalGrossProfit(self):
        for card in self.cardList: # For-in loop
            if card.cardPrice >= self.floorPrice: # if the current card's market price >= user inputted floor price
                self.packGrossProfit += card.cardPrice # add the current card's market price to the pack's gross profit

# MTGCard holds the information for a single card that was found within a pack
class MTGCard:
    def __init__(self, cardName, cardRarity, cardPrice):
        self.cardName = cardName # Name of the card drawn
        self.cardRarity = cardRarity # Rarity of the card
        self.cardPrice = cardPrice # Market price of the card

# getInfo gathers the users information to simulate the pack openings. Returns the object.
def getInfo():
    setName = input("Set Name(I:E TDM): ")
    setType = input("Set Type: ")
    unitCost = float(input("Unit Cost: "))
    floorPrice = float(input("Floor Price: "))
    numToOpen = int(input("Number of openings: "))

    # Obj holding the user's choices / information
    userInput = UserInfo(setName, setType, unitCost, floorPrice, numToOpen)

    return userInput

# Obj to hold the user inputted information
userInput = getInfo()

# check which set was selected and set type
    # Create obj for the pack to be opened
        # Run logic to select first card
            # create card object for the card drawn
            # Store info in card object
            # store card info in cardList (which is in the MTGPack obj)
            # continue until last card
        # Calculate gross profits for cards >= floorPrice
        # Store pack in openedPackList
        # Continue until last pack

testPack1 = MTGPack() # create the object to hold the pack
# Logic to draw card from the pack
testCard1 = MTGCard(cardName, cardRarity, cardPrice) # create card object to hold drawn card info
# call method to add MTGCard obj to the MTGPack cardList
testPack1.addCard(testCard1)
# Continue until the last card
# Calculate the pack's grossProfit, if any