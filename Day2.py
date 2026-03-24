"""

Suppose we're building a word-guessing game with a secret word and a player's guess.

Given two strings, secret and guess, which are guaranteed to be of the same length (5 letters), determine how many characters are correct and in the exact same position.

Note: You don't need to know how Wordle works to do this challenge!

Examples

Example 1

Input: secret = "CODEX", guess = "COINS"
Output: 2
This is because the characters C and O are in the same position in both strings.

Example 2

Input: secret= "HELLO", guess = "WORLD"
Output: 1
The second L is in the same position in both strings.
"""


def wordle_guess(secret, guess):

    guessed_letters = 0

    for i in range(0, 5):
        if guess[i] == secret[i]:
            guessed_letters = guessed_letters + 1
    return guessed_letters


print(wordle_guess("CODEX", "COINS"))
print(wordle_guess("HELLO", "WORLD"))
