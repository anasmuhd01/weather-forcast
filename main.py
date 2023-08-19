import streamlit as st
import plotly.express as px
from get_temp import get_date

st.header("weather forcast for the next days")
place = st.text_input("place")
forecast_days = st.slider("enter temp value", 1, 5)
option = st.selectbox("select data to view", ('temperature', 'sky'))
st.subheader(f"{option} for the next {forecast_days} days {place}")


d, t = get_date(place, forecast_days, option)

fig = px.line(x=d, y=t, labels={"x": "date","y": "temp"})
st.plotly_chart(fig)
