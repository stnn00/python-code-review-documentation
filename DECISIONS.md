# DECISIONS.md

#### An explanation of my thought process when making decisions in refactoring the original script.


## Screencast Overview


Video on YouTube (03:52): *[https://youtu.be/A6nQh4gIfUE](https://youtu.be/A6nQh4gIfUE)*

----------

In revising the original script, I focused on improving clarity and readability. I renamed vague function and variable names to be descriptive and PEP 8-compliant. For example, `do_math_stuff(list_of_nums)` became `multiply_numbers(numbers)` and `do_string_stuff(list_of_strings)` became `format_words(words)`. Variables like `num` and `processed_nums` were updated to `number`, and `multiplied_numbers`, and `list1` and `list2` were renamed to `numbers` and `fruits`. These changes make it easier to understand what each part of the code represents and ensure consistency throughout the script, which helps maintainability and reduces potential confusion for anyone reviewing or modifying the code.

I implemented doc-strings for every function in accordance with PEP 257, describing purpose, parameters, and return values, so that the code is self-explanatory and easier to understand without having to read through every line of implementation. Comments were added in-line where additional explanation was helpful for clarification, for instance in `multiply_numbers`, `format_words`, or clarifying the entry point defined by if `__name__ == "__main__"` block, without restating obvious code. Together, these documentation improvements and inline comments help orient the reader, clarify each function’s responsibilities, and communicate intentional design decisions to make the code self-explanatory, which is useful when collaborating or reviewing old code.

To further enhance efficiency and readability, I refactored loops into list comprehensions in both `multiply_numbers` and `format_words`. In `multiply_numbers`, using a list comprehension allows the conditional logic for doubling even numbers or tripling odd numbers to be expressed concisely in a single line. This reduces repetitive code (boilerplate), improves readability, and makes the transformation easy to understand at a glance. While very complex logic might be harder to read in a comprehension, for this project it provides a good balance between simplicity and clarity. These idiomatic Python practices, together with descriptive naming, thorough documentation, and an organized workflow through main, make the code maintainable, easy to follow, and reflective of deliberate and thoughtful design decisions.