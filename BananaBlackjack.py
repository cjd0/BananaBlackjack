#!/usr/bin/env python3
import time
import random

#introduction to game - exists outside of main game loop
def intro():
    print("Welcome to blackjack. Please take a seat...")
    time.sleep(2)
    input("How are we doing this evening? ... ")
    print("Okay! Okay! I didn't ask for your life story...")
    time.sleep(2)
    print("I see you have brought a whole bunch of bananas with you. Hey big spender! Minimum bet is 1 banana, there is no maximum.")
    time.sleep(2)    
    print("Let's get started. Good luck! You're gonna need it...")
    time.sleep(2)
    

#requests user input to place a bet, initialises the pot
def placeBets():
    global bananas
    global currentBet
    global currentPot
    validBet = False
    while not validBet:
        try:
            currentBet = int(input("You currently have " + str(bananas) + " bananas. Place your bets: "))
        except ValueError:
            invalidEntry()
            continue
        if currentBet <= bananas and currentBet > 0:
            bananas = bananas - currentBet
            currentPot = 2 * currentBet
            currentBet = 0
            validBet = True
        else:
            invalidEntry()
    print("Bet accepted. I will match your bet, so the pot stands at " + str(currentPot) + ".")
            
#allows user input to decide whether ace is worth 1 or 11
def highOrLow():
    global deck
    global aceHigh
    aceHigh = True
    highLowLoop = True
    while highLowLoop:
        aceVal = input("Aces high or low? ")
        if aceVal == "high" or aceVal == "High" or aceVal == "h":
            print("Aces high.")
            random.shuffle(deck)
            highLowLoop = False
            time.sleep(1)
            shuffle()
        elif aceVal == "low" or aceVal == "Low" or aceVal == "l":
            print("Aces low.")
            random.shuffle(deck)
            aceHigh = False
            highLowLoop = False
            time.sleep(1)
            shuffle()
        else:
            invalidEntry()

#delay effect for shuffling
def shuffleDelay(shuffleJoke):
    print(shuffleJoke, end="")
    i = 0
    time.sleep(1)
    while i < 2:
        print(".", end = ""),
        i += 1
        time.sleep(1)
    print(".")
    time.sleep(1)

#stupid jokes for shuffling
def shuffle():
    shuffleDelay("Shuffling cards")
    shuffleDelay("Dropping the cards everywhere")
    shuffleDelay("Fighting through the tears to gather them up as my manager screams at me")
    time.sleep(2)

#function to allow random selection from list of insults - variety is the spice of life!
def invalidEntry():
    insultList = ["Invalid entry: Maybe try using your fingers to type instead of smashing your face against the keyboard?",
                  "Invalid entry: Take a deep breath and focus. You've got this.",
                  "Invalid Entry: If you're confused consider finding a nearby adult to ask for help.",
                  "Invalid entry: Please stop disappointing your parents like this.",
                  "Invalid entry: It's so inspiring that you just keep trying.",
                  "Invalid entry: That's it. You keep flapping aimlessly against the keyboard. You'll get there.",
                  "Invalid entry: Do you mind if I go for a quick smoke break if you're having a moment?",
                  "Invalid entry: You remind me of my second wife. She also had difficulty communicating with me.",
                  "Invalid entry: Sound it out, plan each letter before you type it. I believe in you!",
                  "Invalid entry: Have you fallen on the keyboard and can't get up!? What should I do!?",
                  "Invalid entry: I mean- is that even meant to be a word? If that was on purpose, I'm impressed.",
                  "Invalid entry: You know I'm paid by the hour, so have fun with it.",
                  "Invalid entry: I've survived 3 vending machine crushings this year alone, and reading that was still the worst moment of my life.",
                  "Invalid entry: If you do decide to give up, please tell my boss that I encouraged you to keep trying. Maybe actually give up though...?",
                  "Invalid entry: Is this going to go on much longer? I will need to feed my cat at some point in the near future."]
    print(random.choice(insultList))

#function for all instances of the game ending    
def gameOver():
    global game
    global playerFin
    playerFin = True
    gameOverLoop = True
    print("You're fresh out of bananas my friend. Wanna pop over to Tesco and buy 100 more? That definitely won't look weird...")
    while gameOverLoop:
        again = input("Play again? Y/N: ")
        if again == "y" or again == "Y":
            print("Bring it on!")
            time.sleep(2)
            gameOverLoop = False
        elif again == "n" or again =="N":
            print("Thanks for playing. May all your Jacks be Black.")
            print("Until next time...")
            game = False
            gameOverLoop = False
        else:
            invalidEntry()

#function to allow user to take another card or end turn
def stickOrTwist():
    playerMoveLoop = True
    while playerMoveLoop:
        global playerMove
        playerMove = input("Stick or twist? ")
        if playerMove == "twist" or playerMove == "Twist" or playerMove == "t" or playerMove == "stick" or playerMove == "Stick" or playerMove == "s":
            playerMoveLoop = False
        else:
            invalidEntry()

