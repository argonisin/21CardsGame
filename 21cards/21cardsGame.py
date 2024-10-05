"""
MADE BY @Argonisin on github
Please check out my other programs

Hello welcome to 21 words game, this game derived from the card magic trick called "21 cards trick".
I spent my dying programming hours to put the card trick algorithm into a piece of code,
and then i spent countless hours debugging so that the algorithmn guesses the correct word that 
you have chosen and remembered through your mind.

This algorithm is a implementation of STACK ALGO.

Explanation:
Just youtube the 21 cards trick.

"""

import json, time
from random import shuffle
from os import system as sys

# A exception catcher to prevent FileNotFoundError Prompt to break the code
try:
    
    file_name = "listOfWords.json"
    with open(file_name, 'r') as wordData:
        word = json.load(wordData)
        
except FileNotFoundError as e:
    print(f"[{e}]: Check if the JSON file is within the folder.")

# <<global_declartions>>
original_deck = [i for i in word["words"]]
shuffle(original_deck)
deck1, deck2, deck3 = [], [], []
deckCount = 0

class shuffle:
    
    # <<initialization>>
    def __init__(bot, LIST:list[str]) -> None:
        bot.words = LIST
        bot.limit = 7
    
    # three-way stack is a function to stack the original_deck in three diffrent decks.
    def threewayStack(bot) -> None:
        while True:
            bot.deck1_count = len(deck1) #
            bot.deck2_count = len(deck2) # These checks the lenght of the decks 
            bot.deck3_count = len(deck3) #
            
            # Checks if all conditions are true.
            if bot.deck1_count and bot.deck2_count and bot.deck3_count == bot.limit:
                break
            
            """
            
            Here is where this whole program runs on.
            This is the brain of it.
            
            This works by 2d stack algorithm but it is modified a bit.
            It'll append the first-index word to the deck1 and then-
            remove the word from the list it took it from, and it'll move
            on throught the next deck which is deck2 and also does the same thing
            until deck3. These repeats untill all decks are in the lenght of 7.
            which will stop the program as there are no more words.
            
            """
            deck1.append(bot.words[0])
            bot.words.remove(bot.words[0])
            deck2.append(bot.words[0])
            bot.words.remove(bot.words[0])
            deck3.append(bot.words[0])
            bot.words.remove(bot.words[0]) 

# Checks what terminal you are using in-order to implement if it's "CLS" or "CLEARs"
def device(Device, INT:int) -> str:
    # This returns the way os.system() will clear the terminal.
    if INT == 1:
        if Device == 'pc':
            return 'cls'
        elif Device == 'phone':
            return 'clear'
    
    # This returns the device itself
    if INT == 2:
        return Device

# Bot has guessed your word with 100% accuracy
def guess(wordList:list[str]) -> None:
    print(f"Is your word: {wordList[10]}")
    
    while True:
        user = input("Yes or No [y/n]?: ")
        
        if user.lower() == 'y':
            dialouge = ["See... I can see you..",
                        "                      ",
                        "and.. I can hear you..",
                        "Thanks For playing.   "]
            
            for i in dialouge:
                print(f" Mind-Reader: {i}", end='\r')
                time.sleep(0.88)
            print("\n")
            
            while True:
                user = input("(p)lay again or (e)xit?: ")
                
                if user.lower() == 'p':
                    time.sleep(.23)
                    sys(f'{system}')
                    return main(sysUser)
                elif user.lower() == 'e':
                    print("\nbye")
                    break
                else:
                    continue        
        else:
            break
    
