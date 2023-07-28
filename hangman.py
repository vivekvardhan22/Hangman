import random

def hangman(word):
  # Initialize the game
  guesses_left = 8
  correct_guesses = []
  incorrect_guesses = []

  # Display the game board
  print_game_board(word, correct_guesses, incorrect_guesses)

  # Start the game loop
  while guesses_left > 0:
    # Get the user's guess
    guess = input("Guess a letter: ")

    # Check if the guess is correct
    if guess in word:
      # Add the guess to the list of correct guesses
      correct_guesses.append(guess)

      # Update the game board
      print_game_board(word, correct_guesses, incorrect_guesses)

      # Check if the player has won
      if len(correct_guesses) == len(word):
        print("You won!")
        break
    else:
      # Add the guess to the list of incorrect guesses
      incorrect_guesses.append(guess)

      # Update the game board
      print_game_board(word, correct_guesses, incorrect_guesses)

      # Decrement the number of guesses left
      guesses_left -= 1

  # Check if the player has lost
  if guesses_left == 0:
    print("You lost!")
    print("The word was:", word)

def print_game_board(word, correct_guesses, incorrect_guesses):
  # Print the dashes representing the word
  dashes = []
  for letter in word:
    if letter in correct_guesses:
      dashes.append(letter)
    else:
      dashes.append("_")

  print(" ".join(dashes))

  # Print the incorrect guesses
  print("Incorrect guesses: " + ", ".join(incorrect_guesses))

if __name__ == "__main__":
  # Choose a random word
  word = random.choice(["computer","werewolf","seeker","cinderella","mulan","hajj","supernatural","costume","spooky","midnight","nightmare","pumpkin","eyepatch","trample","vampire","luxury","headsman","assassin","executor","crwth","web","ump","vellum","bugaboo","yoyo","injury","jumbo","nightclub","pneumonia","xylophone","jigsaw","flyby","chthonic","kickshaw","affix","beekeeper","funny","puppy","wizard","pneumonia","pneumonia","ivy","stronghold","kiwifruit", "python", "javascript", "machinelearning", "artificialintelligence","abruptly","absurd","askew","axiom","gabby","galaxy","bikini","unzip","unknown"])

  # Play the game
  hangman(word)
