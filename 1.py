import streamlit as st
import re
import random
import string

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Function to generate a strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Streamlit UI
st.title("🔐 Password Strength Meter")

# User Input
password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)
        
        # Display Feedback
        for msg in feedback:
            st.warning(msg)
        
        # Display Strength Result
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.info("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions above.")
    else:
        st.error("⚠️ Please enter a password to check strength.")

# Password Generator Button
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.success(f"🔑 Suggested Strong Password: `{strong_password}`")
