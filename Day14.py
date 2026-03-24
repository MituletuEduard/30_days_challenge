"""
We'll keep today's Daily Challenge easy, so there's plenty of time to tackle the bonus task! 👀

Complete the function that calculates how much crust (circumference) each friend gets if the pie slices are shared evenly.

To solve this, you need to:

Google how to use π in Python or JavaScript (the focus here!).
Calculate the circumference of the pie.
Divide the slices evenly among friends.
Return the crust per friend, rounded to 2 decimal places.
The circumference formula is:

C=π×d
C = circumference
d = diameter of the pie
Examples

Example 1

Input:
diameter = 10
friends = 8
Output: 3.93
10 inches × π ÷ 8 friends ≈ 3.93 inches of crust per friend

Example 2

Input:
diameter = 12
friends = 5
Output: 7.54
12 inches × π ÷ 5 friends ≈ 7.54 inches of crust per friend

Bonus Task: Go grab or bake your favorite pie, and post it in your IG Story (tag us!) or the Monthly Challenge channel for a chance to win a Codédex Corduroy Cap. 

"""

import math


def cut_pie(diameter, friends):
    circumference = diameter * math.pi
    return round(circumference/friends, 2)


print(cut_pie(10, 8))
print(cut_pie(12, 5))
