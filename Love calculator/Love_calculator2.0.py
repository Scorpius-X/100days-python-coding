"""You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."""

name1 = input("Please input the first name! ").lower()
name2 = input("Please input the second name! ").lower()
fusion = name1 + name2
T = fusion.count("t")
R = fusion.count("r")
U = fusion.count("u")
E = fusion.count("e")

true = T + R + U + E

L = fusion.count("l")
O = fusion.count("o")
V = fusion.count("v")
E = fusion.count("e")

love = L + O + V + E
lovescore = str(true)+ str(love)
total = int(lovescore)
if total < 10 and total > 90:
    print("Calculating your lovescore...")
    print(f"your love score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print("Calculating your lovescore...")
    print(f"your love score is {total}, you are alright together.")
else:
    print("Calculating your lovescore...")
    print(f"your love score is {total}")

