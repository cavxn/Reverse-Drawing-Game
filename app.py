import streamlit as st
import random
import time
from draw_utils import draw_strokes
from quickdraw_loader import load_sketch
from game_logic import check_guess

# Setup
st.set_page_config(page_title="Reverse Drawing Game", layout="centered")
st.title("🎨 Reverse Drawing: AI Draws, You Guess!")

# Categories
categories = ['apple', 'bicycle', 'cat', 'tree', 'clock', 'star', 'face', 'flower', 'pizza', 'house']

# Initialize session state
if 'round' not in st.session_state:
    st.session_state.round = 1
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'used_categories' not in st.session_state:
    st.session_state.used_categories = []
if 'category' not in st.session_state:
    st.session_state.category = random.choice(categories)
if 'guess_submitted' not in st.session_state:
    st.session_state.guess_submitted = False
if 'guess_correct' not in st.session_state:
    st.session_state.guess_correct = False
if 'guess' not in st.session_state:
    st.session_state.guess = ""
if 'game_active' not in st.session_state:
    st.session_state.game_active = True

# Game header
st.markdown(f"🎯 **Round:** {st.session_state.round} &nbsp;&nbsp;&nbsp; 🏆 **Score:** {st.session_state.score}")

# Stop / Reset Game
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🔄 Reset Game"):
        st.session_state.round = 1
        st.session_state.score = 0
        st.session_state.used_categories = []
        st.session_state.guess = ""
        st.session_state.guess_submitted = False
        st.session_state.guess_correct = False
        st.session_state.game_active = True
        st.rerun()
with col2:
    if st.button("🛑 Stop Game"):
        st.session_state.game_active = False
        st.success("🛑 Game stopped. Thanks for playing!")

# Stop if game is inactive
if not st.session_state.game_active:
    st.stop()

st.divider()
st.subheader("🤖 AI is drawing something...")

# Load and draw sketch
strokes = load_sketch(st.session_state.category)
if not strokes:
    st.error("⚠️ Failed to load sketch.")
    st.stop()
else:
    draw_strokes(strokes, draw_time=5)

st.divider()

# Input guess
if not st.session_state.guess_correct:
    st.session_state.guess = st.text_input("🔤 Your Guess:", key="guess_input")

    if st.button("✅ Submit Guess"):
        user_guess = st.session_state.guess.strip()
        if user_guess:
            if check_guess(user_guess, st.session_state.category):
                st.session_state.score += 1
                st.session_state.guess_correct = True
                st.success("🎉 Correct! Press 'Next Round' to continue.")
                st.balloons()
            else:
                st.session_state.guess_submitted = True

# Show wrong answer feedback
if st.session_state.guess_submitted and not st.session_state.guess_correct:
    st.error(f"❌ Nope! The correct answer was: **{st.session_state.category}**")
    if st.button("🔁 Try Again"):
        st.session_state.guess_submitted = False
        st.session_state.guess = ""
        st.rerun()

# Next Round button appears only if correct
if st.session_state.guess_correct:
    if st.button("➡️ Next Round"):
        st.session_state.round += 1
        st.session_state.guess_correct = False
        st.session_state.guess_submitted = False
        st.session_state.guess = ""

        # Avoid repeating previous categories
        st.session_state.used_categories.append(st.session_state.category)
        remaining = list(set(categories) - set(st.session_state.used_categories))
        if not remaining:
            st.session_state.used_categories = []  # Reset if all used
            remaining = categories
        st.session_state.category = random.choice(remaining)

        st.rerun()
