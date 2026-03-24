"""
One part of the proposal is about URLs. URL stands for Uniform Resource Locator. It is the unique address used to identify and locate a webpage, image, or document on the internet. Frequently referred to as a web address".

Given a string representing a web address, determine if it's a valid URL or not.

For our validator, make sure it follows these rules:

It starts with http:// or https://
The domain must contain at least one dot .
The domain only contains letters, digits, hyphens -, or dots .
Return the string "valid" if it is, or "invalid" if it isn't.

Examples

Example 1

Input: https://codedex.io
Output: valid
Example 2

Input: https://netflixcom
Output: invalid
Example 3

Input: http://en.wikipedia.org
Output: valid
Fun fact: Berners-Lee has expressed regret over the "clumsy" syntax, specifically the ://. 🤭

Fun fact #2: https came about five years after the original proposal (which only had http).
"""


def check_url(address):
    # Write code below 💖
    if (address[:8] == "https://" or address[:7] == "http://"):
        if ('.' in address[9:]):
            for char in address[9:]:
                if not (char.isalnum() or char in ['-', '.']):
                    return "invalid"
            return "valid"
    return "invalid"


print(check_url("https://codedex.io"))
print(check_url("https://netflixcom"))
print(check_url("http://en.wikipedia.org"))
