# DECISIONS.md

#### An explanation of my thought process when making decisions in refactoring the original script.

----------

In revising the original script, I focused on improving both clarity and readability. I renamed vague function and variable names to be descriptive and PEP 8-compliant. For example, `do_math_stuff(list_of_nums)` became `process_numbers(numbers)` and `do_string_stuff(list_of_strings)` became `process_strings(strings)`. Variables like `x`, `s`, `num`, and `processed_nums` were updated to `words`, `string`, `number`, and `processed_numbers`, and `list1` and `list2` were renamed to `numbers` and `fruits`. These changes make it easier to understand what each part of the code represents and ensure consistency throughout the script, which helps maintainability and reduces potential confusion for anyone reviewing or modifying the code.