# create a caesar cipher code that encodes and decodes messages, accepting inputs as well as asking whether to end or continue
from art import logo
from Caesar_cipher import alphabet

def caesar(start_text, shift_number, cypher_direction):
    cipher_text = ""
    if cypher_direction == "decode":
        shift_number*= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = alphabet[position + shift_number]
            cipher_text += new_position
        else:
            cipher_text += char
    print(f"Your {cypher_direction}d text is {cipher_text}")

print(logo)
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text= text, shift_number= shift, cypher_direction= direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")