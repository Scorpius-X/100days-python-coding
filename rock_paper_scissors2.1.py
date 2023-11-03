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

# Dictionary mapping choices to their indices
rps_dict = {"rock": 0, "paper": 1, "scissors": 2}

if your_pick not in rps_dict:
    print("Invalid choice. Please choose among rock, paper, or scissors.")
    exit()

# Get the index of the user's choice
user_index = rps_dict[your_pick]

print("You chose!")
print(main_rps[user_index])

# Generate the computer's choice
computer_pick = random.randint(0, 2)

print("Computer chose!")
print(main_rps[computer_pick])

if user_index == computer_pick:
    print("It's a Tie!")
elif (user_index == 0 and computer_pick == 1) or (user_index == 1 and computer_pick == 2) or (user_index == 2 and computer_pick == 0):
    print("You lose!")
else:
    print("You win!")
