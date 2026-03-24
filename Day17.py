"""
The river is colored using approximately 40 pounds of a secret, eco-friendly, vegetable-based powder that appears orange but turns brilliant green upon contact with water!

The dye starts at a few specific points... but the Windy City lives up to its name. 🌬️ Every hour, each green patch drifts one position to the right, spreading the color across the river.

Given the initial state of river and a number of hours, complete the function and return what the river looks like after the dye drifts downstream.

Sláinte! 🍻

Examples

Example 1

Input:
river = ['💧', '☘️', '💧', '💧', '💧', '☘️', '💧', '💧']
hours = 1
Output: ['💧', '☘️', '☘️', '💧', '💧', '☘️', '☘️', '💧']
After 1 hour, each ☘️ drifts one spot to the right.

Example 2

Input:
river = ['☘️', '💧', '💧', '💧', '💧', '☘️', '💧', '💧']
hours = 3
Output: ['☘️', '☘️', '☘️', '☘️', '💧', '☘️', '☘️', '☘️']
After 3 hours, each ☘️ has drifted 3 spots to the right.

💡 Fun fact: The Chicago River's dyed green every year since 1962, except 2020 due to COVID.
"""


def lucky_river(river, hours):
    # We start with a copy so we don't modify the original list
    result = river.copy()
    n = len(river)

    for i in range(n):
        # If we find a dye starting point
        if river[i] == '☘️':
            # The dye spreads from the current spot 'i'
            # up to 'hours' spots to the right
            for offset in range(1, hours + 1):
                new_position = i + offset
                if new_position < n:
                    result[new_position] = '☘️'
                else:
                    # If we've hit the end of the river, no need to keep drifting
                    break

    return result


print(lucky_river(['💧', '☘️', '💧', '💧', '💧', '☘️', '💧', '💧'], 1))
print(lucky_river(['☘️', '💧', '💧', '💧', '💧', '☘️', '💧', '💧'], 3))
print(lucky_river(['💧', '💧', '☘️', '💧', '💧', '☘️', '💧',
      '💧', '☘️', '💧', '💧', '☘️', '💧', '💧', '💧', '💧'], 4))
