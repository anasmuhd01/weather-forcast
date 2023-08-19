import requests


def get_date(place, forecast_days,kind):
    api_key = "cf777969b9400477fb1b2fe6f6e46b3b"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"

    responce = requests.get(url)
    data = responce.json()
    filterd_data = data["list"]
    no_days = 8 * forecast_days
    filterd_data = filterd_data[:no_days]

    if kind == "temperature":
        filterd_data = [dict["main"]["temp"] for dict in filterd_data]
    if kind == "sky":
        filterd_data = [dict["weather"][0]["main"] for dict in filterd_data]
    return filterd_data

if __name__ == "__main__":
    print(get_date(place="tokyo",forecast_days=2,kind="temperature"))

