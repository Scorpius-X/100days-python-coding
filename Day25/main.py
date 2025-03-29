# with open("100days-python-coding/Day25/weather_data.csv") as data:
#     content = data.readlines()
#     print(content)

# import csv

# with open("100days-python-coding/Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for rows in data:
#         if rows[1] != "temp":
#             temperature.append(int(rows[1]))
#     print(temperature)       


import pandas

data = pandas.read_csv("100days-python-coding/Day25/weather_data.csv")
# data_dict = data.to_dict()

average = data["temp"].mean()
max_value = data["temp"].max()

# #get data in a column
# print(data.day)
# print(data.condition)

# #get data in a row
# print(data[data.day == "Sunday"])
# print(data[data.temp == data.temp.max()])

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# fahrenheit = celsius_to_fahrenheit(monday_temp)
# print(f"{fahrenheit} F")

