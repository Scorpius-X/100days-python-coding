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
move_list = [rock, paper, scissors]
print("Welcome to rock, paper, scissors!")
my_pick = input("what move would you like to pick?\n").lower()

# selectable moves
rps = ["rock", "paper", "scissors"]

# index of user input
try:
    rps_index = rps.index(my_pick)
except ValueError:
    print("please input out of rock, paper or scissors")
    exit()

print("You chose! "+ my_pick)
print(move_list[rps_index])

# executing computer pick
comp_pick = random.randint(0, 2)
print(f"Computer chose! {rps[comp_pick]}")
print(move_list[comp_pick])

if rps[comp_pick] == my_pick:
    print("It's a Tie")
elif comp_pick == 0 and rps_index == 2 or\
    comp_pick == 2 and rps_index == 1 or\
        comp_pick == 1 and rps_index == 0:
        print("You lose")
else:
    print("You win!")