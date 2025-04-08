import csv
import pandas

#TODO: Read Lines for the file and get list of lines:
"""
with open("./weather_data.csv", mode="r") as data_file:
    data = data_file.readlines()
    print(data)
"""
#TODO: Get row for the csv file and extract single column:
"""
with open("./weather_data.csv", mode="r") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)
"""
#TODO: Introduction to pandas library:

data = pandas.read_csv("weather_data.csv")
# data_temp = data["temp"].mean()
# data_temp = data["temp"].max()
# print(data_temp)
# average = sum(data_temp) / len(data_temp)
# print(average)

#TODO: Get max temperature row;

# temp_max = data.temp.max()
# row = data[data.temp == temp_max]
# print(row)
# OR
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
f = monday.temp[0]# * (9/5) + 32
print(f)

# TODO: Create dataframe from scratch;

# data_dic = {
#     "students": ["Ali", "Oren", "Zain"],
#     "scores": [8, 9, 5]
# }
# data = pandas.DataFrame(data_dic)
# print(data)
# data.to_csv("new_data.csv")

# TODO: Challenge;

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# color_data = data["Primary Fur Color"].value_counts()
# color_data.to_csv("squirrel_count.csv")

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dic = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Counts": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dic)
# df.to_csv("new_squirrel_count.csv")