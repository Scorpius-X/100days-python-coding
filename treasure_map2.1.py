line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
#create a nested list
map = [line1, line2, line3]
print("Welcome to the Treasure map! X marks the spot of the treasure")
position = input("Where would you like to hide the map? ")
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
print(letter)
print(letter_index)
# index_number = int(position[1])-1
# map[index_number][letter_index] = "X"
# print(f"{line1}\n{line2}\n{line3}")