"""
Inspired by the real Japanese forecasting method, 積算温度, which tracks heat buildup after winter dormancy, blossoms open on the first day the 5-day rolling average temperature crosses 15°C. That means for each day, you look at it and the previous 4 days, compute their average, and check whether it surpasses 15.

Your task: Given a list of daily temperatures, complete the function so that it returns the day number (1-indexed) when the blossoms first bloom, or -1 if they never do.

🌸🍃🌸✨🌸🍃🌸✨🌸🍃🌸✨

Examples

Example 1

Input: temps = [10, 11, 13, 14, 16, 17, 18]
Output: 7
The temperatures steadily climb – by day 7, the 5-day rolling average finally crosses 15°C.

Example 2

Input: temps = [12, 14, 15, 16, 17, 11, 13]
Output: -1
The 5-day average never quite clears 15°C; the blossoms stay closed this year. 🥀
"""


def cherry_blossoms(temps):
    for i in range(4, len(temps)):
        window = temps[i-4:i+1]
        if sum(window) / 5 > 15:
            return i + 1  # 1-indexed
    return -1


# --- Tests ---
print(cherry_blossoms([10, 11, 13, 14, 16, 17, 18]))
print(cherry_blossoms([12, 14, 15, 16, 17, 11, 13]))
