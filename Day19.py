"""
The teams are split into four regions: East, West, South, and Midwest, each with 16 seeds, where #1 is the strongest, #16 is the weakest. Higher seeds play lower seeds (#1 vs #16, #2 vs #15, ...). The winner of each region goes to the "Final Four" to compete for the championship.

But what happens when a lower-seeded team beats a stronger one? That's called an upset.

An upset occurs when a lower-seeded team (larger number) defeats a higher-seeded team (smaller number). The bigger the gap, the more shocking the result! 🤯

We can calculate the probability of an upset using the two teams' seed numbers:

upset probability= 
(higher seed+lower seed)
higher seed
​
 
A #1 vs #16 gives the underdog only a 6% chance. 🤏

Given a list/array of matchups as ["Team A", seedA, "Team B", seedB] (Team A always stronger), return a list of each game's upset probability, rounded to 2 decimal places.

Examples

Example 1

Input:
matchups = [
  ["Duke", 1, "Siena", 16],
  ["Ohio State", 8, "TCU", 9]
]
Output: [0.06, 0.47]
Duke vs Siena gives the underdog just a 6% chance. Ohio State vs TCU is almost a coin flip!

Example 2

Input:
matchups = [
  ["Michigan", 1, "Lehigh", 16],
  ["Nebraska", 4, "Troy", 13],
  ["Houston", 2, "Akron", 15]
]
Output: [0.06, 0.24, 0.12]
Nebraska vs Troy gives Troy a 24% upset chance. Not guaranteed, but not impossible either.

💡 Fun Fact: Lower-seeded teams pulling off huge upsets are called “Cinderella teams.” In 2018, UMBC (#16) beat Virginia (#1). The first 16-over-1 upset in history (since 1939).
"""


def upset_probability(matchups):
    probabilities = []
    for team in matchups:
        seedA = team[1]
        seedB = team[3]
        probability = round(seedA / (seedA + seedB), 2)
        probabilities.append(probability)
    return probabilities

# --- Tests ---


matchups = [
    ["Duke", 1, "Siena", 16],
    ["Ohio State", 8, "TCU", 9]
]
print(upset_probability(matchups))
# Output: [0.06, 0.47]
matchups = [
    ["Michigan", 1, "Lehigh", 16],
    ["Nebraska", 4, "Troy", 13],
    ["Houston", 2, "Akron", 15]
]
print(upset_probability(matchups))
# Output: [0.06, 0.24, 0.12]
