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


def format_strings(strings):
    """
    Formats a list of strings:
    - Converts strings longer than 5 letters to uppercase format.
    - Converts shorter strings to lowercase format.
    - Returns a single string of all formatted words.

    Args:
        strings (list of str): The list containing strings to format.
    
    Returns:
        str: A single string containing all formatted words.
    """

    formatted_strings = ""  # Sets up string to store formatted words

    words = [word.upper() if len(word) > 5 else word.lower() for word in strings]  # Convert 5+ character words to uppercase, otherwise lowercase

    for word in words:
        formatted_strings += word + " "  # Add each formatted word with a space
    
    return formatted_strings.strip()  # Remove extra space at the end


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
    formatted_strings = format_strings(fruits)

    print("Multiplied Numbers:", multiplied_numbers)
    print("Formatted Strings:", formatted_strings)


if __name__ == "__main__":
    main()  # Execute main() only when this file is run directly
