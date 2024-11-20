"""
Group:
    Nathan Larsen
    Anthony Esboldt
    Nolan Henze
 
Objective: Create an UNO card game where everything functions as normal using different functions and class
 
- incorporate container classes such as stacks or queues in the implication of the draw pile
- create a class for the function of hands
- be able to shuffle the discard pile without putting back in the cards currently in players hands
 
UNO: Rules or Basics
- Cards: 4 different colors, numbers up to 9, wild cards, draw 2, wild draw 4, skips, and reverse
    - Red, Yellow, blue, and green
    - There are 108 cards in the deck
    - there are 19 of the regular number cards for each color
        - one 0, and 2 of 1-9
    - 8 of each colored special, two of each color
        - ie: skips, draw 2, or reverse
    - 4 wild and 4 wild draw 4
 
- Must match color, symbol, or play a wild to be able to play
- If you can not play, draw 1
    - If you can play this card, you can do so this turn
 
- 2-10 players
 
- Potentially adding in the scoring rules
    - color == face value
    - skips, reverse, or draw 2 == 20 points
    - wilds == 50 points
 
- Will not be able to incorporate the saying "UNO" rule
"""
 

""" Testing the discard and reshuffling functions
for n in range(10):
    discard_deck.push(uno_deck.remove_from_top())
 
print(discard_deck)
for y in range(uno_deck.size()):
    uno_deck.remove_from_top()
#reshuffle(uno_deck, discard_deck)
#print(discard_deck)
#print(uno_deck)
uno_deck.remove_from_top()
print(uno_deck)
print(discard_deck)
"""
 
