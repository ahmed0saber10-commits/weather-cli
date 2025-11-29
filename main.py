#!/usr/bin/env python3
import requests

API_KEY = "PUT_YOUR_API_KEY_HERE"  # ممكن تسجل على openweathermap.org
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return
        print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind speed: {data['wind']['speed']} m/s\n")
    except Exception as e:
        print("Error fetching data:", e)

def main():
    print("مرحبًا في Weather CLI!")
    city = input("اكتب اسم المدينة: ").strip()
    if city:
        get_weather(city)
    else:
        print("اكتب اسم مدينة صحيح.")

if __name__ == "__main__":
    main()
