"""
At that time, tweets were limited to 140 characters, inspired by the 160-character SMS standard (leaving a little wiggle room for a username).

Over time, Twitter has added different counting rules for things like username mentions, links, and emojis so they would all take up a more consistent amount of space.

For this challenge, we’ll use a simplified version of that idea:

👤 Usernames (any words starting with @) always count as 20 characters
🔗 URLs (any words starting with http:// or https://) always count as 23 characters
😀 Emojis always count as 2 characters (though back in 2006, emojis were barely a thing, so don't worry about testing them!)
🔤 All other characters, including spaces and punctuation, will count normally.
Given a tweet string, return the number of characters left out of 140. If the tweet is too long, return the number of characters over the limit as a negative number.

Think of it like a bank account. You start with 140 and spend as you type! 🐦

Examples

You can assume the input uses normal spaces and standard punctuation, and that special tokens like mentions and URLs will appear on their own rather than mixed into other text.

Example 1

Input: "just setting up my twttr"
Output: 116
24 plain characters used, 116 remaining. ✅

Example 2

Input: "Check out this link https://www.averylongurlthatgoesonnnnnn.com and this one https://short.co too!"
Output: 55
Two URLs each count as exactly 23 characters regardless of length. 55 characters to spare!
"""


def tweet_balance(tweet):
    # Start with the total budget of 140 characters
    balance = 140

    # Split the tweet into words to identify @mentions and URLs
    # split() without arguments also removes multiple spaces
    words = tweet.split()

    # Calculate the number of spaces between words
    # In a normal tweet, there are (word_count - 1) spaces
    # If the tweet is empty, spaces are 0
    num_spaces = len(words) - 1 if len(words) > 0 else 0
    balance -= num_spaces

    for word in words:
        if word.startswith('@'):
            # Rule 1: Username costs a fixed 20
            balance -= 20
        elif word.startswith('http://') or word.startswith('https://'):
            # Rule 2: URL costs a fixed 23
            balance -= 23
        else:
            # Rule 3: Anything else (text, punctuation) is counted normally
            balance -= len(word)

    return balance


# --- Tests ---
print(tweet_balance("just setting up my twttr"))
# Output: 116 (24 characters of text + no special rules)

print(tweet_balance("Check out this link https://www.averylongurlthatgoesonnnnnn.com and this one https://short.co too!"))
# Output: 55
