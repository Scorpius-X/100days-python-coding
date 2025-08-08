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
# Main list of Rock, paper, scissors
main_rps = [rock, paper, scissors]

your_pick = input("Please input out of rock, paper, scissors: ").lower()

# list of user input
rps =["rock", "paper", "scissors"]

# get the index of the users choice
try:
    rps_index = rps.index(your_pick)
except ValueError:
    print("Please input out of rock, paper, scissors")
    exit()

print("You chose!")
print(main_rps[rps_index])

# generate computers choice
computer_pick = random.randint(0,2)

print("Computer chose!")

print(main_rps[computer_pick])


if your_pick == rps[computer_pick]:
    print("It's a Tie!")

elif rps_index == 0 and computer_pick == 1:
    print("You lose!")
elif rps_index == 1 and computer_pick == 2:
    print("you lose!")
elif rps_index == 2 and computer_pick == 0:
    print("you lose!")
elif rps_index == 0 and computer_pick == 2:
    print("you win!")
elif rps_index == 1 and computer_pick == 0:
    print("you win!")
elif rps_index == 2 and computer_pick == 1:
    print("you win!")

