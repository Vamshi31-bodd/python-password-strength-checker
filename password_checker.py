
import re
import string
import secrets
import getpass


COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "iloveyou",
}


def check_password(password):
    score = 0
    feedback = []

    print("\nAnalyzing password...")

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Consider using 12 or more characters.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    # Check numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers (0-9).")

    # Check special symbols
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Consider adding a special symbol.")

    # Check common passwords
    if password.casefold() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a commonly used password.")

    # Check three or more repeated characters in a row
    if re.search(r"(.)\1{2,}", password):
        score = max(0, score - 1)
        feedback.append(
            "Avoid repeating the same character three or more times."
        )

    # Warn about passwords using only letters or only numbers
    if password.isalpha() or password.isdigit():
        feedback.append("Avoid using only letters or only numbers.")

    # Determine password strength
    if password.casefold() in COMMON_PASSWORDS:
        strength = "Very Weak"
    elif len(password) < 8 or score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score, feedback


def generate_password(length=16):
    """Generate a random password using Python's secrets module."""

    if length < 12:
        raise ValueError("Password length must be at least 12.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+?"

    # Include at least one character from every category
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    all_chars = lowercase + uppercase + digits + symbols

    # Fill the remaining length
    password_chars.extend(
        secrets.choice(all_chars) for _ in range(length - 4)
    )

    # Securely shuffle the characters
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = getpass.getpass("Enter a test password: ")

    if not password:
        print("No password entered.")
        return

    strength, score, feedback = check_password(password)

    print(f"\nPassword strength: {strength}")
    print(f"Basic rule score: {score}/6")

    if feedback:
        print("\nSuggestions:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("\nNo basic improvements suggested.")

    if strength in ("Weak", "Very Weak", "Moderate"):
        print("\nSuggested stronger alternative:")
        print(generate_password())

    print("\nPrivacy notice:")
    print("This program does not save passwords to a file or database.")
    print("Use a password manager to store generated passwords safely.")


if __name__ == "__main__":
    main()
