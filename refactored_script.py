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

    processed_numbers = []

    for number in numbers:
        if number % 2 == 0:
            processed_numbers.append(number * 2)
        else:
            processed_numbers.append(number * 3)
            
    return processed_numbers


def process_strings(strings):
    x = ""
    for s in strings:
        if len(s) > 5:
            x += s.upper() + " "
        else:
            x += s.lower() + " "
    return x.strip()


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(list1)
    processed_strings = process_strings(list2)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
