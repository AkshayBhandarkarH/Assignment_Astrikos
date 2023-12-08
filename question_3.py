"""3. Create a basic rock paper scissors game. 
Take 2 user inputs from 2 players. You can use R, P and S are possible user inputs. Play the game 
for 10 rounds and declare the winner.
Rules of the game 
Rock vs Scissors - Rock wins 
Rock vs Paper - Paper wins
Paper vs Scissors - Scissor wins 
Eg: Game 1: Player1 = R, Player2 = S, Output: Player1 wins 
Player1 = P, Player2 = P, Output: Draw
Final Winner: Player with maximum wins
"""
import random

def play_round(player1, player2):
    if player1 == player2:
        return "Draw"
    elif (player1 == "R" and player2 == "S") or (player1 == "P" and player2 == "R") or (player1 == "S" and player2 == "P"):
        return "Player1 wins"
    else:
        return "Player2 wins"

def get_user_input(player):
    while True:
        user_input = input(f"Player{player}, enter your choice (R/P/S): ").upper()
        if user_input in ["R", "P", "S"]:
            return user_input
        else:
            print("Invalid input. Please enter R, P, or S.")

def play_game():
    player1_wins = player2_wins = draws = 0

    for round_num in range(1, 11):
        print(f"\nGame {round_num}:")
        player1 = get_user_input(1)
        player2 = get_user_input(2)

        result = play_round(player1, player2)
        print(f"Player1 = {player1}, Player2 = {player2}, Output: {result}")

        if "Player1" in result:
            player1_wins += 1
        elif "Player2" in result:
            player2_wins += 1
        else:
            draws += 1

    print("\nGame Over!")
    print(f"Player1 wins: {player1_wins}")
    print(f"Player2 wins: {player2_wins}")
    print(f"Draws: {draws}")

    if player1_wins > player2_wins:
        print("Final Winner: Player1")
    elif player2_wins > player1_wins:
        print("Final Winner: Player2")
    else:
        print("It's a Tie!")

play_game()
