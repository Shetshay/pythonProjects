import smtplib



import random
import datetime as dt

array_of_quotes = []

file_path = "quotes.txt"  # Replace with the actual path to your file

try:
    with open(file_path, 'r') as file:
        for line in file:
            # Each 'line' variable will contain one line from the file,
            # including the newline character '\n' at the end (if present).
            array_of_quotes.append(line.strip())  # .strip() removes leading/trailing whitespace, including '\n'
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#print(array_of_quotes)


now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.weekday()
#print(day_of_week)

if day_of_week == 0:
    my_email = ""
    password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="",
                            msg=f"Subject:Happy Monday!\n\n {random.choice(array_of_quotes)}")