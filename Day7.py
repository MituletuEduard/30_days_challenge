""""
At Codédex, our small but mighty team has been grinding on the Daily Challenge feature. We're tracking how much sleep debt everyone racks up before launch.

You’re given the hours each team member planned to sleep vs. actually slept over a week. 🛌💤

Sleep Debt=max(0, Planned Sleep−Actual Sleep)
Planned Sleep: Hours someone intended to sleep
Actual Sleep: Hours they actually got
max(0, x): Returns the larger of 0 or x.
Complete the function and return:

The total sleep debt for the week (including +1 Daylight Savings hour)
The longest streak of consecutive days with sleep debt
Python: Return two numbers. JavaScript: Return an array with two numbers.

⋆｡ ˚｡⋆｡ Sweet dreams ⋆｡˚｡⋆｡

Examples

Example 1: Sonny

Input:
planned = [7.5, 8, 7.5, 8, 8.5, 8, 7.5]
actual = [5, 12, 6, 6, 9, 8, 6.5]
Output:
8.0
2
Sleep debt: 2.5 + 0 + 1.5 + 2 + 0 + 0 + 1 = 7.0 hours (+1 Daylight Savings hour)
Longest streak: 2 days (day 3 and day 4)

Example 2: Asiqur

Input:
planned = [6, 6, 6, 6, 6, 8, 8]
actual = [5, 7, 2.5, 5, 5.5, 6, 4]
Output:
13.0
5
Sleep debt: 1 + 0 + 3.5 + 1 + 0.5 + 2 + 4 = 12.0 (+1 Daylight Savings hour)
Longest streak: 5 days (day 3 through day 7)

Bonus: Calculate your own sleep debt and post it in the Monthly Challenge channel. 🥱
"""


def calculate_sleep_debt(planned, actual):
    # Write code below 💖
    sleep_debt = 0
    longest_streak = 0
    current_streak = 0
    for p, a in zip(planned, actual):
        daily_debt = max(0, p - a)
        print(daily_debt)
        sleep_debt += daily_debt
        if daily_debt > 0:
            current_streak += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
        else:
            current_streak = 0
    sleep_debt += 1  # Add 1 hour for Daylight Savings
    return sleep_debt, longest_streak


print(calculate_sleep_debt(
    [7.5, 8, 7.5, 8, 8.5, 8, 7.5], [5, 12, 6, 6, 9, 8, 6.5]))
