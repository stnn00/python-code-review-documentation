# DECISIONS.md

#### An explanation of my thought process when making decisions in refactoring the original script.

----------

In revising the original script, I focused on improving both clarity and readability. I renamed vague function and variable names to be descriptive and PEP 8-compliant. For example, `do_math_stuff(list_of_nums)` became `process_numbers(numbers)` and `do_string_stuff(list_of_strings)` became `process_strings(strings)`. Variables like `x`, `s`, `num`, and `processed_nums` were updated to `words`, `string`, `number`, and `processed_numbers`, and `list1` and `list2` were renamed to `numbers` and `fruits`. These changes make it easier to understand what each part of the code represents and ensure consistency throughout the script, which helps maintainability and reduces potential confusion for anyone reviewing or modifying the code.

I implemented docstrings for every function in accordance with PEP 257, describing purpose, parameters, and return values, so that the code is self-explanatory and easier to understand without having to read through every line of implementation. Comments were added in-line where additional explanation was helpful for clarification, for instance in processing numbers and strings or clarifying the entry point defined by if `__name__ == "__main__"` block, without restating the code. Together, these documentation improvements and inline comments help orient the reader, clarify each function’s responsibilities, and communicate intentional design decisions beyond what the code alone conveys.
