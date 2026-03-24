def decode_message(message, shift):
    decoded_text = ""
    addition = ord('a')
    for char in message:
        if char == " ":
            # we should keep the spaces in the decoded message
            decoded_text += " "
        else:
            # we need to find the current index of the character in the alphabet, then shift it back by the given number of positions, and finally convert it back to a character
            current_index = ord(char) - addition
            # we use modulo 26 to wrap around the alphabet if the shift goes past 'a'
            new_index = (current_index - shift) % 26
            # we add the new index to the addition to get the ASCII value of the decoded character, and then convert it back to a character
            decoded_text += chr(new_index + addition)

    return decoded_text


# Test
print(decode_message("dwwdfn dw gdzq", 3))           # attack at dawn
print(decode_message("ymj bfqwzx bfx ufzq", 5))      # the walrus was paul
print(decode_message("ai wlsyph womt kcq gpeww", 4))
# we should have fun coding
