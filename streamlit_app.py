import streamlit as st
import qrcode
import io

# Function to simulate the 2-digit lock challenge without tracking attempts/time
def lock_simulation():
    st.title("2-Digit Lock Simulation")

    st.write("""
    Your goal is to find the correct combination to open the lock! 
    Adjust the sliders to find the code.
    """)

    secret_code = 27

    digit_1 = st.slider("Digit 1", 0, 9, 0)
    digit_2 = st.slider("Digit 2", 0, 9, 0)

    current_combination = digit_1 * 10 + digit_2
    st.write(f"Current Guess: {digit_1}{digit_2}")

    if current_combination == secret_code:
        st.success(f"Correct code: {secret_code}!")
        st.balloons()
    else:
        st.info("Try adjusting the digits to find the correct code.")

# Sidebar QR code section
st.sidebar.header("Scan This QR Code to View Menu Online")
qr_link = "https://your-app-url.com"  # Replace with your actual URL
qr = qrcode.make(qr_link)
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)
st.sidebar.image(buf, width=200, caption=qr_link)

# Run the lock simulation
lock_simulation()
