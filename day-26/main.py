# Former way
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# New way
new_list_2 = [n+1 for n in numbers]
print(new_list_2)

# new_list = [new_item for item in list if test]


# Interactive session

list_2 = []
with open("file1.txt") as file1:
    list_1 = file1.readlines()
    list_1 = [int(item.strip()) for item in list_1]
    print(list_1)

with open("file2.txt") as file2:
    list_2 = file2.readlines()
    list_2 = [int(item.strip()) for item in list_2]
    print(list_2)

common_items = [num for num in list_1 if num in list_2]
print(common_items)


# Interactive session

sentence = "What is my name?"

# result = {new_key:new_value for item in list}

new_dictionary = {word:len(word) for word in sentence.split()}
print(new_dictionary)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14
}

weather_f = {day: (temp*9/5) for (day, temp) in weather_c.items() }
print(weather_f)

# Looping through Pandas Dataframe
student_dict = {
    "student": ["Angela", "Kwesi", "Lily"],
    "score": [90, 82, 91]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(index)
    print(row.score)