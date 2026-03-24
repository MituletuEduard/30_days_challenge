"""
Each hour, a pipe loses a fixed percentage of its current volume using this formula:

new volume=current volume×(1− 
100
leak
​
 )
But pipes also have a minimum pressure threshold: once the volume drops below this level, the pipe has failed and water stops flowing entirely. 💥

Given:

A starting volume
A leak percentage per hour
A number of hours
A minimum pressure threshold
Complete the function and return the volume of water remaining after all hours have passed, rounded to 2 decimal places.

If the pipe fails before time is up, return -1. The pipe is done. 💧

Examples

Example 1

Input:
volume = 1000
leak = 5
hours = 3
threshold = 100
Output: 857.38
Applying the formula each hour: 1000 → 950 → 902.50 → 857.38. Never hits the threshold!

Example 2

Input:
volume = 200
leak = 30
hours = 6
threshold = 100
Output: -1
A 30% leak compounds fast; the volume crashes below 100 within 6 hours. Pipe failed! 💥
"""


def leaky_pipe(volume, leak, hours, threshold):
    for _ in range(hours):
        volume *= (1 - leak / 100)
        if volume < threshold:
            return -1
    return round(volume, 2)
