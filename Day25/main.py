import pandas


data = pandas.read_csv("100days-python-coding/Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# fur_color = data.get("Primary Fur Color")
# count = data["Primary Fur Color"].value_counts()
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

#create a dataframe using python Dictionary

data_dict = {
    
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

#create a Dataframe using pandas and initialise it using the dictionary

df = pandas.DataFrame(data_dict)
df.to_csv("100days-python-coding/Day25/Squirrel_count.csv")


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


# data = pandas.read_csv("100days-python-coding/Day25/weather_data.csv")
# data_dict = data.to_dict()

# average = data["temp"].mean()
# max_value = data["temp"].max()
# print(average)
# print(max_value)

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

#creating a dataframe from scratch
# data_dict = {
#     "students": ["amy", "david", "joseph"],
#     "scores": [20, 30, 25],
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("100days-python-coding/Day25/new_data.csv")
