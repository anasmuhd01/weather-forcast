import streamlit as st
import plotly.express as px
from get_temp import get_date

st.header("weather forcast for the next days")
place = st.text_input("place")
forecast_days = st.slider("enter temp value", 1, 5)
option = st.selectbox("select data to view", ('temperature', 'sky'))
st.subheader(f"{option} for the next {forecast_days} days {place}")


try:
    if place:
        filtered_data = get_date(place, forecast_days)
        if option == "temperature":
            st.caption("temperature in Celsius")
            temperature = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"]for dict in filtered_data]

            fig = px.line(x=dates, y=temperature, labels={"x": "date","y": "temperature"})
            st.plotly_chart(fig)

        if option == "sky":
            image = {"Clear":"images/clear.png", "Rain": "images/rain.png"
                     , "Clouds":"images/cloud.png", "Snow": "images/snow.png"}

            sky_conditon = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [image[condition] for condition in sky_conditon]

            st.image(image_path,width=115)
except KeyError:
    st.info(f"there is no place named {place}. please enter valid place")