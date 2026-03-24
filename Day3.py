"""
You are given a timestamp in the format "HH:MM" (24-hour time). Your task is to predict the next 3 times the blood moon will occur.

Examples

Example 1

Input: "01:00"
Output: ["03:48", "06:36", "09:24"]
Each of these are 2 hours and 48 minutes apart.

Example 2

Input: "22:30"
Output: ["01:18", "04:06", "06:54"]
Each of these are 2 hours and 48 minutes apart.
"""


def blood_moon(time):
    # Write code below 💖
    hours = int(time[0:2])
    minutes = int(time[3:5])
    current_total_minutes = hours * 60 + minutes
    moon_min = 168

    predictions = []

    for _ in range(3):
        current_total_minutes += moon_min
        current_total_minutes = current_total_minutes % (24 * 60)
        new_hours = current_total_minutes // 60
        new_minutes = current_total_minutes % 60

        predictions.append(f"{new_hours:02d}:{new_minutes:02d}")
    return predictions


print(blood_moon("22:30"))
