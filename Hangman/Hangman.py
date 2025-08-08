#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ["_" for _ in range(word_length)]
guessed_letters = []

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed
# all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#Check guessed letter

while "_" in display:
    guess = input("Guess a letter: ").lower()

    #checks for valid inputs
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    #checks if guess is in guessed letters
    if guess in guessed_letters:
        print("you have already guessed that letter, try again!")
        continue

    #checks if guess is correct
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print(f"Good job!, {guess} is in the word.")
    else:
        print(f"Oops!, {guess} is not in the word.")

    # Show progress
    print("Current word:", " ".join(display))

print(f"Congratulations you've won!, the correct answer is {chosen_word}")

