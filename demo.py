import random

upperCeil = 101
lowerCeil = 0

computerAttempts = 0

while(True):
    computerNumber = random.randint(lowerCeil, upperCeil)
    print(computerNumber)
    computerAttempts += 1

    userInput = input("Is the number correct? Y/N: ")

    if(userInput.upper() == "Y"):
        break;
    else:
        userInput = input("Is the number generated greater or smaller? G/S: ")

        if userInput.upper() == "G":
            lowerCeil = computerNumber + 1
        else:
            upperCeil = computerNumber

print("The computer guessed the number in", computerAttempts, "attempts")