"""
Today is March 4th... HAPPY HOOOLI!!!

Holi is the Festival of Colors. On this day, people in India, Nepal, and across the world come together to celebrate joy, unity, and new beginnings. People wear white and celebrate by throwing colorful powders. They also sing, dance, and eat traditional sweets!

You're given a 7x7 grid representing an area covered in Holi powders. Each cell contains an emoji representing one of these colors:

["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]

Some colors may be missing from the grid. Can you find which ones are missing? 🤫

Complete the function that finds and returns all the colors missing from the area (in that order).

होली की शुभकामनाएँ :)

Examples

Example 1

Input:

  [["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟥"],
  ["🟨", "🟩", "🟦", "🟪", "🟥", "🟧", "🟨"],
  ["🟦", "🟥", "🟧", "🟨", "🟩", "🟪", "🟦"],
  ["🟩", "🟦", "🟪", "🟥", "🟧", "🟨", "🟩"],
  ["🟧", "🟨", "🟩", "🟦", "🟪", "🟥", "🟧"],
  ["🟪", "🟧", "🟨", "🟩", "🟦", "🟥", "🟪"],
  ["🟥", "🟦", "🟩", "🟪", "🟨", "🟧", "🟦"]]
Output: "[🟫"]

The brown emoji is missing from the 7x7.

Example 2

Input:

[["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟧"],     
["🟨", "🟩", "🟦", "🟥", "🟨", "🟩", "🟦"],     
["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟨"],     
["🟩", "🟦", "🟥", "🟧", "🟨", "🟩", "🟦"],     
["🟨", "🟥", "🟧", "🟨", "🟩", "🟦", "🟥"],     
["🟦", "🟩", "🟨", "🟥", "🟧", "🟩", "🟦"],    
["🟥", "🟧", "🟨", "🟩", "🟦", "🟨", "🟥"]]
Output: ["🟪", "🟫"]

The purple emoji and the brown emoji are missing from the 7x7.
"""


def find_missing_colors(grid):

    colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]

    missing_colors = []

    for color in colors:
        count_color = False
        for row in grid:
            if color in row:
                count_color = True
                break
        if count_color == False:
            missing_colors.append(color)

    return missing_colors


print(find_missing_colors([["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟧"],
                           ["🟨", "🟩", "🟦", "🟥", "🟨", "🟩", "🟦"],
                           ["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟨"],
                           ["🟩", "🟦", "🟥", "🟧", "🟨", "🟩", "🟦"],
                           ["🟨", "🟥", "🟧", "🟨", "🟩", "🟦", "🟥"],
                           ["🟦", "🟩", "🟨", "🟥", "🟧", "🟩", "🟦"],
                           ["🟥", "🟧", "🟨", "🟩", "🟦", "🟨", "🟥"]]))

print(find_missing_colors([["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟥"],
                           ["🟨", "🟩", "🟦", "🟪", "🟥", "🟧", "🟨"],
                           ["🟦", "🟥", "🟧", "🟨", "🟩", "🟪", "🟦"],
                           ["🟩", "🟦", "🟪", "🟥", "🟧", "🟨", "🟩"],
                           ["🟧", "🟨", "🟩", "🟦", "🟪", "🟥", "🟧"],
                           ["🟪", "🟧", "🟨", "🟩", "🟦", "🟥", "🟪"],
                           ["🟥", "🟦", "🟩", "🟪", "🟨", "🟧", "🟦"]]))
