import requests
import streamlit
import streamlit as st

def get_date(place, forecast_days):
    # api_key = st.secrets["API_KEY"]
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid=cf777969b9400477fb1b2fe6f6e46b3b&units=metric"

    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    no_days = 8 * forecast_days
    filtered_data = filtered_data[:no_days]

    return filtered_data


if __name__ == "__main__":
    print(get_date(place="tokyo", forecast_days=2))

