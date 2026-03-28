"""
A dangerous virus is spreading across a city. So it goes... 🦠

Each day, infected people pass the virus to nearby healthy people. Your goal is to determine how many days it takes to infect everyone... or if it’s impossible.

Given a grid representing a city:

' ' = empty space
'👤' = healthy person
'🧟' = infected person
Each day, any infected person '🧟' infects adjacent healthy folks '👤' (up, down, left, right).

Complete the function and return:

The minimum number of days needed to infect all people.
OR -1 if some people can never be infected.
Examples

Example 1

Input:
[
  ['👤', ' ', '🧟'],
  ['🧟', '👤', ' '],
  [' ', '👤', '👤']
]
Output: 3
In three days, everyone is infected. We're cooked! 🧟 🧟‍♀️ 🧟‍♂️

Example 2

Input:
[
  ['👤', ' ', ' ', '🧟'],
  [' ', '👤', '👤', ' '],
  [' ', '👤', ' ', '👤'],
  ['👤', '👤', '👤', ' ']
]
Output: -1
The one in the top right doesn't infect anyone. We can contain this thing! 💉
"""


from collections import deque


def days_to_infect(city):
    # If the city is empty, no days are needed
    if not city or not city[0]:
        return 0

    rows, cols = len(city), len(city[0])
    queue = deque()
    healthy_count = 0

    # 1. Initialize: Find all starting infected positions and count healthy people
    for r in range(rows):
        for c in range(cols):
            if city[r][c] == '🧟':
                queue.append((r, c))
            elif city[r][c] == '👤':
                healthy_count += 1

    # If there are no healthy people to infect, we're already done
    if healthy_count == 0:
        return 0

    days = 0
    # Directions for movement: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 2. Spread the infection day by day using BFS
    while queue and healthy_count > 0:
        days += 1

        # Process all people infected up to the current day
        # This loop ensures we only move one step (one day) at a time
        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check if the neighbor is within bounds and healthy
                if 0 <= nr < rows and 0 <= nc < cols and city[nr][nc] == '👤':
                    # Infect the person and add them to the queue for the next day
                    city[nr][nc] = '🧟'
                    healthy_count -= 1
                    queue.append((nr, nc))

    # 3. Final check: If healthy people remain, they were unreachable
    return days if healthy_count == 0 else -1


# --- Tests ---
print(days_to_infect([
    ['👤', ' ', '🧟'],
    ['🧟', '👤', ' '],
    [' ', '👤', '👤']
]))  # Output: 3

print(days_to_infect([
    ['👤', ' ', ' ', '🧟'],
    [' ', '👤', '👤', ' '],
    [' ', '👤', ' ', '👤'],
    ['👤', '👤', '👤', ' ']
]))  # Output: -1
