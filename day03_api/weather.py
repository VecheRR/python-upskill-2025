import os
import requests
from dotenv import load_dotenv
import argparse
import sys

load_dotenv()
API_KEY = os.getenv('OW_API_KEY')
if not API_KEY:
    sys.exit("❌ OW_API_KEY не найден в .env")

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city: str) -> dict:
    params = {
        "q": city,
        "units": "metric",   # градусы Цельсия
        "lang": "ru",
        "appid": API_KEY,
    }
    r = requests.get(BASE_URL, params=params, timeout=5)
    r.raise_for_status()   # 4xx/5xx → исключение
    return r.json()

def main() -> None:
    parser = argparse.ArgumentParser(description="Погода по городу")
    parser.add_argument("-c", "--city", required=True, help="Название города")
    args = parser.parse_args()

    data = fetch_weather(args.city)
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"].capitalize()
    print(f"{data['name']}: {desc}, {temp}°C")

if __name__ == "__main__":   # pragma: no cover
    main()