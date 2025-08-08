# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height x wall width) ÷ coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 * 4) / 5
#                = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Example Input
# 3
# 9
# Example Output
# You'll need 6 cans of paint.
import math

height = int(input("Please input the height: "))
width = int(input("Please input the weight: "))
coverage = 5


def paint_calc(height, width, coverage):
    num_cans = math.ceil((height * width)/ coverage)
    print(f"You'll need {num_cans} cans of paint.")

paint_calc(height, width, coverage)

