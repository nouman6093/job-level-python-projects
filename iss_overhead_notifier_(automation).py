#this code will notify you via email if international space staton is at your location
#note that you will also need to upload this to a server if you want it to be automated
import smtplib
from dateutil import parser
import requests
import datetime
import time

MY_LAT = #here enter your latitude get it from: https://www.latlong.net/
MY_LNG =  #here enter your longitude get it from: https://www.latlong.net/
MY_EMAIL = "enter your email here"
MY_PASSWORD = "enter password here which you got from google security"

def is_iss_overhead():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    data1 = response1.json()
    iss_latitude = float(data1["iss_position"]["latitude"])
    iss_longitude = float(data1["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LNG + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    #converting utc time to pst time (+5 hours):
    sunrise_utc = parser.parse(sunrise)
    sunset_utc = parser.parse(sunset)
    sunrise_local = sunrise_utc + datetime.timedelta(hours=5)
    sunset_local = sunset_utc + datetime.timedelta(hours=5)

    now = datetime.datetime.now().hour

    if now >= sunset_local or now <= sunrise_local: #its dark
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look Up!\n\nThe ISS is above you in the sky")
