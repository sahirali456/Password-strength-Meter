import re

def check_password_strength(password):
    score = 0
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        print("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        print("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        print("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        print("✅ Strong Password!")
        return True
    elif score == 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
        return False
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")
        return False

# User Input Loop
while True:
    password = input("Enter your password: ")
    if check_password_strength(password):
        break  # Exit loop if password is strong
    print("\n🔁 Try again with a stronger password!\n")