#function to convert an item from the deck list into a int value to add to the playerCount or compCount            
def returnIntValue(card):
    global aceVal
    if card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
        return 10
    elif card[0] == 'A':
        if aceHigh:
            return 11
        else:
            return 1
    else:
        return int(card[:-1])        

#user input for player turn
def playerTurn():
    global deck
    global cardDict
    global currentPot
    global playerFin
    global playerCount
    global bananas
    playerStick = False
    playerCount = 0
    while playerCount < 21 and not playerStick:
        print("You are currently at " + str(playerCount) + "...")
        stickOrTwist()
        if playerMove == "twist" or playerMove == "Twist" or playerMove == "t":
            playerCount = playerCount + returnIntValue(deck[0])
            print("You drew the " + cardDict[deck[0][:-1]] + " of " + cardDict[deck[0][-1]] +  "...")
            del deck[0]
            time.sleep(1)
        else:
            playerStick = True
    if playerStick == True and playerCount < 17:
        print("You're sticking already...? Well okay, I won't tell you how to spend your bananas...")
    elif playerCount < 21:
        print("Stuck at " + str(playerCount) + ".")
    elif playerCount > 21:
        print("Bad luck, you landed on " + str(playerCount) + "...")
        currentPot = 0
        playerFin = True
    else:
        print("Congratulations, you got a Blackjack! Your father and I are so proud of you!")
        playerFin = True
        bananas = bananas + currentPot
        currentPot = 0

#computer has a turn if player does not lose
def compTurn():
    global playerFin
    global compCount
    global cardDict
    compCount = 0
    if not playerFin:
        global playerCount
        global currentPot
        global bananas
        print("It's my turn now. Prepare yourself for a bombardment of furious vengeance...")
        while compCount < 17 and compCount <= playerCount:
            print("I am currently at " + str(compCount) + "...")
            compCount = compCount + returnIntValue(deck[0])
            time.sleep(2)
            print("I drew the " + cardDict[deck[0][:-1]] + " of " + cardDict[deck[0][-1]] +  "...")
            time.sleep(2)
            del deck[0]
        if compCount > 21:
            print("I have landed on " + str(compCount) + ". I have shamed my ancestors and do not deserve to wear this suburban casino uniform!!")
            time.sleep(1)
            print("Congratulations on your victory!")
            bananas = bananas + currentPot
            currentPot = 0
        elif compCount < 21 and compCount > playerCount:
            print("Sticking at " + str(compCount))
            time.sleep(2)
            print("My " + str(compCount) + " defeats your measly " + str(playerCount) + "!")
            time.sleep(1)
            print("I won! Just wait 'til my ex-wife hears about this!!")
            currentPot = 0
        elif compCount == playerCount:
            print("Sticking at " + str(compCount))
            time.sleep(2)
            print("Draw! We both landed on " + str(compCount) + "...")
            time.sleep(1)
            print("The only thing worse than losing is drawing. Except the kind that involves crayons...")
            bananas = bananas + int((currentPot / 2))
            currentPot = 0
        elif compCount == 21:
            print("I got a blackjack! My therapist will be so proud of me.")
            currentPot = 0
        else:
            print("Sticking at " + str(compCount))
            time.sleep(2)
            print("My " + str(compCount) + " has been defeated by your " + str(playerCount) + "...")
            time.sleep(1)
            print("I can't believe I lost. Mr. Whiskers is never gonna look me in the eye again.")
            bananas = bananas + currentPot
            currentPot = 0

#dictionary used to convert the items on the deck list into a more readable format
cardDict = {
    "C" : "Clubs",
    "D" : "Diamonds",
    "H" : "Hearts",
    "S" : "Spades",
    "A" : "Ace",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "10" : "Ten",
    "J" : "Jack",
    "Q" : "Queen",
    "K" : "King"
}

#main game
game = True
intro()
while game:
    playerCount = 0
    compCount = 0
    deckIndex = 0
    currentDeck = []
    bananas = 100
    currentBet = 0
    currentPot = 0
    aceHigh = True
    while bananas > 0:
        #a standard deck of cards
        deck = ['AC','AD','AH','AS','2C','2D','2H','2S','3C','3D','3H','3S','4C','4D','4H','4S','5C','5D','5H','5S',
                '6C','6D','6H','6S','7C','7D','7H','7S','8C','8D','8H','8S','9C','9D','9H','9S','10C','10D','10H','10S',
                'JC','JD','JH','JS','QC','QD','QH','QS','KC','KD','KH','KS']
        playerFin = False
        placeBets()
        highOrLow()
        playerTurn()
        compTurn()
    gameOver()