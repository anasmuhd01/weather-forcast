import streamlit as st
import plotly.express as px
import pandas as pd
st.header("weather forcast for the next days")
place = st.text_input("place")
temp = st.slider("enter temp value", 1, 5)
option = st.selectbox("select data to view", ('temperature', 'sky'))
st.subheader(f"{option} for the next {temp} days {place}")


def get_date(tempe):
    dates = ["1998-10-10", "1998-11", "1998-12-10"]
    temp = [10,20,30]
    temp = [tempe * i for i in temp]
    return dates,temp


d, t = get_date(temp)
fig = px.line(x=d, y=t, labels={"x": "date","y": "temp"})
st.plotly_chart(fig)
