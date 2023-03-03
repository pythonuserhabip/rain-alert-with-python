import requests
import smtplib

my_email = "pythonuserhabip@gmail.com"
password = "zmvhkvlxiinovaec"


OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "fc56b905e2496f17a8e5ecfc0986eba6"

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
                            to_addrs="habip1834@gmail.com",
                            msg=f"Subject:Weather!\n\nIt's rainy today, don't forget your umbrella"
                            )
