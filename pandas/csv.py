import csv

with open("./weather_data.csv") as data_file:
    data = csv.DictReader(data_file)
    temperatures = []
    for row in data:
        if row['temp']:
            temperatures.append(int(row['temp'])) # Create an object that operates like a regular reader but maps the
            # information in each row to a dict whose keys are given by the optional fieldnames parameter.
print(temperatures)