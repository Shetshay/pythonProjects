import pandas
#def practice():
    #data = pandas.read_csv("weather_data.csv-filepath")
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

    # monday = data[data.day == "Monday"]

    # convert to Fahrenheit from Celsius
    # print(monday.replace(monday.temp[0], (monday.temp[0] * (9/5) + 32)))



    # Create a dataframe from scratch
    # data_dict = {
    #     "students": ["Amy", "James", "Angela"],
    #     "scores": [76, 56, 65]
    # }
    # data_school = pandas.DataFrame(data_dict)
    # print(data_school)
    # data_school.to_csv("new_data.csv-filepath") # create new data

#practice()

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250116.csv")
#print(squirrel_data["Primary Fur Color"])

#print(squirrel_data["Primary Fur Color"].unique())
(data["Primary Fur Color"].unique())

squirrel_fur_color = (data["Primary Fur Color"].unique()[1::])
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"]) # inside the data column, if primary fur color == gray
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

squirrel_color_count = (gray_squirrel, cinnamon_squirrel, black_squirrel)


fur_color_count = {
    "Fur Color": squirrel_fur_color,
    "Count": squirrel_color_count
}

df = pandas.DataFrame(fur_color_count)
df.to_csv("squirrel_query.csv-filepath") # create new data

print(df)