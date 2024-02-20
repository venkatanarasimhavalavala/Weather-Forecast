import requests
api_key = "5abd675a00529783ff88f660f66ddc69"
userinput = input("enter the city name: ")
weatherdata = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={userinput}&units=imperial&APPID={api_key}")
weather = weatherdata.json()['weather'][0]['main']
temp = round(weatherdata.json()['main']['temp'])
hum = round(weatherdata.json()['main']['humidity'])
print(f"the weather in {userinput} is: {weather}")
print(f"the temperature in {userinput} is: {temp}")
print(f"the humidity in {userinput} is: {hum}")
