import requests

api_key='5216f3f32dde8bfa1f7e8ad836b78305'

user_input=input("Enter City:")

weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric")

if weather_data.json()['cod']=='404':
    print("no city found")

else:
    weather=weather_data.json()['weather'][0]['main']
    temp=round(weather_data.json()['main']['temp'])

    print(f"the weather in {user_input} is: {weather}")
    print(f"the temperature in {user_input} is: {temp}")


