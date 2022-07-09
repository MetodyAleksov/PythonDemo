import random

choices = ["Rock", "Paper", "Scissors"]

playerWins = 0
computerWins = 0

playerChoice = input("Rock, paper or scissors? or quit by typing quit: ")

while(playerChoice != "quit"):
    computerChoice = random.choice(choices)
    print("Computer choice:", computerChoice.lower())

    playerWon = True

    if(playerChoice.lower() == computerChoice.lower()):
        playerWins += 1
        computerWins += 1
        print("Draw")
    else:
        if (   (playerChoice.lower() == "rock" and computerChoice.lower() == "papper")
            or (playerChoice.lower() == "papper" and computerChoice.lower() == "scissors")
            or (playerChoice.lower() == "scissors" and computerChoice.lower() == "rock")):
            playerWon = False
        if playerWon:
            playerWins += 1
            print("Player wins with a choice of", playerChoice.upper(), "and computer choice of", computerChoice.upper())
        else:
            computerWins += 1
            print("Computer wins with a choice of", computerChoice.upper(), "and player choice of", playerChoice.upper())
    
    print("Score:\nPlayer wins: {0}\nComputer wins: {1}\n".format(playerWins, computerWins))
    playerChoice = input("Rock, paper or scissors? or quit by typing quit: ")

print("Score:\nPlayer wins: {0}\nComputer wins: {1}\n".format(playerWins, computerWins))