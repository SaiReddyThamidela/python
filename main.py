from symbol import parameters
from twilio.rest import Client
import requests
API_KEY = "a83ced151a24947b0efb88bc61f9c4a3"
MY_LAT=13.106745
MY_LNG=80.096954
MY_NUM= "+14155238886"
ACCOUNT = 'AC07c830c2d358f52502c62f40c27f9c1e'
AUTH = "a7cfcea2202ab01ef5491cf8a4865316"

parameters = {
    "lat":MY_LAT,
    "lon":MY_LNG,
    "appid":API_KEY,
    "units":"metric",
    "cnt":4,
}

res = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
data = res.json()
is_rain =False
for i in range(0,4):
    if data["list"][i]["weather"][0]["id"]>499:
        print(data["list"][i]["weather"][0]["id"])
        is_rain=True
if is_rain:
    client = Client(ACCOUNT, AUTH)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today. Remember to bring an umbrella",
        to='whatsapp:+919573585568'
    )

    print(message.sid)