"""
Given a string, complete the function that checks whether it's a palindrome.

Python: Return True if it is, False if it isn't.
JavaScript: Return true if it is, false if it isn't.
Ignore spaces and capitalization.

Assume the string only contains letters (a-Z) and numbers (0-9). No punctuation.

Examples

Example 1

Input: "racecar"
Output: True
Example 2

Input: "Was it a car or a cat I saw"
Output: True
Example 3

Input: "11 11" (make a wish!)
Output: True
Example 4

Input: "12345"
Output: False
Remember that it's lowercase true/false for JavaScript.
"""


def check_palindrome(sequence):
    # Write code below 💖
    cleaned_sequence = ''.join(sequence.split()).lower()
    return cleaned_sequence == cleaned_sequence[::-1]


print(check_palindrome("11 11"))
print(check_palindrome("Was it a car or a cat I saw"))
