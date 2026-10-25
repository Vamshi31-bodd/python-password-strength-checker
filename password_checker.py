
import math
import re
import string
import secrets
import getpass


COMMON_PASSWORDS = {
    "123456", "password", "123456789", "12345678",
    "12345", "qwerty", "abc123", "password1",
    "admin", "letmein", "welcome", "monkey",
}


def calculate_entropy(password: str) -> float:
    """Estimate password entropy using the tutorial's character-set method."""
    charset = 0

    if any(c.islower() for c in password):
        charset += 26

    if any(c.isupper() for c in password):
        charset += 26

    if any(c.isdigit() for c in password):
        charset += 10

    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)

    if any(c.isspace() for c in password):
        charset += 1

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)


def score_password(password: str) -> dict:
    """Calculate a rule-based password score and strength verdict."""
    score = 0
    length = len(password)
    entropy = calculate_entropy(password)

    # Rule-based scoring, following the tutorial screenshots
    if length >= 8:
        score += 20

    if length >= 12:
        score += 10

    if any(c.islower() for c in password):
        score += 10

    if any(c.isupper() for c in password):
        score += 10

    if any(c.isdigit() for c in password):
        score += 10

    if any(c in string.punctuation for c in password):
        score += 10

    if entropy > 50:
        score += 20

    # Penalize common passwords
    if password.casefold() in COMMON_PASSWORDS:
        score = min(score, 10)

    # Penalize predictable repeated characters
    if re.search(r"(.)\1{2,}", password):
        score = max(0, score - 10)

    score = min(score, 100)

    if password.casefold() in COMMON_PASSWORDS or length < 8:
        verdict = "Weak"
    elif score < 40:
        verdict = "Weak"
    elif score < 70:
        verdict = "Moderate"
    else:
        verdict = "Strong"

    return {
        "length": length,
        "entropy": entropy,
        "score": score,
        "verdict": verdict,
    }


def generate_password(length: int = 16) -> str:
    """Generate a random password containing several character types."""
    if length < 12:
        raise ValueError("Password length must be at least 12.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+?"

    characters = lowercase + uppercase + digits + symbols

    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    password_chars.extend(
        secrets.choice(characters) for _ in range(length - 4)
    )

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def main():
    print("=" * 40)
    print("     PASSWORD STRENGTH ANALYZER")
    print("=" * 40)

    password = getpass.getpass("Enter a test password: ")

    if not password:
        print("No password entered.")
        return

    result = score_password(password)

    print("\n--- Password Analysis ---")
    print(f"Length:  {result['length']}")
    print(f"Entropy: {result['entropy']} bits")
    print(f"Score:   {result['score']} / 100")
    print(f"Verdict: {result['verdict']}")

    if result["verdict"] != "Strong":
        print("\nSuggestions:")
        if result["length"] < 12:
            print("- Consider using a longer password.")
        if result["entropy"] <= 50:
            print("- Use a longer, less predictable password.")
        if password.casefold() in COMMON_PASSWORDS:
            print("- Avoid commonly used passwords.")

        print("\nSuggested alternative:")
        print(generate_password())

    print("\nThe program does not save your password.")


if __name__ == "__main__":
    main()
