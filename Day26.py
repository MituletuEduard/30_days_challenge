"""
And boy, did I bomb it. I still got the job, but this problem has stuck with me ever since.

Here's today's Daily Challenge:

Given a nested list/array (one that can contain numbers or other lists/arrays), sometimes deeply nested, your task is to flatten it into a "single-level" list/array.

Complete the function that returns a new list/array with all values flattened.

Give it a try and see if you can do what I struggled (ask Lumi for help!).

Examples

Example 1

Input: [1, [2, 3], 4, 5]
Output: [1, 2, 3, 4, 5]
The nested [2, 3] is flattened into the main list/array.

Example 2

Input: [1, 2, [3, [4, 5]], 6, 7]
Output: [1, 2, 3, 4, 5, 6, 7]
Multiple levels of nesting. Everything gets flattened.
"""


def flatten(list1):
    result = []
    for item in list1:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# --- Tests ---
print(flatten([1, [2, 3], 4, 5]))  # Output: [1, 2, 3, 4, 5]
print(flatten([1, 2, [3, [4, 5]], 6, 7]))  # Output: [1, 2, 3, 4, 5, 6, 7]
