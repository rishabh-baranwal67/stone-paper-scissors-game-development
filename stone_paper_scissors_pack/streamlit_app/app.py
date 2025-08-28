#!/usr/bin/env python3
# Stone-Paper-Scissors (Streamlit Web App)
# Run locally: streamlit run app.py

import random
import streamlit as st

st.set_page_config(page_title="Stone • Paper • Scissor", page_icon="🎮")

CHOICES = ["stone", "paper", "scissor"]
EMOJI = {"stone": "🪨", "paper": "📄", "scissor": "✂️"}

def decide_winner(user, comp):
    if user == comp:
        return "draw"
    wins = {("stone", "scissor"), ("paper", "stone"), ("scissor", "paper")}
    return "user" if (user, comp) in wins else "comp"

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "comp_score" not in st.session_state:
    st.session_state.comp_score = 0
if "draws" not in st.session_state:
    st.session_state.draws = 0
if "last" not in st.session_state:
    st.session_state.last = None

st.title("Stone • Paper • Scissor 🎮")
st.caption("Play against the computer. First to N wins (optional).")

colA, colB = st.columns([2,1])
with colA:
    target_enabled = st.checkbox("Play best of N (first to N wins)", value=False)
with colB:
    n_target = st.number_input("N", min_value=1, max_value=20, value=5, step=1)

st.markdown("---")

c1, c2, c3 = st.columns(3)

def on_click(choice):
    comp = random.choice(CHOICES)
    outcome = decide_winner(choice, comp)
    if outcome == "draw":
        st.session_state.draws += 1
    elif outcome == "user":
        st.session_state.user_score += 1
    else:
        st.session_state.comp_score += 1
    st.session_state.last = (choice, comp, outcome)

with c1:
    if st.button(f"{EMOJI['stone']}  Stone", use_container_width=True):
        on_click("stone")
with c2:
    if st.button(f"{EMOJI['paper']}  Paper", use_container_width=True):
        on_click("paper")
with c3:
    if st.button(f"{EMOJI['scissor']}  Scissor", use_container_width=True):
        on_click("scissor")

st.markdown("### Scoreboard")
st.write(f"**You:** {st.session_state.user_score} | **Computer:** {st.session_state.comp_score} | **Draws:** {st.session_state.draws}")

if st.session_state.last:
    u, c, o = st.session_state.last
    result_text = "It's a draw 🤝" if o == "draw" else ("You win 🎉" if o == "user" else "Computer wins 💻")
    st.info(f"You: {EMOJI[u]}  vs  Computer: {EMOJI[c]}  →  {result_text}")

# Win condition when playing best of N
if target_enabled:
    if st.session_state.user_score >= n_target:
        st.success(f"🏆 You reached {n_target} wins!")
    elif st.session_state.comp_score >= n_target:
        st.error(f"🤖 Computer reached {n_target} wins!")

left, right = st.columns(2)
with left:
    if st.button("Reset Scores"):
        st.session_state.user_score = st.session_state.comp_score = st.session_state.draws = 0
        st.session_state.last = None
with right:
    st.caption("Tip: Click any move to play a round.")

st.markdown("---")
st.caption("Built with Streamlit • Enjoy!")
