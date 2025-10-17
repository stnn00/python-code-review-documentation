# README.md - Refactor and Review Python Script Project

## Project Overview
This project involved refactoring and documenting an existing Python script to improve readability, maintainability, and adherence to Pythonic practices. It also simulated a collaborative workflow through a self-review using GitHub pull requests and review features.

## Screencast Overview

Video on YouTube (03:52): *[https://youtu.be/A6nQh4gIfUE](https://youtu.be/A6nQh4gIfUE)*

## Refactored Functionality
The refactored script includes functions for multiplying numbers and formatting words:
- `multiply_numbers(numbers)`: Takes a list of integers and returns a new list where even numbers are doubled and odd numbers are tripled.
- `format_words(words)`: Takes a list of strings and returns a single string where words longer than 5 letters are uppercase, shorter words (including exactly 5 letters) are lowercase, separated by spaces.
- `main()`: Demonstrates the script using example lists of numbers and words, calling the above functions and printing the results. Executed only when the script is run directly via the `if __name__ == "__main__"` block.

## Repository Files
- `undocumented_script.py` - Original starter Python script provided for the assignment.
- `refactored_script.py` - Refactored Python script with descriptive names, doc-strings, and inline comments.
- `DECISIONS.md` - Documentation explaining design choices and refactoring rationale.
- `README.md` - Overview of the project, workflow, and instructions.
- `LICENSE` - MIT license included as instructed by the course tutorial.

## Installation & Usage

1. **Install Python 3**  

    - Ensure [Python 3](https://www.python.org/downloads/) is installed on your system.

2. **Clone the Repository**  

    - Open a terminal (Git Bash, Terminal, etc.)  
    - Clone the repository:

    ```bash
    git clone https://github.com/stnn00/python-code-review-documentation.git
    ```

    - Move into the repository directory:

    ```bash
    cd <repository-folder>
    ```

3. **Run the Main Program**

    1. Once you're inside the repository directory, run the refactored script:

    ```bash
    python refactored_script.py
    ```

    2. Expected output:
        - A list of numbers where even numbers are doubled and odd numbers are tripled.
        - A formatted string of words where words longer than 5 letters are uppercase, and shorter or exactly 5-letter words are lowercase.

    3. The script demonstrates functionality through the `main()` function, which calls `multiply_numbers()` and `format_words()` using example lists of numbers and words. It is executed only when the script is run directly (via the `if __name__ == "__main__"` block).
