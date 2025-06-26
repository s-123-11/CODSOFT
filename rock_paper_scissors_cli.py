# rock_paper_scissors.py
import random

print("--- Let's play Rock-Paper-Scissors! ---")
user_score = 0
computer_score = 0

while True:
    print("\nType 'rock', 'paper', or 'scissors'")
    user_choice = input("Your choice: ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    if user_choice not in options:
        print("Invalid choice. Try again.")
        continue

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("Score => You:", user_score, "Computer:", computer_score)

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
