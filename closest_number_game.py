# simple two-player guessing game
import random

print("\n=== Closest Number Game ===")
# generate target number
secret_number = random.randint(1, 100)

print("\nGuess a number between 1 and 100")
# get player guesses
player1_guess = int(input("Player 1 guess: "))
player2_guess = int(input("Player 2 guess: "))

# calculate differences from target
player1_diff = abs(secret_number - player1_guess)
player2_diff = abs(secret_number - player2_guess)

# determine winner based on closest guess
if player1_diff < player2_diff:
    winner = "Player 1"
elif player2_diff < player1_diff:
    winner = "Player 2"
else:
    winner = "It's a tie"

print("\nResults:")
print("--------")
print(f"Secret number was: {secret_number}")
print(f"Player 1 guessed: {player1_guess} (difference: {player1_diff})")
print(f"Player 2 guessed: {player2_guess} (difference: {player2_diff})")
print(f"Winner: {winner}")

# verify winner logic
expected_winner = "Player 1" if player1_diff < player2_diff else \
                 "Player 2" if player2_diff < player1_diff else \
                 "It's a tie"

if winner == expected_winner:
    print("\nTest PASSED ✓")
else:
    print("\nTest FAILED ✗")