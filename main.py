# import random module
import random

# Print multiline game instructions

print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper -> Paper beats Rock \n"
      + "Rock vs scissor -> Rock beats Scissors \n"
      + "paper vs scissor -> Scissors beats Paper \n")

while True:
    print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")

    # take the input from user
    user_input = (input("Your turn: "))

    # change to uppercase if user inputs lowercase character
    choice = user_input.upper()

    # looping until user enters valid input
    choice_list = ["R", "P", "S"]
    while choice not in choice_list:
        print("Invalid input. Please try again...")
        choice = input("Enter valid input: ")

    # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == "R":
        choice_name = 'Rock'
    elif choice == "P":
        choice_name = 'paper'
    else:
        choice_name = 'scissors'

    # print user choice
    print("Your choice is: " + choice_name)
    print("\nNow its computer's turn.......")

    # Computer chooses randomly any letter
    # from choice_list
    comp_choice = random.choice(choice_list)

    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == "R":
        comp_choice_name = 'Rock'
    elif comp_choice == "P":
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    # print computer's choice
    print("Computer's choice is: " + comp_choice_name)

    # print both user and computer's choice
    print("Player (" + (choice_name)+") : " + "CPU (" + comp_choice_name+")")

    # condition for winning
    if((choice == "R" and comp_choice == "P") or
       (choice == "P" and comp_choice == "R")):
        print("Paper covers Rock => ", end="")
        result = "paper"

    elif((choice == "R" and comp_choice == "S") or
         (choice == "S" and comp_choice == "R")):
        print("Rock smashes Scissors =>", end="")
        result = "Rock"

    elif((choice == "R" and comp_choice == "R") or
         (choice == "S" and comp_choice == "S") or (choice == "P" and comp_choice == "P")):
        print("It's a Tie! =>", end="")
        result = "Tie"

    else:
        print("Scissors cuts Paper =>", end="")
        result = "scissors"

    # Printing either user wins, computer wins, or if it's a tie
    if result == choice_name:
        print("<== You won ==>")

    elif result == "Tie":
        print("<== Play Again. ==>")

    else:
        print("<== Computer won ==>")

    # restart the game
    print("Do you want to play again? \nEnter any key to continue, or 'N' to exit")
    ans = input()

    # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break


# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")
