import random
from colorama import Fore, Style

computer_score = 0
user_score = 0
tie_rounds = 0
# This is a basic Python script for me to learn Python
# I am building a very basic rock paper scissors game.
def determine_round_winner(user_input, computer_action):
    global tie_rounds
    global user_score
    global computer_score

    if user_input == computer_action:
        print(f"Both players chose {user_input}, {Fore.CYAN}tie{Style.RESET_ALL}.")
        tie_rounds += 1
    elif user_input == "rock":
        if computer_action == "scissors":
            print(f"Rock smashes scissors! You {Fore.GREEN}win{Style.RESET_ALL}!")
            user_score += 1
        else:
            print(f"Paper covers rock! You {Fore.RED}lose{Style.RESET_ALL}.")
            computer_score += 1
    elif user_input == "paper":
        if computer_action == "rock":
            print(f"Paper covers rock! You {Fore.GREEN}win{Style.RESET_ALL}!")
            user_score += 1
        else:
            print(f"Scissors cuts paper! You {Fore.RED}lose{Style.RESET_ALL}.")
            computer_score += 1
    elif user_input == "scissors":
        if computer_action == "paper":
            print(f"Scissors cuts paper! You {Fore.GREEN}win{Style.RESET_ALL}!")
            user_score += 1
        else:
            print(f"Rock smashes scissors! You {Fore.RED}lose{Style.RESET_ALL}.")
            computer_score += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_round = 0

    valid_choices = ["rock", "paper", "scissors"]

    while True:
        while user_score < 5 and computer_score < 5:
            computer_action = random.choice(valid_choices)
            user_input = input("Choose rock, paper, or scissors: ").lower()

            while user_input not in valid_choices:
                print("You did not enter rock, paper, or scissors. Please re-enter your input.")
                user_input = input("Choose rock, paper, or scissors: ").lower()

            print(f"You chose {user_input}, and the computer chose {computer_action}.")

            determine_round_winner(user_input, computer_action)

            game_round += 1

            print(f"Your score: {user_score}, Computer Score: {computer_score}\nTie Rounds: {tie_rounds} after round {game_round}!")

        print("\nGame over.")

        play_again = input("Would you like to play another round? (y/n): ")
        if play_again.lower() != "y":
            print("Thanks for playing!")
            break
        else:
            computer_score = 0
            user_score = 0
            tie_rounds = 0
            game_round = 0
