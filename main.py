import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from a .env file, if you're using python-dotenv
load_dotenv()

# Store sensitive data like API keys and credentials as environment variables for security.
api_key = os.getenv("WEATHER_API_KEY")  # Get API key from environment variable
my_lat = "37.983810"  # Latitude for the location (example: Athens, Greece)
my_long = "23.727539"  # Longitude for the location (example: Athens, Greece)
email = os.getenv("EMAIL")  # Get email from environment variable
password = os.getenv("EMAIL_PASSWORD")  # Get email password from environment variable
receiver_email = os.getenv("RECEIVER_EMAIL")  # Get recipient's email from environment variable

# Parameters for the OpenWeather API request
parameters = {
    "lat": my_lat,
    "lon": my_long,
    "exclude": "current,minutely,daily,alerts",  # Exclude unnecessary data
    "units": "metric",  # Use metric units (Celsius for temperature)
    "appid": api_key  # API key for authentication
}

# Send a request to the OpenWeather API
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()  # Check for any errors in the request
weather_data = response.json()  # Parse the response to JSON format

# Check if the weather ID indicates rain (weather ID < 700 means precipitation)
will_rain = False
for i in range(11):  # Check the weather forecast for the next 11 hours
    if weather_data["hourly"][i]["weather"][0]["id"] < 700:
        will_rain = True

# If rain is expected, send an email notification
if will_rain:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Secure the connection using TLS
        connection.login(user=email, password=password)  # Login with email credentials
        # Send the email notification
        connection.sendmail(
            from_addr=email,
            to_addrs=receiver_email,  # Replace with the recipient's email address
            msg="Subject: Hello rain!\n\nDon't forget your umbrella!"  # Email content
        )

