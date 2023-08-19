import requests


def get_date(place, forecast_days):
    api_key = "cf777969b9400477fb1b2fe6f6e46b3b"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"

    responce = requests.get(url)
    data = responce.json()
    filterd_data = data["list"]
    no_days = 8 * forecast_days
    filterd_data = filterd_data[:no_days]
    return data

if __name__ == "__main__":
    print(get_date(place="tokyo",forecast_days=None))

