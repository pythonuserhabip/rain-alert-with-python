import requests
import smtplib

my_email = "YOUR E-MAİL ADDRESS"
password = "YOUR PASSWORD"


OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "YOUR APİ KEY"

weather_params = {
     "lat": -36.848461,
     "lon": 174.763336,
     "appid": api_key,
     "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
     condition_code  = hour_data["weather"][0]["id"]
     if int(condition_code) < 700:
          will_rain = True

if will_rain:
    # print("take an umbrella")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="MAIL ADDRESS YOU WISH TO SEND",
                            msg=f"Subject:Weather!\n\nIt's rainy today, don't forget your umbrella"
                            )
