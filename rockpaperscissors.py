# Rock, Paper, Scissors (vs Computer)

def play_game():
    # step 1 - import module and set choices
    import random
    options = ["rock", "paper", "scissors"]
    # step 2 - get user & computer choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    print("Computer choice :",computer_choice)
    # step 3 - check for winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

def main_func():
    play_again = "yes"
    while play_again == "yes":
     play_game()
     play_again = input("Play again? (yes/no):").lower()

main_func()

