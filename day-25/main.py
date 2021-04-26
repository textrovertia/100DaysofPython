# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Installing and using pandas to read data files
import pandas
data = pandas.read_csv("weather_data.csv") #data frame
print(data["temp"]) #series

print(data.to_dict())

temp_list = data["temp"].to_list()
print(temp_list)

print(data.temp.max)

# Get data in columns
print(data.condition)
print(data["condition"])

# Data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp
print(monday_temp)
print("mONDAY", monday_temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)


data_dict = {
    "students": ["Ama", "Kojo", "Adwoa"],
    "scores": [80, 82, 91]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data2.csv")