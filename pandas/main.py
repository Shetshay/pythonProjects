import pandas
#def practice():
    #data = pandas.read_csv("weather_data.csv")
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
    # data_school.to_csv("new_data.csv") # create new data

#practice()

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250116.csv")
#print(squirrel_data["Primary Fur Color"])

#print(squirrel_data["Primary Fur Color"].unique())
(squirrel_data["Primary Fur Color"].unique())

squirrel_fur_color = (squirrel_data["Primary Fur Color"].unique()[1::])
squirrel_count_fur_color = []

for color in squirrel_fur_color:
    print(squirrel_data.count(squirrel_fur_color))

#squirrel_count_fur_color = (squirrel_data["Primary Fur Color"].count())

fur_color_count = {
    "Fur Color": squirrel_fur_color,
    #"Count": squirrel_count_fur_color
}

squirrel_query = pandas.DataFrame(fur_color_count)
squirrel_query.to_csv("squirrel_query.csv") # create new data

print(squirrel_query)