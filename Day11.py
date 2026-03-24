"""
Your task: Find the minimum number of components whose sum is exactly 42.

If it’s impossible to reach exactly 42, return -1.

Choose wisely. The wrong combination might tear a hole in the space-time continuum!

Examples

Example 1

Input: [10, 20, 5, 15, 7]
Output: 3
One combination is 20 + 15 + 7 = 42. The minimum number of components needed is 3.

Example 2

Input: [1, 2, 3, 4, 5, 6]
Output: -1
No combination sums to exactly 42.

Example 3

Input: [42, 1, 1, 1]
Output: 1
"""


def minimum_components(components):
    # Write code below 💖
    components.sort(reverse=True)
    total = 0
    count = 0
    # Check combinations starting from the largest component
    for component in components:
        total += component
        count += 1
        if total == 42:
            return count
        elif total > 42:
            total -= component
            count -= 1

    return -1


print(minimum_components([10, 20, 5, 15, 7]))
print(minimum_components([1, 2, 3, 4, 5, 6]))
print(minimum_components([41, 1, 1, 42]))
