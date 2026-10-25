
# 🔐 Python Password Strength Checker

A beginner-friendly cybersecurity project built with Python to evaluate password strength and generate stronger password suggestions.

## Features

- Checks password length
- Detects lowercase and uppercase letters
- Checks for numbers and special symbols
- Identifies selected common passwords
- Detects repeated-character patterns
- Provides password improvement suggestions
- Generates random password alternatives using Python's `secrets` module
- Hides password input in the terminal
- Does not save passwords to a file or database

## Technologies Used

- Python 3
- Regular expressions (`re`)
- `string` module
- `secrets` module
- `getpass` module

## Requirements

- Python 3.10 or later
- No external packages required

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run:

   ```bash
   python password_checker.py
   ```

4. Enter a fictional test password when prompted.

## Example

For a test password such as `hello123`, the program may report a moderate strength rating and suggest improvements.

## Learning Objectives

- Understand basic password security concepts
- Practice Python functions and conditional statements
- Learn regular expressions
- Explore secure random password generation
- Practice Git and GitHub

## Limitations

This project uses simple heuristic rules. Its score is not a guarantee of password security and does not check breached-password databases or accurately estimate guessing difficulty.

## Future Improvements

- Add automated unit tests
- Improve password strength estimation
- Add password history and reuse prevention
- Create a graphical user interface

## Disclaimer

For educational purposes only. Never enter passwords that you currently use for personal accounts.

---

Created as a cybersecurity learning project.

