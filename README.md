
# 🔐 Python Password Strength Analyzer

A Python cybersecurity project that analyzes password strength using character variety, password length, and an estimated entropy score.

## Features

- Calculates estimated password entropy in bits
- Scores passwords out of 100 using basic rules
- Classifies passwords as Weak, Moderate, or Strong
- Detects selected common passwords
- Identifies repeated-character patterns
- Generates random password alternatives using Python's `secrets` module
- Hides password input in the terminal
- Includes automated unit tests

## Technologies

- Python 3
- math
- re
- string
- secrets
- getpass
- unittest

## Requirements

Python 3.10 or later. No third-party packages are required.

## Run the Analyzer

```bash
python password_checker.py
```

Enter a fictional test password when prompted.

## Run Automated Tests

```bash
python -m unittest -v
```

## How Entropy Is Estimated

The analyzer estimates entropy using:

entropy = password length × log2(character-set size)

The character-set size is estimated from the types of characters present in the password.

This is a simplified estimate and does not accurately measure every password's real-world resistance to guessing.

## Limitations

- The scoring system uses simple heuristic rules.
- Common-password detection uses a small built-in list.
- It does not check breached-password databases.
- It does not store or prevent reuse of previous passwords.

## Disclaimer

For educational purposes only. Never enter passwords used for real personal accounts.
