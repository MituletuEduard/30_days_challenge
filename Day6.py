"""
Last week at the 2026 Winter Olympics, Alysa Liu became an international sensation, winning two gold medals and ending a 24-year Olympic gold drought for the U.S. in women’s figure skating. Her dazzling free skate earned her top scores, and her presence lit up the rink.

alysa liu

But how does figure skating scoring actually work? It's pretty complex!

There are three parts: Technical Element Score, Program Component Score, and Deductions.

For this Daily Challenge, let's focus on the first one...

🎯 Technical Element Score (TES)

Each skating element (jump, spin, or step sequence) has a base value.
Nine judges assign a Grade of Execution (GOE) for each element (-5 to 5).
To reduce bias, the highest and lowest GOE are dropped.
The remaining 7 are averaged.
The element score is calculated as:

Element Score=Base Value+(Average GOE×0.1×Base Value)
The TES is the sum of all element scores.

Given these rules, complete the function to calculate the TES (round it to one decimal place).

Examples

Input: elements
elements = [
  ("Triple Flip",            9.7,  [3, 2, 3, 3, 2, 4, 3, 2, 3]),
  ("Triple Lutz+Toe Combo", 12.5,  [4, 5, 4, 5, 5, 4, 4, 3, 4]),
  ("Triple Salchow",         7.0,  [2, 3, 2, 2, 3, 2, 2, 3, 2]),
  ("Triple Loop",            6.0,  [3, 3, 2, 4, 3, 3, 2, 3, 2]),
  ("Step Sequence",          3.3,  [4, 4, 4, 4, 3, 3, 4, 3, 4])
]
Output: 50.9
For JavaScript, change all the parentheses to square brackets: ( to [.

The Triple Flip score is calculated as 9.7 + (2.5714 × 0.1 × 9.7) ≈ 12.194

Adding up all element scores: 12.194 + 17.86 + 8.60 + 7.63 + 4.48 ≈ 50.9

P.S. Post an Alysa Liu GIF in the Monthly Challenge channel when you're done! ❄️
"""


def calculate_score(elements):
    tes_score = 0  # Initialize the total TES score to 0
    # Loop through each element and calculate its score
    for element in elements:
        base_value = element[1]  # Get the base value for the element
        goes = element[2]  # Get the GOE scores for the element
        sorted_goes = sorted(goes)  # Sort the GOE scores
        # Remove the highest and lowest GOE scores
        goe_value = sorted_goes[1:-1]
        # Calculate the average GOE
        avg_goe = (sum(goe_value)) / len(goe_value)
        # Calculate the element score
        element_score = base_value + (avg_goe * 0.1 * base_value)
        tes_score += element_score  # Add the element score to the total TES score

    # Round the total TES score to one decimal place and return it
    return round(tes_score, 1)


elements = [
    ("Triple Flip",            9.7,  [3, 2, 3, 3, 2, 4, 3, 2, 3]),
    ("Triple Lutz+Toe Combo", 12.5,  [4, 5, 4, 5, 5, 4, 4, 3, 4]),
    ("Triple Salchow",         7.0,  [2, 3, 2, 2, 3, 2, 2, 3, 2]),
    ("Triple Loop",            6.0,  [3, 3, 2, 4, 3, 3, 2, 3, 2]),
    ("Step Sequence",          3.3,  [4, 4, 4, 4, 3, 3, 4, 3, 4])
]

print(calculate_score(elements))
