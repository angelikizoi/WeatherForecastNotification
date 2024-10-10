# Weather Notification Script

This is a Python script that checks the weather for a specific location and sends an email notification if rain is expected in the next 11 hours. It uses the OpenWeather API to retrieve weather data and the `smtplib` library to send emails.

## Features

- **Fetch Weather Data**: Retrieves weather data for a specified latitude and longitude using the OpenWeather API.
- **Rain Notification**: If rain is forecasted in the next 11 hours, it sends an email notification to remind the user to take an umbrella.
- **Environment Variables**: Sensitive data such as API keys and email credentials are stored in environment variables for security.

## Prerequisites

- **Python 3.x** installed.
- An OpenWeather API key.
- A Gmail account (or another email service with SMTP support) to send notifications.
- `python-dotenv` package for loading environment variables from a `.env` file (optional but recommended).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/angelikizoi/WeatherForecastNotification.git
   cd WeatherForecastNotification
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   You can use a `.env` file to store your sensitive data (API key, email, and password). Create a `.env` file in the project directory:

   ```
   WEATHER_API_KEY=your_openweather_api_key
   EMAIL=your_email@example.com
   EMAIL_PASSWORD=your_email_password
   RECEIVER_EMAIL=receiver_email@example.com
   ```

5. **Run the script**:
   ```bash
   python main.py
   ```

## Environment Variables

The following environment variables are required:

- `WEATHER_API_KEY`: Your OpenWeather API key.
- `EMAIL`: The email address used to send notifications.
- `EMAIL_PASSWORD`: The email password or app-specific password (if using Gmail).
- `RECEIVER_EMAIL`: The email address that will receive the rain notifications.

## Usage

- The script fetches weather data for the location specified by `my_lat` (latitude) and `my_long` (longitude) in the code.
- If rain is expected within the next 11 hours, the script sends an email notification to the specified recipient.

## Example

The script is set to check the weather for **Athens, Greece** (`37.983810` latitude and `23.727539` longitude). If rain is expected, an email will be sent with the subject "Hello rain!" and the message "Don't forget your umbrella!"

### Example Email Notification

```
Subject: Hello rain!
Body:
Don't forget your umbrella!
```

## Customization

You can customize the latitude, longitude, email recipient, and email message by modifying the respective variables in the script.

## Dependencies

- `requests`: To make HTTP requests to the OpenWeather API.
- `smtplib`: To send emails via SMTP.
- `python-dotenv`: To load environment variables from a `.env` file (optional).

