import streamlit as st
import random

# ---------------------------
# 1. Title Section
# ---------------------------
st.title("🎮 Rock, Paper, Scissors Game")
st.write("Welcome! Play against the computer and see who wins.")

# ---------------------------
# 2. Initialize State
# ---------------------------
if "user_points" not in st.session_state:
    st.session_state.user_points = 0
if "computer_points" not in st.session_state:
    st.session_state.computer_points = 0

# ---------------------------
# 3. User Input Section
# ---------------------------
st.header("👉 Your Turn")
user_pick = st.radio("Choose Rock, Paper, or Scissors:", ["rock", "paper", "scissors"])

if st.button("Play"):
    # Computer random choice
    computer_pick = random.choice(["rock", "paper", "scissors"])

    st.write(f"💻 Computer picked: **{computer_pick}**")

    # ---------------------------
    # 4. Game Logic Section
    # ---------------------------
    if user_pick == "rock" and computer_pick == "scissors":
        st.success("🎉 You won!")
        st.session_state.user_points += 1

    elif user_pick == "paper" and computer_pick == "rock":
        st.success("🎉 You won!")
        st.session_state.user_points += 1

    elif user_pick == "scissors" and computer_pick == "paper":
        st.success("🎉 You won!")
        st.session_state.user_points += 1

    elif user_pick == computer_pick:
        st.info("🤝 It's a tie!")

    else:
        st.error("😢 You lost!")
        st.session_state.computer_points += 1

# ---------------------------
# 5. Score Section
# ---------------------------
st.header("📊 Scoreboard")
col1, col2 = st.columns(2)
with col1:
    st.metric("Your Score", st.session_state.user_points)
with col2:
    st.metric("Computer Score", st.session_state.computer_points)

# ---------------------------
# 6. Reset Section
# ---------------------------
if st.button("Reset Game"):
    st.session_state.user_points = 0
    st.session_state.computer_points = 0
    st.info("Game has been reset!")
