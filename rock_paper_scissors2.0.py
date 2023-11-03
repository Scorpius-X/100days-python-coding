import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of possible moves
main_rps = [rock, paper, scissors]

your_pick = input("Choose among rock, paper, scissors: ").lower()

# List of possible choices
rps = ["rock", "paper", "scissors"]

# Get the index of the user's choice
try:
    rps_index = rps.index(your_pick)
except ValueError:
    print("Invalid choice. Please choose among rock, paper, or scissors.")
    exit()

print("You chose!")
print(main_rps[rps_index])

# Generate the computer's choice
computer_pick = random.randint(0, 2)

print("Computer chose!")
print(main_rps[computer_pick])

if your_pick == rps[computer_pick]:
    print("It's a Tie!")
elif (your_pick == "rock" and rps[computer_pick] == "paper") or \
     (your_pick == "paper" and rps[computer_pick] == "scissors") or \
     (your_pick == "scissors" and rps[computer_pick] == "rock"):
    print("You lose!")
else:
    print("You win!")
