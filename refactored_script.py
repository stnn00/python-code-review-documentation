def multiply_numbers(numbers):
    """
    Multiplies each integer in the list depending on whether it is even or odd:
    - Even numbers are doubled.
    - Odd numbers are tripled.

    Args:
        numbers (list of int): The list containing integers to process.

    Returns:
        list of int: A new list containing the processed numbers.
    """

    multiplied_numbers = [num * 2 if num % 2 == 0 else num * 3 for num in numbers]  # Apply activity requirements for even/odd numbers
    return multiplied_numbers


def format_words(words):
    """
    Formats a list of words:
    - Converts words longer than 5 letters to uppercase format.
    - Converts shorter words to lowercase format.
    - Returns a single string of all formatted words.

    Args:
        words (list of str): The list containing words to format.
    
    Returns:
        str: A single string containing all formatted words.
    """

    formatted_words = [word.upper() if len(word) > 5 else word.lower() for word in words]  # Convert 5+ character words to uppercase, otherwise lowercase

    formatted_string = ""
    for word in formatted_words:
        formatted_string += word + " "  # Add each formatted word with a space
    
    return formatted_string.strip()  # Remove extra space at the end


def main():
    """
    Runs the main workflow for processing numbers and strings:
    - Creates a list of numbers and a list of fruits.
    - Multiplies numbers using `multiply_numbers()`.
    - Formats strings using `format_strings()`.
    - Prints the results of the multiplied numbers and formatted strings.
    """

    numbers = [1, 2, 3, 4, 5, 6, 7]  # List of numbers to multiply
    fruits = ["apple", "banana", "kiwi", "grapefruit", "cherry"]  # List of words to format

    multiplied_numbers = multiply_numbers(numbers)
    formatted_words = format_words(fruits)

    print("Multiplied Numbers:", multiplied_numbers)
    print("Formatted Words:", formatted_words)


if __name__ == "__main__":
    main()  # Execute main() only when this file is run directly
