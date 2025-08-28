#!/usr/bin/env python3
"""
Stone-Paper-Scissors (Tkinter GUI)
Run: python sps_tkinter.py
"""

import tkinter as tk
import random

CHOICES = ["stone", "paper", "scissor"]
EMOJI = {"stone": "🪨", "paper": "📄", "scissor": "✂️"}

def decide_winner(user, comp):
    if user == comp:
        return "draw"
    wins = {("stone", "scissor"), ("paper", "stone"), ("scissor", "paper")}
    return "user" if (user, comp) in wins else "comp"

class SPSApp:
    def __init__(self, root):
        self.root = root
        root.title("Stone • Paper • Scissor")
        root.geometry("420x420")
        root.resizable(False, False)

        self.user_score = 0
        self.comp_score = 0
        self.draws = 0

        self.title = tk.Label(root, text="Stone • Paper • Scissor", font=("Helvetica", 18, "bold"))
        self.title.pack(pady=10)

        self.status = tk.Label(root, text="Make your move!", font=("Helvetica", 12))
        self.status.pack(pady=6)

        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack(pady=10)

        for choice in CHOICES:
            btn = tk.Button(self.choices_frame, text=f"{EMOJI[choice]}  {choice.title()}",
                            width=14, height=2, command=lambda c=choice: self.play_round(c))
            btn.pack(side=tk.LEFT, padx=6)

        self.result = tk.Label(root, text="", font=("Helvetica", 14))
        self.result.pack(pady=12)

        self.score = tk.Label(root, text=self.score_text(), font=("Helvetica", 12))
        self.score.pack(pady=8)

        self.reset_btn = tk.Button(root, text="Reset Scores", command=self.reset_scores)
        self.reset_btn.pack(pady=6)

        self.footer = tk.Label(root, text="Have fun! 🎮", font=("Helvetica", 10), fg="#666")
        self.footer.pack(side=tk.BOTTOM, pady=10)

    def score_text(self):
        return f"Score → You: {self.user_score}  Computer: {self.comp_score}  Draws: {self.draws}"

    def play_round(self, user_choice):
        comp_choice = random.choice(CHOICES)
        outcome = decide_winner(user_choice, comp_choice)

        if outcome == "draw":
            self.draws += 1
            text = "It's a draw 🤝"
        elif outcome == "user":
            self.user_score += 1
            text = "You win 🎉"
        else:
            self.comp_score += 1
            text = "Computer wins 💻"

        self.result.config(text=f"You: {EMOJI[user_choice]}  vs  Computer: {EMOJI[comp_choice]}\n{text}")
        self.score.config(text=self.score_text())

    def reset_scores(self):
        self.user_score = self.comp_score = self.draws = 0
        self.score.config(text=self.score_text())
        self.result.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = SPSApp(root)
    root.mainloop()
