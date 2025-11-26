##################### Hard Starting Project ######################

import smtplib
import datetime as dt
import csv
import random

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.

my_email = ""
password = ""

now = dt.datetime.now()

day = now.day
month = now.month

letters = []

for x in range(1,4):
    letters.append(f"letter_{x}.txt")

random_letter = random.choice(letters)

with open('birthdays.csv', mode='r', newline='') as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        if day == int(row['day']) and month == int(row['month']):
            with open(f'letter_templates/{random_letter}', 'r') as letter_file:
                letter_content = letter_file.read().replace("[NAME]", f"{row['name']}")

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email,
                                        to_addrs=row['email'],
                                        msg=f"Subject:Happy Birthday!\n\n {letter_content}")