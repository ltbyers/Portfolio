#Global Declarations
import random
coins = 100 #Set starting coins

#Betting Game Functions Below

#Heads or Tail Betting Game
def coin_flip(bet,callIt):

  coin = random.randint(1,2)
  #Check for valid bet
  if bet <= 0: #Makes sure a bet of at least 1 coin is made
    print("Sorry, you must bet at least 1 coin.")
  elif bet > coins: #Makes sure a bet does not exceed available coins
    print("Sorry, you do not have enough coins to make that bet.")
  #If a valid bet is made start the game
  else:
    #Print the coin result for the player
    if coin == 1: #1 equals heads
      print("It's Heads!")
    elif coin == 2: #2 equals tails
      print("It's Tails!")
    #If guess was correct
    if (callIt.lower() == "heads" and coin == 1) or (callIt.lower() == "tails" and coin == 2):
      print("Congrats, you won! Your bet of " + str(bet) + " coins is now " + str(bet*2) + " coins.")
      return bet #Doubles original bet
    #If guess was incorrect
    else:
      print("Sorry, you lost your bet of " + str(bet) + " coins. Please try again!")
      return -bet #Loses original bet


#Cho-Han Betting Game
def roll_dice(bet,predict):

  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  #Check for valid bet
  if bet <= 0: #Makes sure a bet of at least 1 coin is made
    print("Sorry, you must bet at least 1 coin.")
  elif bet > coins: #Makes sure a bet does not exceed available coins
    print("Sorry, you do not have enough coins to make that bet.")
  #If a valid bet is made start the game
  else:
    #Print the dice for the player
    print("The first dice was a " + str(dice1) + " and the second dice was a " + str(dice2))
    if (dice1 + dice2) % 2 == 0: #Checks to see if total is odd or even
      result = "even"
      print("Even!")
    else:
      result = "odd"
      print("Odd!")
    #If guess was correct
    if result == predict.lower():
      print("Congrats, you won! Your bet of " + str(bet) + " coins is now " + str(bet*2) + " coins!")
      return bet #Doubles original bet
    #If guess was incorrect
    else:
      print("Sorry you lost your bet of " + str(bet) + " coins. Better luck next time.")
      return -bet #Loses original bet


#Highest Card Wins Betting Game
def high_card(bet):

  card1 = random.randint(2,14)
  card2 = random.randint(2,14)
  #Check for valid bet
  if bet <= 0: #Makes sure a bet of at least 1 coin is made
    print("Sorry, you must bet at least 1 coin.")
  elif bet > coins: #Makes sure a bet does not exceed available coins
    print("Sorry, you do not have enough coins to make that bet.")
  #If a valid bet is made start the game
  else:
    #Converts face cards from numbers to face names to print for user
    numbers_to_face = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}#Ace is high card
    if card1 in numbers_to_face:
    	card1 = numbers_to_face[card1]
    if card2 in numbers_to_face:
    	card2 = numbers_to_face[card2]
    #Print cards for player, card1 is player's card and card2 is computer's card
    print("Your card is a " + str(card1) + " and the computer's card is a " + str(card2) + ".")
    #Convert face cards back to numbers so program can compare which is highest card
    face_to_numbers = {"Jack": 11, "Queen": 12, "King": 13, "Ace": 14}#Ace is high card
    if card1 in face_to_numbers:
    	card1 = face_to_numbers[card1]
    if card2 in face_to_numbers:
    	card2 = face_to_numbers[card2]
    #If player wins
    if card1 > card2:
      print("Congrats, you won! Your bet of " + str(bet) + " coins is now " + str(bet*2) + " coins!")
      return bet
    #If computer wins
    elif card1 < card2:
      print("Sorry you lost your bet of " + str(bet) + " coins. Better luck next time.")
      return -bet
    #If there is a tie
    elif card1 == card2:
      print("It's a tie! Your bet of " + str(bet) + " coins has been returned to you. Please play again!")
      return 0


#Roulette Betting Game      
def roulette(bet,predict):

  ball = random.randint(0, 36)
  #Check for a valid bet
  if bet <= 0: #Makes sure a bet of at least 1 coin is made
    print("Sorry, you must bet higher than 0 coins.")
  elif bet > coins: #Makes sure a bet does not exceed available coins
    print("Sorry, you do not have enough coins to make that bet.")
  #If a valid bet is made start the game
  else:
    #Print where the ball landed for the player
    print(ball)
    if type(predict) == int: #If player guessed the number the ball landed on it pays out 35 to 1
      if predict == ball:
        print("Congrats, you won! Your bet of " + str(bet) + " coins is now " + str(bet*35) + " coins!")
        return bet * 34
      else:
      	print("Sorry you lost your bet of " + str(bet) + " coins. Better luck next time.")
    elif (ball % 2) == 0 and ball != 0: #Checks to see if the ball landed on an even number not including 0
      print("Even!")
      if predict.lower() == "even": #If player guessed Even correctly it pays out 2 to 1
        print("Congrats, you won! Your bet of " + str(bet) + " coins is now " + str(bet*2) + " coins!")
        return bet
      else: #If the player guessed Odd incorrectly
        print("Sorry you lost your bet of " + str(bet) + " coins. Better luck next time.")
        return -bet
    elif (ball % 2) != 0: #Checks to see if ball landed on an odd number
      print("Odd!")
      if predict.lower() == "odd": #If player guessed Odd correctly it pays out 2 to 1
        print("Congrats, you won! Your bet of " + str(bet) + " coins is now " + str(bet*2) + " coins!")
        return bet
      else: #If players guessed Even incorrectly
        print("Sorry you lost your bet of " + str(bet) + " coins. Better luck next time.")
        return -bet
    elif ball == 0: #If player guessed Even or Odd, but ball landed on 0 they lose
      print("Sorry you lost your bet of " + str(bet) + " coins. Better luck next time.")
      return -bet