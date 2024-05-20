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

should_continue = True
print(logo)
while should_continue:
    direction = input("Please choose whether to 'encode' or 'decode' your message: \n").lower()
    text = input("Please type in your message: ").lower()
    shift = int(input("Please input the shift number: "))
    shift = shift % 26
    caesar(start_text= text, shift_number= shift, cypher_direction= direction)
    result = input("Type 'yes' or 'no' if you would like to continue: ")

    if result == "no":
        should_continue = False
        print("Thanks Goodbye")
