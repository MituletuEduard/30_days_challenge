"""
Day 10: Write a Python program to find the second largest number in a list.
In today's Daily Challenge, we are looking at phone transcripts.

Complete the function that counts the number of unique words in a phone call.

Words are separated by spaces, and punctuation should be ignored. Treat words as the same regardless of capitalization.

Examples

Example 1

Input: "Mr. Watson, come here, I want to see you."
Output: 9
There are 9 unique words in the phone call transcript.

Example 2

Input: "Hello Neil and Buzz, I am talking to you by telephone from the Oval Room at the White House, and this certainly has to be the most historic telephone call ever made."
Output: 27
There are 27 unique words because "the", "and", "to", "telephone" are repeated.

🎟️ Don't forget to share the result on socials when you're done to enter a swag raffle!

#3 biggest telecom company in the world.
💡 Fun fact: Alexander Graham Bell co-founded AT&T (originally American Telephone & Telegraph) in 1885. It is now worth $200B and

#2: Bell actually preferred "Ahoy" as the standard telephone greeting. But Thomas Edison pushed for "Hello", which became the global standard.
💡 Fun fact
"""


def find_unique_words(transcript):
    # Write code below 💖
    words = transcript.split()
    unique_words = set()

    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
        if cleaned_word:
            unique_words.add(cleaned_word)
    return len(unique_words)


print(find_unique_words("Mr. Watson, come here, I want to see you."))
print(find_unique_words("Hello Neil and Buzz, I am talking to you by telephone from the Oval Room at the White House, and this certainly has to be the most historic telephone call ever made."))
print(find_unique_words("omg i am in this new cafe lol deadass the vibes here insane lol no cap yesss... we are just vibing haha omg yesss... can't even... deadass for real yesss OMG YESSS period yep yep... girl i feel you girl no cap okay... bet sounds good to me. bye girl love ya."))
