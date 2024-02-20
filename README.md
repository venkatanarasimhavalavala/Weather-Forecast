# Weather-Forecast
A weather forecast application using python and weather data from an API
Imports requests: Enables HTTP requests to interact with the API.
Defines api_key: Holds your unique OpenWeatherMap API key (remember to update it with your own).
Prompts for city name: Asks the user to enter a city name using input.
Retrieves weather data:
f-string constructs the API URL dynamically, incorporating the city name and user's preferred units (imperial in this case).
requests.get(url) sends a GET request to the API and stores the response.
json() method parses the JSON response into a dictionary.
Extracts relevant data:
weather = weatherdata.json()['weather'][0]['main']: Gets the main weather description (e.g., "Clouds").
temp = round(weatherdata.json()['main']['temp']): Rounds the current temperature in degrees Fahrenheit.
hum = round(weatherdata.json()['main']['humidity']): Rounds the humidity percentage.
Prints results:
Displays the city name, weather description, temperature, and humidity in an easily readable format.
