import random
import time

# Define constants to represent rock, paper, and scissors
rock = 1
paper = 2
scissors = 3

# Create dictionaries to map numbers to their corresponding names and winning rules
names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

# Initialize player and computer scores
player_score = 0
computer_score = 0

# Function to start the game
def start():
    print("Let's play a game of Rock, Paper, Scissors.")
    while game():
        pass
    scores()

# Function to handle the game logic
def game():
    player = move()  # Get the player's move
    computer = random.randint(1, 3)  # Generate a random move for the computer
    result(player, computer)  # Determine the result of the game
    return play_again()  # Ask the player if they want to play again

# Function for the player to make a move
def move():
    while True:
        print()
        player = input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print("Oops! I didn't understand that. Please enter 1, 2, or 3.")

# Function to determine the result of the game
def result(player, computer):
    print("1...")
    time.sleep(0.5)
    print("2...")
    time.sleep(0.5)
    print("3!")
    time.sleep(0.5)
    print("Computer threw {0}!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Tie game ")
    else:
        if rules[player] == computer:
            print("Your victory has been assured.")
            player_score += 1
        else:
            print("The computer laughs as you realize you have been defeated.")
            computer_score += 1

# Function to ask the player if they want to play again
def play_again():
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes"):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")

# Function to display the scores
def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player:", player_score)
    print("Computer:", computer_score)

# Main entry point of the program
if __name__ == '__main__':
    start()  # Start the game
