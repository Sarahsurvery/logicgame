# logicgame

# import random
# import streamlit as st

# def guess_the_number():
#     if "number" not in st.session_state:
#         st.session_state.number = random.randint(1, 100)
#         st.session_state.guesses_left = 8
#         st.session_state.game_over = False
#         st.session_state.feedback = ""

#     st.markdown("<h1 style='text-align: center; color: #FF6347;'>🎮 Welcome to the Number Guessing Game! 🎮</h1>", unsafe_allow_html=True)
#     st.markdown("<h3 style='text-align: center; color: #1E90FF;'>I am thinking of a number between 1 and 100.</h3>", unsafe_allow_html=True)

#     if not st.session_state.game_over:
#         st.session_state.feedback = f"<p style='color: #32CD32;'>🎯 You have {st.session_state.guesses_left} guesses left.</p>"
#         st.markdown(st.session_state.feedback, unsafe_allow_html=True)

#         guess = st.number_input("Take a guess:", min_value=1, max_value=100, step=1, key="guess_input")

#         if guess:
#             st.session_state.guesses_left -= 1
#             if guess < st.session_state.number:
#                 st.session_state.feedback = "<p style='color: orange;'>⬇️ Too low! Try again!</p>"
#             elif guess > st.session_state.number:
#                 st.session_state.feedback = "<p style='color: orange;'>⬆️ Too high! Try again!</p>"
#             else:
#                 st.session_state.feedback = f"<p style='color: #32CD32;'>🎉 Congratulations! You guessed the correct number in {8 - st.session_state.guesses_left} tries! 🎉</p>"
#                 st.session_state.game_over = True
#     else:
#         st.session_state.feedback = f"<p style='color: #FF6347;'>😞 Game Over! The number was {st.session_state.number}.</p>"
#         st.session_state.guesses_left = 0

#     st.markdown(st.session_state.feedback, unsafe_allow_html=True)
#     st.markdown(f"<p style='color: #4682B4;'>You have {st.session_state.guesses_left} guesses left.</p>", unsafe_allow_html=True)

#     if st.session_state.game_over:
#         if st.button("Play Again", key="restart"):
#             st.session_state.clear()

# st.markdown("""
#     <style>
#         body { background-color: #f0f8ff; font-family: 'Arial', sans-serif; }
#         .stButton>button { background-color: #4CAF50; color: white; font-size: 20px; border-radius: 10px; padding: 10px 20px; }
#         .stButton>button:hover { background-color: #45a049; }
#         .stNumberInput input { font-size: 18px; text-align: center; }
#         h1, h3 { font-family: 'Helvetica', sans-serif; }
#     </style>
# """, unsafe_allow_html=True)

# guess_the_number()

import random
import streamlit as st

# Function to generate a random number and manage the game
def guess_the_number():
    """Guess The Number"""
    number = random.randint(1, 100)
    guesses_left = 8

    # Streamlit UI Components for the Game
    st.markdown("<h1 style='text-align: center; color: #FF6347;'>🎮 Welcome to the Number Guessing Game! 🎮</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #1E90FF;'>I am thinking of a number between 1 and 100.</h3>", unsafe_allow_html=True)

    guess = None
    game_over = False
    feedback = ""

    # Check if the session state is initialized for game state
    if "guesses_left" not in st.session_state:
        st.session_state.guesses_left = guesses_left
        st.session_state.number = number
        st.session_state.game_over = game_over
        st.session_state.feedback = ""
        st.session_state.guesses_left = guesses_left

    # Allow the user to input a guess
    if not st.session_state.game_over:
        st.session_state.feedback = f"<p style='color: #32CD32;'>🎯 You have {st.session_state.guesses_left} guesses left.</p>"
        st.markdown(st.session_state.feedback, unsafe_allow_html=True)

        # Create input field for the user to guess a number
        guess = st.number_input("Take a guess:", min_value=1, max_value=100, step=1, key="guess_input")

        if guess:
            st.session_state.guesses_left -= 1

            if guess < st.session_state.number:
                st.session_state.feedback = "<p style='color: orange;'>⬇️ Too low! Try again!</p>"
            elif guess > st.session_state.number:
                st.session_state.feedback = "<p style='color: orange;'>⬆️ Too high! Try again!</p>"
            else:
                st.session_state.feedback = f"<p style='color: #32CD32;'>🎉 Congratulations! You guessed the correct number in {8 - st.session_state.guesses_left} tries! 🎉</p>"
                st.session_state.game_over = True

    else:
        st.session_state.feedback = f"<p style='color: #FF6347;'>😞 Game Over! The number was {st.session_state.number}.</p>"
        st.session_state.guesses_left = 0

    # Display feedback and guesses left
    st.markdown(st.session_state.feedback, unsafe_allow_html=True)
    st.markdown(f"<p style='color: #4682B4;'>You have {st.session_state.guesses_left} guesses left.</p>", unsafe_allow_html=True)

    # Option to restart the game
    if st.session_state.game_over:
        if st.button("Play Again", key="restart"):
            st.session_state.clear()

# Add custom CSS styling for the page
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 20px;
            border-radius: 10px;
            padding: 10px 20px;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            background-color: #45a049;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .stNumberInput input {
            font-size: 18px;
            text-align: center;
        }
        h1, h3 {
            font-family: 'Helvetica', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Call the function to play the game
guess_the_number()
