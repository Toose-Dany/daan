import requests

def simple_weather():
    api_key = 'bd391fbb5b4f55e382b9ca3b4731602a'
    city = ("Tver', RU")

    url = 'https://api.openweathermap.org/data/2.5/weather'

    try:
        response = requests.get(url)
        data = response.json()

        print(f"Погода в {data['name']}:")
        print(f"Температура: {data['main']['temp']}°C")
        print(f"Ощущается как: {data['main']['feels_like']}°C")
        print(f"Погода: {data['weather'][0]['description']}")
        print(f"Влажность: {data['main']['humidity']}%")


    except:
        print("Не удалось получить данные о погоде")

simple_weather()















