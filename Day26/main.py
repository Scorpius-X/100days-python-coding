student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


nato_data = pandas.read_csv("100days-python-coding\\Day26\\nato_phonetic_alphabet.csv")
nato_dict = {row.letter : row.code for (index, row) in nato_data.iterrows()}

# def natofunc():
#     while True:
#         try:
#             word = input("Enter a word: ").upper()
#             output_list = [nato_dict[letter] for letter in word]
#             print(output_list)
#             break
#         except KeyError:
#             print("Sorry, please input only letters in the alphabet")

# natofunc()

def natofunc2():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
        print(output_list)
    except KeyError:
        print("Sorry, please input only letters in the alphabet")
        natofunc2()

natofunc2()
