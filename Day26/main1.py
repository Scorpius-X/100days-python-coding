student_dict = {
    "student": ["alex","draco","tom"],
    "score": [50, 34, 56]
}

for (key,value) in student_dict.items():
    print(key,value)

import pandas

student_dict_dataframe = pandas.DataFrame(student_dict)
print(student_dict_dataframe)

# for (index,row) in student_dict_dataframe.iterrows():
#     if row.student == "alex":
#         print(row.score)