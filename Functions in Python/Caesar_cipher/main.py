from art import logo
from Caesar_cipher import alphabet

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_number, cypher_direction):
    cipher_text = ""
    if cypher_direction == "decode":
        shift_number*= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = alphabet[position + shift_number]
        cipher_text += new_position
    print(f"Your {cypher_direction}d text is {cipher_text}")

caesar(start_text= text, shift_number= shift, cypher_direction= direction)