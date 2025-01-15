# with open("./weather_data.csv", mode='r') as data:
#     weatherData = data.readlines()
#
# print(weatherData)

import csv

with open("./weather_data.csv") as data_file:
    data = csv.DictReader(data_file)
    #print(data)
    temperatures = []
    for row in data:
        if row['temp']:
            temperatures.append(int(row['temp']))
        #print(row)
print(temperatures)