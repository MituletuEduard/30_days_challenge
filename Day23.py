"""
Day 23: Cuddly  Kittens 🐱
You're helping kittens line up in a cozy play area. They only stay calm if their energy levels are similar. Otherwise, the purring stops, and chaos ensues.

You're given:

A list/array kittens, where kittens[i] represents the energy level of the i-th kitten
A number limit, the biggest difference between any two kittens in a calm group
A group of kittens is calm and can purr together if:

max energy−min energy≤limit
Return the length of the longest group of consecutive kittens that can stay calm. 🐾🐾🐾

Bonus Task: Snap a pic of your cat with Codédex for a chance to win a Codédex Crewneck! 📸

Examples

Example 1

Input:
kittens = [1, 3, 6, 7, 9]
limit = 3
Output: 3
The longest valid group is [6, 7, 9] because max - min = 9 - 6 = 3.

Example 2

Input:
kittens = [2, 3, 4, 5]
limit = 10
Output: 4
All kittens can stay together since max - min = 5 - 2 = 3 ≤ 10.
"""


def cuddly_kittens(kittens, limit):
    left = 0
    best = 0

    for right in range(len(kittens)):
        # Shrink window from the left until it's calm again
        while max(kittens[left:right+1]) - min(kittens[left:right+1]) > limit:
            left += 1
        best = max(best, right - left + 1)

    return best


# --- Tests ---
print(cuddly_kittens([1, 3, 9, 1, 7, 8, 9], 3))
print(cuddly_kittens([2, 3, 4, 5], 10))
