import streamlit as st
import time

# Function to simulate the 2-digit lock challenge
def lock_simulation():
    st.title(" 2-Digit Lock Simulation")

    # Instructional text
    st.write("""
    Your goal is to find the correct combination to open the lock! 
    Adjust the sliders to find the code, and observe how many different combinations you try.
    """)

    # Randomly set a "secret" combination (e.g., 27)
    secret_code = 27

    # Create sliders for each digit of the 2-digit lock
    digit_1 = st.slider("Digit 1", 0, 9, 0)
    digit_2 = st.slider("Digit 2", 0, 9, 0)

    # Initialize session state for tracking attempts and timer
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None # Timer not started yet
    if 'attempts' not in st.session_state:
        st.session_state.attempts = set() # Using a set to track unique attempts

    # Start timer when the first guess is made
    if st.session_state.start_time is None and (digit_1 != 0 or digit_2 != 0):
        st.session_state.start_time = time.time() # Start the timer when sliders are changed

    # Display current guess
    current_combination = f"{digit_1}{digit_2}"
    st.write(f"Current Guess: {current_combination}")

    # Track unique attempts
    st.session_state.attempts.add(current_combination) # Add the current guess to the set

    # Check if the guess is correct
    if digit_1 * 10 + digit_2 == secret_code:
        end_time = time.time() # End the timer
        time_taken = round(end_time - st.session_state.start_time, 2) # Calculate time taken in seconds
        st.success(f"Correct code: {secret_code}!")
        st.write(f"Time taken to unlock: {time_taken} seconds")
        st.write(f"You tried {len(st.session_state.attempts)} different combinations.")
        st.balloons() # Celebrate with balloons when they get it right
        del st.session_state.start_time # Reset the timer after success
        del st.session_state.attempts # Reset attempts after success
    else:
        st.write(f"You've tried {len(st.session_state.attempts)} different combinations so far. Keep going!")

# Run the lock simulation
lock_simulation()
