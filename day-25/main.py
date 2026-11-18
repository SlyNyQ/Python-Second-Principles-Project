import csv
import pandas

# data = pandas.read_csv("weather_data.csv")
#print(type(data))
#data_dict = data.to_dict()
#print(data_dict)

# temp_list = data["temp"].to_list()
#print(type(data["temp"]))

#ave_temp = sum(temp_list) / len(temp_list)
# OR
# ave_temp = data["temp"].mean()
#
# max_temp = data["temp"].max()


#print(temp_list)
#print(ave_temp)
#print(max_temp)

#print(data["condition"])
# OR
#print(data.condition)

#print(ave_temp)
#print(max_temp)

#TODO: Get data in rows
#print(data[data.day == "Monday"])
#print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# #print(monday.condition)
#
# def c_to_F(temp):
#     return temp *(9/5) + 32
#
#
# print(c_to_F(monday.temp[0]))

#TODO: Create data frame

# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores": [76, 56, 65]
# }
# student_data = pandas.DataFrame(data_dict)
# student_data.to_csv("student_data.csv")


#TODO: Open the weather_data.csv Use .readline() to create a list called data that contains the values
# from the csv file

# with open("weather_data.csv", mode="r") as file:
#     data = csv.reader(file)
#     temperature = []
#     days = []
#     conditions = []
#     for row in data:
#         print(row)
#         if row[0] != "day":
#             days.append(row[0])
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         if row[2] != "condition":
#             conditions.append(row[2])
#

    # TODO: Extract temp column from reader

#     print(temperature)
#     print(days)
#     print(conditions)
    ##OR
    # data = file.readlines()

    ##OR
    # data = []
    # day = []
    # temp = []
    # condition = []
    # header_line = file.readline(0)
    # for line in range(0, len(file.readline())):
    #     data_line = file.readline()
    #     data_line = data_line.replace("\n", "")
    #
    #     data.append(data_line)
    #print(data)

#TODO: READ original CSV
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#TODO: Identify the fur color
#colour_list = squirrel_data["Primary Fur Color"].to_list
fur_colour = data["Primary Fur Color"]
# monday = data[data.day == "Monday"]

gray_sqrls = data[data["Primary Fur Color"] == "Gray"]
red_sqrls = data[data["Primary Fur Color"] == "Cinnamon"]
black_sqrls = data[data["Primary Fur Color"] == "Black"]

#TODO: Count the colours
print(len(gray_sqrls))
print(len(red_sqrls))
print(len(black_sqrls))

#print(gray == "Cinnamon")
gray_count = len(gray_sqrls)
red_count = len(red_sqrls)
black_count = len(black_sqrls)


#TODO: Use pandas to create a csv called squirrel_count

data_dict = {
    "Fur Color": ["gray","red","black"],
    "count": [gray_count, red_count, black_count],
}
squirrel_data = pandas.DataFrame(data_dict)
#print(squirrel_data)
squirrel_data.to_csv("squirrel_count.csv")

# for col in fur_colour:
#     print(col)
#     if fur_colour[col] == "Gray":
#         gray_count += 1
#     elif fur_colour[col] == "Red":
#         red_count += 1
#     elif fur_colour[col] == "Black":
#         black_count += 1
#
# print(f"Gray count is = {gray_count}")
# print(f"Red count is = {red_count}")
# print(f"Black count is = {black_count}")

