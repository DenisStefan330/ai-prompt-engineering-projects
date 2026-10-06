# ==========================================
# SECURE PASSWORD GENERATOR
# AI-Assisted Script developed for R&D Portfolio
# ==========================================

# Bring in the random tool from Python's library
import random

def generate_password():
    # Create strings containing all our possible characters
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    # Combine them all into one massive string of options
    all_characters = letters + numbers + symbols

    # Decide how long we want our password to be
    password_length = 12

    # Create an empty box to hold our final password
    secure_password = ""

    # Loop 12 times, picking one random character each time
    for step in range(password_length):
        # Pick a random character from our big string of options
        random_choice = random.choice(all_characters)
        
        # Add that random character to our password box
        secure_password = secure_password + random_choice

    return secure_password

# Execute the script
if __name__ == "__main__":
    print("Generating your highly secure password...")
    final_password = generate_password()
    print("Your highly secure password is:")
    print(final_password)
