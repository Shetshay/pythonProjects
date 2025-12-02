import requests
from datetime import datetime
import time

MY_LAT = 35.373291 # Your latitude 35.373291
MY_LONG = -119.018715 # Your longitude -119.018715

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

def iss_location():
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
result = iss_location()


print(result)

print(sunset)
print(sunrise)
print(time_now.hour)

while True:
    time.sleep(60)
    if result and (sunset <= time_now.hour or time_now.hour <= sunrise):
        print("Look Up!!")



# BONUS: run the code every 60 seconds.

# print(iss_latitude)
# print(iss_longitude)


