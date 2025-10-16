def process_numbers(numbers):
    """
    Multiplies each integer in the list depending on whether it is even or odd:
    - Even numbers are doubled.
    - Odd numbers are tripled.

    Parameters:
        numbers (list of int): The list containing integers to process.

    Returns:
        list of int: A new list containing the processed numbers.
    """

    processed_numbers = [num * 2 if num % 2 == 0 else num * 3 for num in numbers]  # Apply activity requirements for even/odd numbers
    return processed_numbers


def process_strings(strings):
    """
    Processes a list of strings:
    - Converts strings longer than 5 letters to uppercase format.
    - Converts shorter strings to lowercase format.
    - Returns a single string of all processed words.

    Parameters:
        strings (list of str): The list containing strings to process.
    
    Returns:
        str: A single string containing all processed words.
    """

    processed_words = ""  # Sets up string to store processed words

    words = [word.upper() if len(word) > 5 else word.lower() for word in strings]  # Convert 5+ character words to uppercase, otherwise lowercase

    for word in words:
        processed_words += word + " "  # Add each processed word with a space
    
    return processed_words.strip()  # Remove extra space at the end


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(list1)
    processed_strings = process_strings(list2)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
