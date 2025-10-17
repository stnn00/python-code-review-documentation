# README.md - Refactor and Review Python Script Project

## Project Overview
This project involved refactoring and documenting an existing Python script to improve readability, maintainability, and adherence to Pythonic practices. It also simulated a collaborative workflow through a self-review using GitHub pull requests and review features.

## Refactored Functionality
The refactored script includes functions for multiplying numbers and formatting words:
- `multiply_numbers(numbers)`: Takes a list of integers and returns a new list where even numbers are doubled and odd numbers are tripled.
- `format_words(words)`: Takes a list of strings and returns a single string where words longer than 5 letters are uppercase, shorter words (including exactly 5 letters) are lowercase, separated by spaces.
- `main()`: Demonstrates the script using example lists of numbers and words, calling the above functions and printing the results. Executed only when the script is run directly via the `if __name__ == "__main__"` block.

## Repository Files
- `undocumented_script.py` - Original starter Python script provided for the assignment.
- `refactored_script.py` - Refactored Python script with descriptive names, docstrings, and inline comments.
- `DECISIONS.md` - Documentation explaining design choices and refactoring rationale.
- `README.md` - Overview of the project, workflow, and instructions.
- `LICENSE` - MIT license included as instructed by the course tutorial.