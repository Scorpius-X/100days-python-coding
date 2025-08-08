print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
path = input("You came across two pathways on your way into the island, what path do you intend to take? left or right? ").lower()

if path == "left":
    waterpath = input("You successfully escaped the booby trap, you came across a mysterious lake, you have to cross-over, do you intend to swim or wait? ").lower()
    if waterpath == "wait":
        door = input("You waited and saw a stone lever that created a path through the lake, you came across three doors, one yellow, one blue, and one green. which door will you open? ").lower()
        if door == "yellow":
            print("Congratulations you have Discovered the treasure!")
        elif door == "Blue":
            print("You got caught by a blue monster, you died!")
        else:
            print("You got caught by a carnivorous green plant, you've been eaten up")

    else:
        print("You were attacked by pirannas, you died!, Game Over!")

else:
    print("You stepped into a booby trap and died, Game Over!")



