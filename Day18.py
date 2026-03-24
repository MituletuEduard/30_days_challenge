"""
Your task is simple: Pick the voucher that gives you the most value for your time. Specifically, you want the highest dollars per hour waited (voucher amount-to-delay ratio). 🎫

dollars per hour waited= 
hours delayed
voucher amount
​
 
But you also have a maximum number hours you're willing to wait. Any option longer is out.

Given:

vouchers: a list of voucher amounts (in dollars)
delays: a list of corresponding delay times (in hours)
max_wait: the maximum hours you're willing to wait
Complete the function and return the index of the best option.

If two options tie, return the first one.
If none qualify, return -1.
Examples

Example 1

Input:
vouchers = [50, 120, 20]
delays = [2, 4, 1]
max_wait = 3
Output: 0
Option 0 is $25/hr. ✅ Option 1 has a 4-hour wait (over limit). Option 2 is $20/hr.

Example 2

Input:
vouchers = [300, 400, 1000]
delays = [5, 6, 10]
max_wait = 4
Output: -1
Every option exceeds the max wait. No deal is worth it. 😤
"""


def pick_voucher(vouchers, delays, max_wait):
    # Write code below
    best_index = -1
    best_value = -1.0

    for i in range(len(vouchers)):
        if delays[i] <= max_wait:
            value = vouchers[i] / delays[i]
            if value > best_value:
                best_value = value
                best_index = i
    if best_index == -1:
        return -1
    else:
        return best_index


print(pick_voucher([50, 120, 20], [2, 4, 1], 3))
print(pick_voucher([300, 400, 1000], [5, 6, 10], 4))
print(pick_voucher([0, 0], [1, 2], 2))
