"""Cows and bulls game"""
# Randomly generate a 3-digit number. Ask the user to guess a 3-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
# tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.


import random


# check if number provided by user lets win the game or not.
def guess(b):

    if len(b) == 3:
        for i in range(len(a)):
            if a[i] == b[i]:
                print("Cow")
            else:
                print("Bull")
    else:
        print("You haven't entered 3-digit number")

    while True:
        if a[0] == b[0] and a[1] == b[1] and a[2] == b[2]:
            print("You won the game!")
            break
        else:
            print("Try again")
            play_again(b)
        break


# gives a clue for the user
def get_clue(b):

    # clue about the last digit
    if b[2] == 0 or 2 or 4 or 6 or 8:
        print("The number is divided by 2")
    elif (b[1] + b[2]) % 3 == 0:
        print("The number is divided by 3")
    elif b[2] % 4 == 0:
        print("The number is divided by 4")
    elif b[2] == 0 or 5:
        print("The number is divided by 5")
    elif b[2] % 2 == 0 and b[2] % 3 == 0:
        print("The number is divided by 6")


# ask user if play again the game
def play_again(b):

    again = input("Would you like to play again? Enter Y if yes, N if no. ")

    if again == "Y":

        clue = input("Would you like to get a clue? Enter Y if yes, N if no. ")

        if clue == "Y":
            get_clue(b)
            b = list(input("Guess a 3-digit number. What is your answer? "))
            guess(b)
        else:
            b = list(input("Guess a 3-digit number. What is your answer? "))
            guess(b)
    else:
        print("Game over.")


if __name__ == "__main__":
    play = True
    a = str(random.randint(100, 999))

    print("Welcome to Cows and bulls game! Your task is to guess the number that I generated. \nFor every number "
          "in the wrong place, you get a Cow. \nFor every one in the right place, you get a Bull.\n"
          "The game ends when you get 3 Bulls!")

    b = list(input("Guess a 3-digit number. What is your answer? "))

    print(a)

    while play:
        guess(b)
        break
