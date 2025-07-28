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

# MTGOpenedPacks holds a list of MTGPack objects
class MTGOpenedPacks:
    def __init__(self, fPrice):
        self.packList = [] # create an empty list
        self.floorPrice = fPrice # Cheapest card that can be sold

# MTGPack holds the info for each pack that was opened and calculates grossProfits for each pack, if any
class MTGPack:
    def __init__(self):
        self.cardList = [] # List holding each card drawn for the pack
        self.packGrossProfit = 0.00

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
    numToOpen = int(input("Number of packs to open: "))

    # Obj holding the user's choices / information
    userInput = UserInfo(setName, setType, unitCost, floorPrice, numToOpen)

    return userInput

# genMTGPack generates a MTGPack
def genMTGPack():
    pass

# genRandCard generates a random card, used for testing. numOfCard == Num of cards per pack, currentPack == MTGPack obj
# returns a list of cards that were drawn
def genRandCard(numOfCard):
    # Placeholder names for cards
    namePlaceHolder = ["Goblin", "Shark", "Cat", "Dog", "Vampire", "Angel", "Demon", "Ent", "Elf", "Orc", "Dwarf", "Fireball", "Lightning", "Curse", "Pacify"]
    # Placeholder rarities
    rarityPlaceHolder = ["Mythic", "Rare", "Uncommon", "Common"]

    cardList = [] # list of MTGCard objects

    for _ in range(numOfCard):
        cardName = random.choice(namePlaceHolder) # get random name for card
        cardRarity = random.choice(rarityPlaceHolder) # randomly selected rarity
        cardPrice = round(random.uniform(0.01, 0.5), 2) # random price from 0.01 to 20.00 rounded to 2 decimal places

        card = MTGCard(cardName, cardRarity, cardPrice) # create a card object
        cardList.append(card) # add the card obj to the cardList list
    
    return cardList

# Get information from user and create userInfo object
userInput = getInfo()

# create the object that will hold all pack objects
openedMTGPacks = MTGOpenedPacks(userInput.floorPrice)

# simulate opening X amount of packs, defined by user
for pack in range(userInput.numToOpen): # opening a pack

    # Create a pack object
    testPack = MTGPack()

    # Generate the num of cards per pack, returns a list of MTGCard objects
    cardList = genRandCard(14)

    # add the current cardList to the MTGPack object cardList
    testPack.cardList = cardList

    # Calculate the total gross profit of the pack, if any. 
    for cPrice in cardList:
        if cPrice.cardPrice >= openedMTGPacks.floorPrice:
            # packs gross profit
            testPack.packGrossProfit += cPrice.cardPrice

for c in testPack.cardList:
    print(c.cardName, c.cardRarity, c.cardPrice)

print("Gross profit: ", testPack.packGrossProfit)