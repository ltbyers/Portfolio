letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]#Letters A-Z
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]#Points for each letter
letter_to_points = {letter:points for letter, points in zip(letters, points)}#Create dictionary with letters and their corresponding points

letter_to_points[" "] = 0#Blank tiles are worth 0 points

player_to_words = {"player1": ["blue", "tennis", "exit"], "wordNerd": ["earth", "eyes", "machine"], "Lexi Con": ["eraser", "belly", "husky"], "Prof Reader": ["zap", "coma", "period"]}

def calculate_player_points(player,word):
  if player in player_to_words:#Make sure the player is in the game
    player_to_words[player].append(word)#Add word to players list of words
    player_to_points = {}#Create dictionary for keeping track of each player's points
    for player,words in player_to_words.items():
      player_points = 0#Points start at 0
      for word in words:
        word = word.upper()#Letters in letter_to_points are all uppercase so make the word uppercase as well
        for letter in word:
          player_points += letter_to_points[letter]#For each letter in the word add the corresponding points to the player's total points in player_points
        player_to_points[player] = player_points#Add player name and points to player_to_points dictionary
    return player_to_points, player_to_words#Return dictionaries of players and their points and players and their words
  else:
    return "That is not a valid player in this game!"#Return error if user inputs a player that is not in the game