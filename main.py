# This Allows The Computer To Pick A Random either 'Rock', 'Paper' Or 'Scissor'.
import random

print("Welcome To rock Paper Scissors Game!!! !!!")
print("-------------------------------------")


# Defining A Function Play To determine Win or Play.
def choice():
    # Takes In the Input From The User to determine The result Of the Game...
    player = input("What's Your Choice? 'r' for rock, 'p' for paper, 's' for scissors :: \n")
    player = player.lower()

    outcome = ['r', 'p', 's']

    # This Come in Handy When The User Or Player Input An Invalid Choice
    while player not in outcome:
        print("invalid input!, Please try Again")
        player = input("What's Your Choice? 'r' for rock, 'p' for paper, 's' for scissors :: \n")
        player = player.lower()

    # The Cpu select a choice from the defined choice made
    cpu = random.choice(['r', 'p', 's'])

    # This submits the tie made the player
    if player == cpu:
        print("It's a tie!\n You Chose = {} : Computer = {}.".format(player, cpu))
        return choice()

    # This submits the win made the player
    if is_win(player, cpu):
        return "You Won!!!\n You Chose = {} : Computer = {}.".format(player, cpu)

    # This submits the lost made the player
    return "You lost!!!\n You Chose = {} : Computer = {}.".format(player, cpu)


# Defining the function is_win to check for wins by the Player
def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    return False


# To run the entire program
if __name__ == '__main__':
    print(choice())
