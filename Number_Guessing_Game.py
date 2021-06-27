import random

secretNumber = random.randint(1, 20)
userGuesses = 0
userInput = False

while userInput == False:
    player_name = input("Welcome! What is your name\n")
    print(player_name +'\t'"Let's play a game!")
    print("I'll think of a number between 1 and 20 and you have 6 attempts to get it right.")
    print("What is your first guess?")

    while userGuesses <= 5:

        userInput = input()

        if int(userInput) > secretNumber:
            print("Too High! Try again!")
            userGuesses += 1

        elif int(userInput) < secretNumber:
            print("Too Low! Try again!")
            userGuesses += 1

        else:
            print("Congratulations! You guessed the secret number in " + str(userGuesses + 1) + " guesses!")
            print("Would you like to play again? Y or N")
            playGame = input()
            if playGame == "Y":
                userInput = False
                userGuesses = 0
                break
            else:
                userInput = True
                print("Goodbye!")

    else:
        print("You have run out of guesses! The number I was thinking of was " + str(secretNumber) + ". Better luck "
                                                                                                     "next time!")
