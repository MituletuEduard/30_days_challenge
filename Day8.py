"""
Day 8: Dompier Music
Tech companies track and publish the percentage of women in their workforce each year. Your mission: Analyze these trends and quantify each company's progress in “closing the gap.”

You're given annual percentages from real diversity reports published by some companies.

Complete the function that returns three metrics:

Net Change Per Year: Average yearly increase or decrease.
Net Change Per Year=
Years−1
Last Year−First Year
​

Trend: Compares the last 3-year average to the first 3-year average:
"improving": last 3-year average higher
"stagnating": averages equal
"declining": last 3-year average lower
Dips: Number of years where the percentage decreased compared to the previous year.
Python: Return three numbers. JavaScript: Return an array with three numbers.

Examples

Each test case is a FAANG company: Facebook (Meta), Amazon, Apple, Netflix, and Google.

Meta 🌀 (2014-2022)

Input: [31.0, 31.0, 33.0, 35.0, 36.0, 36.0, 36.2, 36.7, 37.1]
Output:
0.7625
"improving"
0
Net Change Per Year = (37.1−31.0) / 8 = 0.7625

Amazon 📦 (2014-2024)

Input: [42.0, 43.0, 42.0, 43.0, 44.0, 44.0, 44.6, 44.8, 44.7, 45.0, 45.8]
Output:
0.38
"improving"
2
Apple 🍎 (2014–2024)

Input: [30.0, 31.0, 32.0, 32.0, 33.0, 34.0, 34.0, 34.8, 35.0, 35.0, 35.3]
Output:
0.53
"improving"
0
This timeframe marks when all five companies began publishing official diversity reports. Every data point comes directly from published annual reports. No estimates.

Note: Meta and Google stopped reporting diversity data in early 2025 amid DEI rollbacks. Amazon, Apple, and Netflix still report as of 2026.
"""


def analyze(switches):
    years = len(switches)
    if years < 2:  # Not enough data to calculate net change per year
        return 0.0, "insufficient data", 0

    last_year = switches[-1]
    first_year = switches[0]

    net_change_per_year = round((last_year - first_year) / (years - 1), 4)

    n = min(3, years)
    last_n_years_avg = sum(switches[-n:]) / n
    first_n_years_avg = sum(switches[:n]) / n

    if last_n_years_avg > first_n_years_avg:
        trend = "improving"
    elif last_n_years_avg < first_n_years_avg:
        trend = "declining"
    else:
        trend = "stagnating"

    dips = sum(1 for i in range(1, years) if switches[i] < switches[i - 1])

    return net_change_per_year, trend, dips


print(analyze([31.0, 31.0, 33.0, 35.0, 36.0, 36.0, 36.2, 36.7, 37.1]))
print(analyze([42.0, 43.0, 42.0, 43.0, 44.0,
      44.0, 44.6, 44.8, 44.7, 45.0, 45.8]))
print(analyze([30.0, 31.0, 32.0, 32.0, 33.0,
      34.0, 34.0, 34.8, 35.0, 35.0, 35.3]))
    