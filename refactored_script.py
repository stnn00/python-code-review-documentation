def multiply_numbers(numbers):
    """
    Multiplies each integer in the list depending on whether it is even or odd:
    - Even numbers are doubled.
    - Odd numbers are tripled.

    Args:
        numbers (list of int): The list containing integers to process.

    Returns:
        list of int: A new list containing the multiplied numbers.
    """

    multiplied_numbers = [number * 2 if number % 2 == 0 else number * 3 for number in numbers]  # Apply conditions for multiplying even/odd numbers
    return multiplied_numbers


def format_words(words):
    """
    Formats a list of words according to their length:
    - Converts words longer than 5 letters to uppercase format.
    - Converts words shorter than 5 letters to lowercase format.
    - Words with exactly 5 letters are also converted to lowercase.
    - Returns a string of all words separated by spaces.

    Args:
        words (list of str): The list containing words to format.
    
    Returns:
        str: A single string containing all formatted words.
    """

    formatted_string = " ".join(
        word.upper() if len(word) > 5 else word.lower() for word in words
    )  # Convert words >5 letters to uppercase, otherwise lowercase
    return formatted_string


def main():
    """
    Runs the main workflow for processing numbers and words:
    - Creates a list of numbers and a list of fruits.
    - Multiplies numbers using `multiply_numbers()`.
    - Formats words using `format_words()`.
    - Prints the results of the multiplied numbers and formatted words.
    """

    numbers = [1, 2, 3, 4, 5, 6, 7]  # List of numbers to multiply
    fruits = ["apple", "banana", "kiwi", "grapefruit", "cherry"]  # List of words to format

    multiplied_numbers = multiply_numbers(numbers)
    formatted_fruits = format_words(fruits)

    print("Multiplied Numbers:", multiplied_numbers)
    print("Formatted Words:", formatted_fruits)


if __name__ == "__main__":
    main()  # Execute main() only when this file is run directly
