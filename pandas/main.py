import pandas

data = pandas.read_csv("weather_data.csv")
# #print(type(data))
# #print(data["temp"])
#
# data_dict = data.to_dict()
# #print(data_dict)
#
# temp_list = data["temp"].to_list()
# #print(temp_list)
#
# print(data["temp"].max())

#print(data[data.day == "Monday"])

#print(data[data.temp == (data["temp"].max())])

monday = data[data.day == "Monday"]

# convert to Fahrenheit from Celsius
print(monday.replace(monday.temp[0], (monday.temp[0] * (9/5) + 32)))



# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_school = pandas.DataFrame(data_dict)
print(data_school)
data_school.to_csv("new_data.csv") # create new data