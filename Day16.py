"""
Oscars 2026

After the ceremony, we now have two things:

A list of the actual winners:
Best Picture: One Battle After Another
Best Actor: Michael B. Jordan
Best Actress: Jessie Buckley
Best Director: Paul Thomas Anderson
Each friend’s predicted winners
Complete the function that calculates each friend’s prediction accuracy:

accuracy= 
total predictions
correct predictions
​
 
Which friend has the highest accuracy? Return their name. If there's a tie, return "Tie".

Examples

Example 1

Input:
predictions = [
  ["@sonny", "One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Ryan Cooger"],
  ["@brit896", "Marty Supreme", "Timothée Chalamet", "Jessie Buckley", "Josh Safdie"],
  ["@tylerwhit", "Sinners", "Michael B. Jordan", "Rose Byrne", "Paul Thomas Anderson"]
]
Output: "@sonny"
@sonny got 3/4, @brit896 got 1/4, and @tylerwhit got 2/4.

Example 2

Input:
predictions = [
  ["Kalshi", "One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"],
  ["Polymarket", "One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"]
]
Output: "Tie"
Both have a perfect score, so it's a tie.

Example 3

Input:
predictions = [
  ["Rotten Tomatoes", "The Secret Agent", "Wagner Moura", "Renate Reinsve", "Kleber Mendonça Filho"],
  ["IMDb", "One Battle After Another", "Timothée Chalamet", "Jessie Buckley", "Chloé Zhao"]
]
Output: "IMDb"
Rotten Tomatoes got 0/4 and IMDb got 2/4.
"""


def oscar_pool(predictions):
    actual_winners = ["One Battle After Another",
                      "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"]
    accuracies = {}
    for prediction in predictions:
        name = prediction[0]
        # We compare the predicted winners (starting from index 1) with the actual winners and count how many predictions are correct
        correct_predictions = sum(
            1 for i in range(1, 5) if prediction[i] == actual_winners[i-1])
        total_predictions = 4
        accuracy = correct_predictions / total_predictions
        accuracies[name] = accuracy

    max_accuracy = max(accuracies.values())

    # Find all friends with the maximum accuracy
    winners = [name for name, acc in accuracies.items() if acc == max_accuracy]
    if len(winners) == 1:
        return winners[0]
    else:
        return "Tie"


predictions = [
    ["@sonny", "One Battle After Another",
        "Michael B. Jordan", "Jessie Buckley", "Ryan Cooger"],
    ["@brit896", "Marty Supreme", "Timothée Chalamet",
        "Jessie Buckley", "Josh Safdie"],
    ["@tylerwhit", "Sinners", "Michael B. Jordan",
     "Rose Byrne", "Paul Thomas Anderson"]
]
print(oscar_pool(predictions))
