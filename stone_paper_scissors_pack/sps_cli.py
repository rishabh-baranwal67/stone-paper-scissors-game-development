#!/usr/bin/env python3
"""
Stone-Paper-Scissors (CLI)
Run: python sps_cli.py
"""

import random

CHOICES = ["stone", "paper", "scissor"]

def decide_winner(user, comp):
    if user == comp:
        return "draw"
    wins = {("stone", "scissor"), ("paper", "stone"), ("scissor", "paper")}
    return "user" if (user, comp) in wins else "comp"

def play():
    print("=== Stone • Paper • Scissor ===")
    print("Type stone/paper/scissor or 'q' to quit.")
    user_score = comp_score = draws = 0

    while True:
        user = input("\nYour move [stone/paper/scissor/q]: ").strip().lower()
        if user in ("q", "quit", "exit"):
            break
        if user not in CHOICES:
            print("❗ Invalid choice. Try again.")
            continue

        comp = random.choice(CHOICES)
        result = decide_winner(user, comp)

        print(f"Computer chose: {comp}")
        if result == "draw":
            print("Result: It's a draw 🤝")
            draws += 1
        elif result == "user":
            print("Result: You win 🎉")
            user_score += 1
        else:
            print("Result: Computer wins 💻")
            comp_score += 1

        print(f"Score -> You: {user_score}  Computer: {comp_score}  Draws: {draws}")

    print("\nThanks for playing! Final score:")
    print(f"You: {user_score}  Computer: {comp_score}  Draws: {draws}")
    if user_score > comp_score:
        print("🏆 You won the session!")
    elif comp_score > user_score:
        print("🤖 Computer won the session!")
    else:
        print("🤝 Session ended in a draw.")

if __name__ == "__main__":
    play()
