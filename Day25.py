"""
As the season kicks off, one thing fans obsess over is winning streaks – how many games in a row can your team win? Streaks are the heartbeat of a baseball season.

But baseball has a unique wrinkle: rainouts. 🌧️

A rainout ("R") means the game was never played. It doesn't count as a win/loss, and it does not break a streak. A 5-game winning streak that gets rained out is still on a streak!

Given a list/array of game results, return the longest winning streak of the season.

Each character is one of:

"W": Win
"L": Loss
"R": Rainout (doesn't break a streak)
Let the games begin! ⚾️ 🏟️ 🧢 🌭 ✨

Examples

Example 1

Input: ["W", "W", "L", "W", "W", "W", "L", "W", "W"]
Output: 3
The streak ["W", "W", "W"] in the middle is the longest. No rainouts to worry about here.

Example 2

Input: ["W", "W", "R", "W", "W", "L", "W"]
Output: 4
The rainout doesn't break the streak. ["W", "W", "R", "W", "W"] is 4 consecutive wins! 🌧️

Example 3

Input: ["R", "R", "W", "R", "R", "W", "W", "R", "R", "W", "W", "W", "R"]
Output: 6
Rainouts everywhere! This counts as 6 consecutive wins. 🌧️
"""


def streak_counter(games):
    max_streak = 0
    current_streak = 0

    for result in games:
        if result == 'W':
            current_streak += 1
        elif result == 'L':
            max_streak = max(max_streak, current_streak)
            current_streak = 0

    return max(max_streak, current_streak)


# --- Tests ---
# Output: 3
print(streak_counter(["W", "W", "L", "W", "W", "W", "L", "W", "W"]))
print(streak_counter(["W", "W", "R", "W", "W", "L", "W"]))  # Output: 4
print(streak_counter(["R", "R", "W", "R", "R", "W",
      "W", "R", "R", "W", "W", "W", "R"]))  # Output: 6