# Where the fun begins..
def main_game():
    
    # Shuffles the cards..
    def shuffling() -> None:
        print("[MINDREADER_GAME! [v1]]\n")
        load = [" Shuffling.", " Shuffling..", " Shuffling...", " Shuffling   "]
        count = 0
        
        while count != 2:    
            for i in load:
                print(i, end='\r')
                time.sleep(0.65)
            count+=1
        time.sleep(.2)
        shuffle(original_deck).threewayStack()
        sys(f'{system}')
        return gameShuffle(deckCount)
    
    # The middle of the plot
    def gameShuffle(deckCount):
        deckCount = deckCount
        print("[MINDREADER_GAME! [v1]]\n")
        load = [" Stacking.", " Stacking..", " Stacking...", " Stacking   "]
        count = 0
        
        while count != 2:    
            for i in load:
                print(i, end='\r')
                time.sleep(0.65)
            count+=1
        time.sleep(.2)
        shuffle(original_deck).threewayStack()
        sys(f'{system}')
        
        print("[MINDREADER_GAME! [v1]]\n")
        
        # Repeat these stacking and shuffling 3 times:
        while deckCount != 3:
            print(f"""
Deck One : {deck1}
Deck Two : {deck2}
Deck Three : {deck3}
""")
            user = input("Where is your word at?[1,2,3]: ")
            
            # If 1 then the configuration should be like this: deck2, deck1, deck3 and vice-versa
            if user == '1':
                # Stacks all of the decks in one list
                newDeck1 = [j for n in [deck2, deck1, deck3] for j in n] 
                
                deck1.clear() #
                deck2.clear() # These clears the value that is in the decks
                deck3.clear() #
                
                shuffle(newDeck1).threewayStack() # These gets spliced to three stacks again
                deckCount+=1
                time.sleep(0.5)
                sys(f'{system}')
                return gameShuffle(deckCount)
            
            elif user == '2':
                # Stacks all of the decks in one list
                newDeck2 = [j for n in [deck1, deck2, deck3] for j in n]
                
                deck1.clear() #
                deck2.clear() # These clears the value that is in the decks
                deck3.clear() #
                
                shuffle(newDeck2).threewayStack() # These gets spliced to three stacks again
                deckCount+=1
                time.sleep(0.5)
                sys(f'{system}')
                return gameShuffle(deckCount)
            
            elif user == '3':
                # Stacks all of the decks in one list
                newDeck3 = [j for n in [deck1, deck3, deck2] for j in n]
                
                deck1.clear() #
                deck2.clear() # These clears the value that is in the decks
                deck3.clear() #
                
                shuffle(newDeck3).threewayStack() # These gets spliced to three stacks again
                deckCount+=1
                time.sleep(0.5)
                sys(f'{system}')
                return gameShuffle(deckCount)
            else:
                continue
        
        # These gets spliced to three stacks for the last time
        finishedDeck = [j for n in [deck1, deck2, deck3] for j in n]  
        return guess(finishedDeck)
    
    ######################################################
    #                  <<SEPARATOR>>                     #
    ######################################################
    
    # Another panel
    
    print("[MINDREADER_GAME! [v1]]\n")
    print("WORDS:\n")
    print("------------------\n")
    for i in original_deck:
        print(f"'{i}'",end='\n')
    print("\n------------------\n")
    
    No = 0 # A literal 'NO' counter.
    while True:
        user = input("Have you chosen a word (y/n)?: ")
        
        if user.lower() == 'y':
            sys(f'{system}')
            time.sleep(.23)
            return shuffling()
        
        elif user.lower() == 'n':
            No+=1
            if No == 2:
                sys(f'{system}')
                time.sleep(.23)
                return main(sysUser)
            print("\nCome on choose one..")
            print("or to main menu say No again.\n")
      
# Loading to the game..  
def dialouge():
    while True:
        print("[MINDREADER_GAME! [v1]]\n")
        
        dialouge = ["I have 21 words..",
                    "You must choose one and remember it..",
                    "Ready?                               "]

        for i in dialouge:
            print(f" Mind-Reader: {i}", end='\r')
            time.sleep(0.92)
        print("\n")
        time.sleep(0.12)
        
        while True:
            user = input("y/n: ")
            
            if user.lower() == 'y':
                time.sleep(0.23)
                sys(f'{system}')
                return main_game()
            
            elif user.lower() == 'n':
                time.sleep(0.23)
                sys(f'{system}')
                return main(sysUser)
            else:
                print("\nchoose a valid response\n")

# Main-menu 
def main(sysDev):
    
    ##  GLOBAL DECLARATIONS  ##
    global sysUser, system
    sysUser = device(sysDev, 2)
    system = device(sysDev, 1)
    ###########################
    
    print("[MINDREADER_GAME! [v1]]\n")
    opts = {1:"Start",
            2:"Quit"}
    
    for num, opt in opts.items():
        print(f"[{num}]:{opt}")
    print()
    
    while True:
        user = input(": ")
        
        if user == '1':
            sys(f'{system}')
            return dialouge()
        
        elif user == '2':
            break
        
        else:
            print("\n[Number is not in the range of options available]\n")
            time.sleep(0.67)
            sys(f'{system}')
            return main(sysUser)
                
if __name__ == "__main__":
    while True:
        choose = input("Are you on [Phone] or [PC]?: ")
        
        if choose.lower() == 'phone':
            print("wait...")
            time.sleep(0.75)
            sys('clear')
            main(choose.lower())
            break
        elif choose.lower() == 'pc':
            print("wait...")
            time.sleep(0.75)
            sys('cls')
            main(choose.lower())
            break
        else:
            continue
