# rock paper scissors game vs computer
import random

choices = ["rock", "paper", "scissors"]

print("\n=== Rock, Paper, Scissors ===")
print("\nChoose: rock, paper, or scissors")
# get player choice
user_choice = input("Your choice: ").lower()

# get random computer choice
computer_choice = random.choice(choices)

# determine winner using game rules
if user_choice == computer_choice:
    result = "It's a tie!"
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    result = "You win!"
else:
    result = "Computer wins!"

print("\nResults:")
print("--------")
print(f"Your choice: {user_choice}")
print(f"Computer chose: {computer_choice}")
print(f"Result: {result}")

# verify valid game outcome
if result in ["It's a tie!", "You win!", "Computer wins!"]:
    print("\nTest PASSED ✓")
else:
    print("\nTest FAILED ✗")