def play_uno():
    #playing card class (made adjustments for uno)
    class PlayingCard:
       
        def __init__(self,v,c):
           
            self.__value = v
            self.__suit = c
 
        def getValue(self):
            return self.__value
 
        def getColor(self):
            return self.__suit
           
        def __repr__(self): #this changes the print value for uno specific cards but not the self.__value
            printval = self.__value
            if self.__value == 10:
                printval = "Reverse"
            elif self.__value == 11:
                printval = "Skip"
            elif self.__value == 12:
                printval = "Draw 2"
            elif self.__value == 13:
                printval = "Card"
            elif self.__value == 14:
                printval = "Draw 4"
            return str(self.__suit)+" "+str(printval)
 
    #Portion from in class work that includes shuffle
    import random
 
    from numpy import true_divide
    class Deck:
       
        def __init__(self):
            self.__card_list = []  #the deck will be initially empty
           
        def put_on_top(self,card):
            self.__card_list.append(card)
           
        def remove_from_top(self):
            if len(self.__card_list) == 0:
                reshuffle(uno_deck, discard_deck)
            else:
                return self.__card_list.pop()
 
        def __repr__(self):
            return str(self.__card_list)
 
        def shuffle(self):
            return random.shuffle(self.__card_list)
        def is_empty(self):
            if len(self.__card_list) == 0:
                return True
            else:
                return False
        def size(self):
            return len(self.__card_list)
 
    #First I need to make a hand class and then I need to make it so It will deal cards for however many people are playing
    class Hand:
        def __init__(self, name):
            self.__card_list = []
            self.__name = name
       
        def play(self,card): #might need to make this more complicated
            counter = 0
            for x in self.__card_list:
                if x == card:
                    index = counter
                counter += 1
            return self.__card_list.pop(index)
 
        def draw(self):
            card_drawn = uno_deck.remove_from_top()
            self.__card_list.append(card_drawn)
            return card_drawn
 
        def size(self):
            return len(self.__card_list)
 
        def getCards(self):
            return self.__card_list
 
        def getValues(self):
            value_list = []
            for a in self.__card_list:
                value_list.append(a.getValue())
            return value_list
 
        def getColors(self):
            color_list = []
            for a in self.__card_list:
                color_list.append(a.getColor())
            return color_list
 
        def getPlayer(self):
            return self.__name
 
        def __repr__(self):
           
            return str(self.__name) + ": " + str(self.__card_list)
 
            #In this spot we could include another function by sorting a list different ways
            #This could be value, color, or some other factor
 
    #Discard pile should be a stack that you can view or reference that eventually will get reshuffled
    class Stack:
        def __init__(self):
            self.items = []
 
        def isEmpty(self):
            return self.items == []
 
        def push(self, item):
            self.items.append(item)
 
        def pop(self):
            return self.items.pop()
 
        def size(self):
            return len(self.items)
 
        def peek(self):
            return self.items[-1]
 
        def __repr__(self):
            return "Discard Pile: " + str(list(self.items))
 
    #Reshuffle Function
    def reshuffle(deck, discard_pile):
        temp = discard_pile.pop()
        for num in range(discard_pile.size()):
            deck.put_on_top(discard_pile.pop())
        deck.shuffle()
        for n in range(discard_pile.size()):
            discard_pile.pop()
        discard_pile.push(temp)
 
    colors = ["Blue", "Yellow", "Red", "Green", "Wild"] #Testing change back to wild
    primary_colors = ["Blue", "Yellow", "Red", "Green"]
 
    #This portion creates the UNO deck of cards
    uno_deck = Deck()
    discard_deck = Stack()
 
    def setup():
        for c in colors:
            if c in primary_colors:
                for v in [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12]: #10-12 is reverse, skip, or draw 2
                    curr_card = PlayingCard(v,c)
                    uno_deck.put_on_top(curr_card)
            else:
                for v in [13,13,13,13,14,14,14,14]:
                    curr_card = PlayingCard(v,c)
                    uno_deck.put_on_top(curr_card)
        uno_deck.shuffle()
 
    setup()
   
    num_players = int(input("How many people are playing (2-10): "))
    players_list = []
 
    #Trying to automate creating players
    if num_players == 2:
         p1 = Hand("Player 1")
         p2 = Hand("Player 2")
         players_list.append(p1)
         players_list.append(p2)
    elif num_players == 3:
        p1 = Hand("Player 1")
        p2 = Hand("Player 2")
        p3 = Hand("Player 3")
        players_list.append(p1)
        players_list.append(p2)
        players_list.append(p3)
    elif num_players == 4:
        p1 = Hand("Player 1")
        p2 = Hand("Player 2")
        p3 = Hand("Player 3")
        p4 = Hand("Player 4")
        players_list.append(p1)
        players_list.append(p2)
        players_list.append(p3)
        players_list.append(p4)
    elif num_players == 5:
        p1 = Hand("Player 1")
        p2 = Hand("Player 2")
        p3 = Hand("Player 3")
        p4 = Hand("Player 4")
        p5 = Hand("Player 5")
        players_list.append(p1)
        players_list.append(p2)
        players_list.append(p3)
        players_list.append(p4)
        players_list.append(p5)
    elif num_players == 6:
        p1 = Hand("Player 1")
        p2 = Hand("Player 2")
        p3 = Hand("Player 3")
        p4 = Hand("Player 4")
        p5 = Hand("Player 5")
        p6 = Hand("Player 6")
        players_list.append(p1)
        players_list.append(p2)
        players_list.append(p3)
        players_list.append(p4)
        players_list.append(p5)
        players_list.append(p6)
    elif num_players == 7:
        p1 = Hand("Player 1")
        p2 = Hand("Player 2")
        p3 = Hand("Player 3")
        p4 = Hand("Player 4")
        p5 = Hand("Player 5")
        p6 = Hand("Player 6")
        p7 = Hand("Player 7")
        players_list.append(p1)
        players_list.append(p2)
        players_list.append(p3)
        players_list.append(p4)
        players_list.append(p5)
        players_list.append(p6)
        players_list.append(p7)
    elif num_players == 8:
        p1 = Hand("Player 1")
        p2 = Hand("Player 2")
        p3 = Hand("Player 3")
        p4 = Hand("Player 4")
        p5 = Hand("Player 5")
        p6 = Hand("Player 6")
        p7 = Hand("Player 7")
        p8 = Hand("Player 8")
        players_list.append(p1)
        players_list.append(p2)
        players_list.append(p3)
        players_list.append(p4)
        players_list.append(p5)
        players_list.append(p6)
        players_list.append(p7)
        players_list.append(p8)
    elif num_players == 9:
        p1 = Hand("Player 1")
        p2 = Hand("Player 2")
        p3 = Hand("Player 3")
        p4 = Hand("Player 4")
        p5 = Hand("Player 5")
        p6 = Hand("Player 6")
        p7 = Hand("Player 7")
        p8 = Hand("Player 8")
        p9 = Hand("Player 9")
        players_list.append(p1)
        players_list.append(p2)
        players_list.append(p3)
        players_list.append(p4)
        players_list.append(p5)
        players_list.append(p6)
        players_list.append(p7)
        players_list.append(p8)
        players_list.append(p9)
    elif num_players == 10:
        p1 = Hand("Player 1")
        p2 = Hand("Player 2")
        p3 = Hand("Player 3")
        p4 = Hand("Player 4")
        p5 = Hand("Player 5")
        p6 = Hand("Player 6")
        p7 = Hand("Player 7")
        p8 = Hand("Player 8")
        p9 = Hand("Player 9")
        p10 = Hand("Player 10")
        players_list.append(p1)
        players_list.append(p2)
        players_list.append(p3)
        players_list.append(p4)
        players_list.append(p5)
        players_list.append(p6)
        players_list.append(p7)
        players_list.append(p8)
        players_list.append(p9)
        players_list.append(p10)



    #Creating player hands
    for n in range(7):
        for c in range(1,num_players+1):
            if c == 1:
                p1.draw()
            elif c == 2:
                p2.draw()
            elif c == 3:
                p3.draw()
            elif c == 4:
                p4.draw()
            elif c == 5:
                p5.draw()
            elif c == 6:
                p6.draw()
            elif c == 7:
                p7.draw()
            elif c == 8:
                p8.draw()
            elif c == 9:
                p9.draw()
            elif c == 10:
                p10.draw()
   
    discard_deck.push(uno_deck.remove_from_top())
 
    print(discard_deck)
    print(players_list)
   
     
    win = "n"
 
    #This is making the game actually run and cycling through turns
    while win.lower() != "y":
        for player in players_list:
                top_card = discard_deck.peek()
                temp_color = ""
                if top_card.getValue() in player.getValues() or top_card.getColor() in player.getColors() or "Wild" in player.getColors() or card.getColor() == temp_color:
                    print(top_card) #If it passes the statement above, that means that they can play a card
 
                    #Trying to make card selection that are available
                    playable = []
                    for card in player.getCards():
                        if card.getValue() == top_card.getValue() or card.getColor() == top_card.getColor() or card.getColor() == "Wild" or card.getColor() == temp_color:
                            playable.append(card)
 
                    print(player.getPlayer(), "Hand: ", player.getCards())
                    print(player.getPlayer(), "playable cards:", playable)
                   
                    choice_index = int(input("Which card would you like to play (Input a number based on order of list): "))
 
                    counter = 0
                    for v in player.getCards():
                        if v == playable[choice_index - 1]:
                            dex = counter
                        counter += 1
                       
                    print((player.getCards())[dex])
                    temp_color = player.play(player.getCards()[dex])
                    discard_deck.push(temp_color)
 
                    if temp_color.getColor() == "Wild":
                        print(primary_colors)
                        temp_dex = int(input("Select which color you would like to change it to. (1-4)"))
                        temp_color = primary_colors[temp_dex - 1]
                        print(temp_color)
 
                    print(discard_deck)
                    print(player.size())
 
                    #Breaks out of the while loop
                    if player.size() == 0:
                        winner = player
                        break
                else:
                    print(player.getPlayer(), "drew:", player.draw())
    print(winner)
 
play_uno()
 

#I think I got drawing set up I just need to get playing and game rules
 
#Potentially using a sorting method to make it so you can view your hand in different orders
 
#do we automate it so you can only select valid options to go on the pile and or make it so if you cant play,
#that it will automatically draw for you?