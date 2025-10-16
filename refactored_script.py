def process_numbers(numbers):
    processed_numbers = []
    for number in numbers:
        if number % 2 == 0:
            processed_numbers.append(number * 2)
        else:
            processed_numbers.append(number * 3)
    return processed_numbers


def do_string_stuff(list_of_strings):
    x = ""
    for s in list_of_strings:
        if len(s) > 5:
            x += s.upper() + " "
        else:
            x += s.lower() + " "
    return x.strip()


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(list1)
    processed_strings = do_string_stuff(list2)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
