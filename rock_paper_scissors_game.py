import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("The rules are simple: Rock smashes scissors, scissors cuts paper, paper covers rock.")

    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please select from rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

rock_paper_scissors()
